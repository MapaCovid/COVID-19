# Import required libraries
import pickle
import copy
import pathlib
import dash
import math
import datetime as dt
import pandas as pd
from dash.dependencies import Input, Output, State, ClientsideFunction
import dash_core_components as dcc
import dash_html_components as html
from dash.exceptions import PreventUpdate
from src.DataLoader import DataLoader
import dash_table

# Multi-dropdown options
from controls import COUNTIES, WELL_STATUSES, WELL_TYPES, WELL_COLORS

# get relative data folder
PATH = pathlib.Path(__file__).parent
DATA_PATH = PATH.joinpath("data").resolve()

app = dash.Dash(__name__, meta_tags=[{"name": "viewport", "content": "width=device-width"}])
app.scripts.config.serve_locally = True
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
region_stats = dataLoader.get_country_stats()
last_day, last_df = dataLoader.get_last_day()
reg_accum = process_daily_df(last_df)
region_opts = [{'label': region_ids[region_id], 'value': region_id} for region_id in region_ids.keys()]

# town data
town_stats = dataLoader.get_region_data()
town_names = process_town_names_by_region(town_stats[list(town_stats.keys())[0]])

# accessing
infected = region_stats['contagiados']['accumulated'][region_stats['contagiados']['accumulated'].last_valid_index()]
deaths = region_stats['fallecidos']['accumulated'][region_stats['fallecidos']['accumulated'].last_valid_index()]
recovered = region_stats['recuperados']['accumulated'][region_stats['recuperados']['accumulated'].last_valid_index()]

# creating main graph data
colors = ["#fac1b7", "#a9bb95", "#92d8d8"]
data = []
for i, segment in enumerate(['contagiados', 'fallecidos', 'recuperados']):
    data.append(dict(type="scatter",
                     mode="lines+markers",
                     name=segment,
                     x=region_stats[segment]['accumulated'].index,
                     y=region_stats[segment]['accumulated'],
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
                            columns=[{"name": i, "id": i} for i in reg_accum.columns],
                            data=reg_accum.to_dict('records'),
                            style_data={'font-color': 'black'},
                            style_cell={
                                'textAlign': 'center',
                                'font-weight': 400,
                                'font-family': 'Open Sans'
                            },
                            style_cell_conditional=[
                                    {'if': {'column_id': 'Región'},
                                     'width': '40%'},
                                    {'if': {'column_id': 'Contagiados'},
                                     'width': '20%'},
                                    {'if': {'column_id': 'Fallecidos'},
                                     'width': '20%'},
                                    {'if': {'column_id': 'Recuperados'},
                                     'width': '20%'}
                                ]
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
                            className="pretty_container",
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
                                         value=1,
                                         placeholder="Seleccione una región"),
                            dcc.Dropdown(id='town_dropdown',
                                         options=[],
                                         placeholder="Selecciona una comuna",
                                         style={'marginTop': '0.5%'})
                        ]),
                        html.P(id='town_last_info')
                    ]),
                    dcc.Graph(id="main_graph")
                     ],
                    className="pretty_container seven columns",
                ),
                html.Div(
                    [dcc.Graph(id="individual_graph")],
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
        raise PreventUpdate

    last_town_df = town_stats[list(town_stats.keys())[-1]]
    sub_df = last_town_df[last_town_df['nombre_comuna'] == town_id]
    if sub_df is not None:
        population = int(sub_df['poblacion'].iloc[0])
        rate = sub_df['tasa'].iloc[0]
        return f'Población: {population} | Tasa: {rate}'
    return ''


@app.callback(Output('main_graph', 'figure'),
              [Input('region_dropdown', 'value'),
               Input('town_dropdown', 'value')])
def update_main_graph(region_id, town_id):
    if region_id is None and town_id is None:
        raise PreventUpdate

    # render region graph
    if region_id is not None and town_id is None:
        pass

    # render town graph
    if town_id is not None:
        pass

    return dict(data=[], layout=dict())


# Main
if __name__ == "__main__":
    app.server.run(debug=True, port=8080, threaded=True)