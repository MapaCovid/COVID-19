# Import required libraries
import pickle
import copy
import pathlib
import dash
import math
from datetime import datetime as dt
import pandas as pd
from dash.dependencies import Input, Output, State, ClientsideFunction
import dash_core_components as dcc
import dash_html_components as html
from dash.exceptions import PreventUpdate
from src.DataLoader import DataLoader
import dash_table
from typing import Tuple

# Multi-dropdown options
from controls import COUNTIES, WELL_STATUSES, WELL_TYPES, WELL_COLORS

# get relative data folder
PATH = pathlib.Path(__file__).parent
DATA_PATH = PATH.joinpath("data").resolve()

app = dash.Dash(__name__, meta_tags=[{"name": "viewport", "content": "width=device-width"}])
app.scripts.config.serve_locally = True
app.title = 'COVID-19 Chile'
server = app.server


def process_daily_df(raw_df: pd.DataFrame) -> pd.DataFrame:
    raw_df = raw_df.copy(deep=True)
    raw_df.sort_values(by='id_reg', inplace=True)
    raw_df.rename(columns={
        'nombre_reg': 'Región',
        'casos_totales': 'Contagiados',
        'fallecidos_totales': 'Fallecidos',
        'recuperados_totales': 'Recuperados'
    }, inplace=True)
    raw_df.drop(columns=['casos_nuevos', 'fallecidos_nuevos', 'recuperados_nuevos', 'id_reg'],
                inplace=True)

    # finally, generates total row
    infected_total = raw_df['Contagiados'].sum()
    death_total = raw_df['Fallecidos'].sum()
    recovery_total = raw_df['Recuperados'].sum()
    raw_df = raw_df.append({'Región': 'Total',
                            'Contagiados': infected_total,
                            'Fallecidos': death_total,
                            'Recuperados': recovery_total}, ignore_index=True)
    return raw_df


def process_town_names_by_region(raw_df: pd.DataFrame) -> dict:
    names = {}
    for region_id in raw_df['id_region'].unique():
        sub_df = raw_df[raw_df['id_region'] == region_id]
        names[region_id] = list(sub_df['nombre_comuna'].unique())
    return names


# getting and processing data
dataLoader = DataLoader()
region_ids = dataLoader.REGION_IDS

# region stats
country_stats = dataLoader.get_country_stats()
last_day, last_df = dataLoader.get_last_day()
reg_latest_accum = process_daily_df(last_df)
reg_stats = dataLoader.get_country_data()
region_opts = [{'label': region_ids[region_id], 'value': region_id} for region_id in region_ids.keys()]

# town data
town_stats = dataLoader.get_region_data()
town_names = process_town_names_by_region(town_stats[list(town_stats.keys())[0]])

# accessing
infected = country_stats['contagiados']['accumulated'][country_stats['contagiados']['accumulated'].last_valid_index()]
deaths = country_stats['fallecidos']['accumulated'][country_stats['fallecidos']['accumulated'].last_valid_index()]
recovered = country_stats['recuperados']['accumulated'][country_stats['recuperados']['accumulated'].last_valid_index()]

# creating main graph data
colors = ["#fac1b7", "#a9bb95", "#92d8d8"]
data = []
for i, segment in enumerate(['contagiados', 'fallecidos', 'recuperados']):
    data.append(dict(type="scatter",
                     mode="lines+markers",
                     name=segment,
                     x=country_stats[segment]['accumulated'].index,
                     y=country_stats[segment]['accumulated'],
                     line=dict(shape="spline", smoothing=1, width=1, color=colors[i]),
                     marker=dict(symbol="diamond-open")))

# creating main graph layout
layout = dict(
    autosize=True,
    automargin=True,
    margin=dict(l=30, r=30, b=20, t=40),
    hovermode="closest",
    plot_bgcolor="#F9F9F9",
    paper_bgcolor="#F9F9F9",
    legend=dict(font=dict(size=10), orientation="h"),
    title="Evolución temporal",
)

# creating whole graph
main_fig = dict(data=data, layout=layout)

