from src.DataLoader import DataLoader
import dash
import dash_table
import pandas as pd


dataLoader = DataLoader()
stats = dataLoader.get_country_stats()
day, df = dataLoader.get_last_day()
region_ids = dataLoader.REGION_IDS


def process_daily_df(raw_df: pd.DataFrame) -> pd.DataFrame:
    raw_df = raw_df.copy(deep=True)
    raw_df.sort_values(by='id_reg', inplace=True)
    raw_df.rename(columns={
        'nombre_reg': 'Región',
        'casos_totales': 'Casos',
        'fallecidos_totales': 'Fallecidos',
        'recuperados_totales': 'Recuperados'
    }, inplace=True)
    raw_df.drop(columns=['casos_nuevos', 'fallecidos_nuevos', 'recuperados_nuevos', 'id_reg'],
                inplace=True)
    return raw_df


df = process_daily_df(df)
app = dash.Dash(__name__)

app.layout = dash_table.DataTable(
    id='table',
    columns=[{"name": i, "id": i} for i in df.columns],
    data=df.to_dict('records'),
)

if __name__ == '__main__':
    app.run_server(debug=True)