# Create app layout
app.layout = html.Div(
    [
        dcc.Store(id="aggregate_data"),
        # empty Div to trigger javascript file for graph resizing
        html.Div(id="output-clientside"),
        html.Div(
            [
                html.Div(
                    [
                        html.Img(
                            src=app.get_asset_url("rsz_covid_19_2-removebg-preview.png"),
                            id="covid-image",
                            style={
                                "height": "60px",
                                "width": "auto",
                                "margin-bottom": "25px",
                            },
                        )
                    ],
                    className="one-third column",
                ),
                html.Div(
                    [
                        html.Div(
                            [
                                html.H3(
                                    "COVID-19 en Chile",
                                    style={"margin-bottom": "0px"},
                                ),
                                html.H5(
                                    "Visualización", style={"margin-top": "0px"}
                                ),
                            ]
                        )
                    ],
                    className="one-half column",
                    id="title",
                ),
                html.Div(
                    [
                        html.A(
                            html.Button("Ayúdanos!", id="learn-more-button"),
                            href="https://github.com/YachayData/COVID-19",
                        )
                    ],
                    className="one-third column",
                    id="button",
                ),
            ],
            id="header",
            className="row flex-display",
            style={"margin-bottom": "25px"},
        ),
        html.Div(
            [
                html.Div(
                    [
                        html.Div([
                            html.H5('Detalle por región'),
                            html.P(f"Última actualización: {last_day}")
                        ]),
                        dash_table.DataTable(
                            id='table',
                            columns=[{"name": i, "id": i} for i in reg_latest_accum.columns],
                            data=reg_latest_accum.to_dict('records'),
                            style_data={'font-color': 'black'},
                            style_data_conditional=[{
                                "if": {"row_index": 16},
                                "fontWeight": "bold"
                            }
                            ],
                            style_cell={
                                'textAlign': 'center',
                                'font-weight': 400,
                                'font-family': 'Helvetica'
                            },
                            style_cell_conditional=[
                                {'if': {'column_id': 'Región'},
                                 'width': '40%'},
                                {'if': {'column_id': 'Contagiados'},
                                 'width': '20%'},
                                {'if': {'column_id': 'Fallecidos'},
                                 'width': '20%'},
                                {'if': {'column_id': 'Recuperados'},
                                 'width': '20%'},
                                {'if': {'row_index': 'odd'},
                                 'backgroundColor': 'rgb(248, 248, 248)'
                                 }
                            ],
                            style_header={'backgroundColor': '#b5b5b5'}
                        )
                    ],
                    className="pretty_container four columns",
                    id="cross-filter-options",
                ),
                html.Div(
                    [
                        html.Div(
                            [
                                html.Div(
                                    [html.H6(children=infected),
                                     html.P("Contagiados")],
                                    id="wells",
                                    className="mini_container",
                                ),
                                html.Div(
                                    [html.H6(children=deaths),
                                     html.P("Fallecidos")],
                                    id="gas",
                                    className="mini_container",
                                ),
                                html.Div(
                                    [html.H6(children=recovered),
                                     html.P("Recuperados")],
                                    id="oil",
                                    className="mini_container",
                                )
                            ],
                            id="info-container",
                            className="row container-display",
                        ),
                        html.Div(
                            [dcc.Graph(id="count_graph",
                                       figure=main_fig,
                                       config=dict(displayModeBar=True, displaylogo=False))],
                            id="countGraphContainer",
                            className="pretty_pie_container",
                        ),
                    ],
                    id="right-column",
                    className="eight columns",
                ),
            ],
            className="row flex-display",
        ),
        html.Div(
            [
                html.Div([
                    html.Div([
                        html.H5('Desglose por comuna'),
                        html.Div([
                            dcc.Dropdown(id='region_dropdown',
                                         options=region_opts,
                                         value=13,
                                         placeholder="Seleccione una región"),
                            dcc.Dropdown(id='town_dropdown',
                                         options=[],
                                         placeholder="Selecciona una comuna",
                                         style={'marginTop': '0.5%'})
                        ]),
                        html.P(id='town_last_info')
                    ]),
                    dcc.Graph(id="main_graph",
                              config={'displayModeBar': False})
                ],
                    className="pretty_container seven columns",
                ),
                html.Div(
                    [dcc.Graph(id="pie_graph",
                               config={'displayModeBar': False}),
                     html.P(id='pie_date',
                            style={'textAlign': 'center',
                                   'marginBottom': 10})],
                    className="pretty_container five columns",
                ),
            ],
            className="row flex-display",
        )
    ],
    id="mainContainer",
    style={"display": "flex", "flex-direction": "column"},
)

# Create callbacks
app.clientside_callback(
    ClientsideFunction(namespace="clientside", function_name="resize"),
    Output("output-clientside", "children"),
    [Input("count_graph", "figure")],
)


def create_series_by_name(source_data: dict, name: str, filter_criteria: str) -> Tuple[list, list]:
    """
    Iterates over some source of data to filter it. This method return two lists, the first one contains dates
    and the other the number of infected people. The filter criteria can be changed to the name of the column
    that wants to be used to search the coincidences. Remember that this method assumes a dictionary structure where
    the key is some date as string and the value some pandas dataframe.
    """
    dates = []
    infected_numbers = []
    for date_as_str, df in source_data.items():
        # this should return just one record
        sub_df = df[df[filter_criteria] == name]
        if len(sub_df) > 1:
            raise ValueError(f"Duplicated rows of data filtered by: {filter_criteria} = {name}.")
        try:
            infected_numbers.append(int(sub_df['casos_totales'].iloc[0]))
            dates.append(dt.strptime(date_as_str, '%Y-%m-%d'))
        except ValueError:
            continue
    return dates, infected_numbers


@app.callback(Output('town_dropdown', 'options'),
              [Input('region_dropdown', 'value')])
def update_town_dropdown(region_id):
    if region_id is None:
        raise PreventUpdate

    if region_id in town_names.keys():
        # filtering by
        return [{'label': town, 'value': town} for town in town_names[region_id]]
    return []


@app.callback(Output('town_last_info', 'children'),
              [Input('town_dropdown', 'value')])
def update_main_graph(town_id):
    if town_id is None:
        return ''

    last_town_df = town_stats[list(town_stats.keys())[-1]]
    sub_df = last_town_df[last_town_df['nombre_comuna'] == town_id]
    if sub_df is not None:
        population = int(sub_df['poblacion'].iloc[0])
        rate = sub_df['tasa'].iloc[0]
        return f'Población: {population} | Tasa: {rate}'


@app.callback([Output('pie_graph', 'figure'),
               Output('pie_date', 'children')],
              [Input('region_dropdown', 'value')])
def update_pie_graph(region_id):
    if region_id not in town_names.keys():
        raise ValueError("The selected region is not registered. Please add it into the town_names variable.")
    names = town_names[region_id]
    final_names = []
    values = []
    max_dates = []
    for name in names:
        dates, cases = create_series_by_name(town_stats, name, filter_criteria='nombre_comuna')
        if len(cases) == 0:
            continue
        values.append(cases[-1])
        final_names.append(name)
        max_dates.append(dates[-1])
    assert len(set(max_dates)) == 1, "The data is not consistent."
    fig_data = dict(
        type="pie",
        labels=final_names,
        values=values,
        hoverinfo='percent+label+value',
        textposition='inside'
    )

    pie_layout = dict(
        autosize=False,
        automargin=False,
        textinfo='percent',
        margin=dict(l=30, r=30, b=20, t=40),
        hovermode="closest",
        plot_bgcolor="#F9F9F9",
        paper_bgcolor="#F9F9F9",
        legend=dict(font=dict(size=10)),
        title="Distribución de contagiados por comuna",
    )
    return dict(data=[fig_data], layout=pie_layout), f"Actualizado: {max_dates[0]}"


@app.callback(Output('main_graph', 'figure'),
              [Input('region_dropdown', 'value'),
               Input('town_dropdown', 'value')])
def update_main_graph(region_id, town_id):
    if region_id is None and town_id is None:
        raise PreventUpdate

    layout_copy = layout.copy()
    fig = dict(data=[], layout=dict())
    dates = []
    cases = []

    # render region graph
    if region_id is not None and town_id is None:
        dates, cases = create_series_by_name(reg_stats, region_id, filter_criteria='id_reg')
        layout_copy['title'] = f'Evolución para la región: {region_ids[region_id]}'

    # render town graph
    if town_id is not None:
        dates, cases = create_series_by_name(town_stats, town_id, filter_criteria='nombre_comuna')
        layout_copy['title'] = f'Evolución para la comuna de {town_id}'

    fig_data = [dict(type="scatter",
                     mode="lines+markers",
                     name=segment,
                     x=dates,
                     y=cases,
                     line=dict(shape="spline", smoothing=1, width=1, color=colors[i]),
                     marker=dict(symbol="diamond-open"))]
    fig['data'] = fig_data
    fig['layout'] = layout_copy

    return fig


# Main
if __name__ == "__main__":
    app.server.run(debug=True, port=8080, threaded=True)
