import pathlib
import pandas as pd
from tqdm import tqdm
from datetime import datetime as dt
import glob


class DataLoader:

    REGION_IDS = {
        1: 'Tarapaca',
        2: 'Antofagasta',
        3: 'Atacama',
        4: 'Coquimbo',
        5: 'Valparaíso',
        6: 'Ohiggins',
        7: 'Maule',
        8: 'Biobio',
        9: 'Araucania',
        10: 'Los Lagos',
        11: 'Aysen',
        12: 'Magallanes',
        13: 'Metropolitana',
        14: 'Los Rios',
        15: 'Arica y Parinacota',
        16: 'Nuble'
    }

    def __init__(self):
        self.region_data = None
        self.__initialize_data()

    def __initialize_data(self):
        """
        Initialize the data stored in a specific folder.
        """

        # get relative data folder
        main_path = pathlib.Path(__file__).parent.parent.parent.parent
        region_data_path = main_path.joinpath("informes_minsal/informes_diarios_Region_CSV").resolve()
        town_data_path = main_path.joinpath("informes_minsal/informes_diarios_Comuna_CSV").resolve()

        # load the data for each region
        csv_data = {}
        for filename in tqdm(glob.glob(f'{region_data_path}/*.csv'), desc='Loading data from each region'):
            date = self._get_date_from_filename(filename)
            csv_data[date] = pd.read_csv(filename)
        self.region_data = csv_data

        # load the data for each region
        csv_data = {}
        for filename in tqdm(glob.glob(f'{town_data_path}/*.csv'), desc='Loading data from each town'):
            date = self._get_date_from_filename(filename)
            csv_data[date] = pd.read_csv(filename)
        self.town_data = csv_data

    @staticmethod
    def _get_date_from_filename(filename):
        """
        This method returns the date inferred from a string (filename).
        :param filename:                Filename as string.
        :return:                        Date as string.
        """
        filename = filename.split('\\')[-1]
        date_as_str = filename[:10]
        return date_as_str

    def get_country_stats(self):
        """
        Returns a dictionary with series of detailed and accumulated values of infected, death and
        recovered people in Chile.

        Example of result:
            {
                'contagiados':
                    {
                        'detailed': pd.Series(),
                        'accumulated: pd.Series()
                    },
                'fallecidos':
                    {
                        'detailed': pd.Series(),
                        'accumulated: pd.Series()
                    },
                'recuperados':
                    {
                        'detailed': pd.Series(),
                        'accumulated: pd.Series()
                    },
            }

        :return:
            A Dictionary
        """
        index = [dt.strptime(date, '%Y-%m-%d') for date in self.region_data.keys()]

        stats = {}
        for segment in ['casos', 'fallecidos', 'recuperados']:
            # getting accumulated values of infected cases
            accumulated_chile = [self.region_data[date][f'{segment}_totales'].sum() for date in self.region_data]
            accumulated_chile = pd.Series(index=index, data=accumulated_chile)

            # getting detailed values of infected cases
            detailed_chile = [self.region_data[date][f'{segment}_nuevos'].sum() for date in self.region_data]
            detailed_chile = pd.Series(index=index, data=detailed_chile)

            if segment == 'casos':
                segment = 'contagiados'

            stats[segment] = {'detailed': detailed_chile, 'accumulated': accumulated_chile}

        return stats

    def get_last_day(self):
        """
        Returns the day, and data of infected, death and recuperated people associated with the latest update.
        :return:                A Tuple.
                                    1) Date (String).
                                    2) DataFrame.
        """
        last_day = list(self.region_data.keys())[-1]
        df = self.region_data[last_day]
        return last_day, df

    def get_country_data(self) -> dict:
        return self.region_data

    def get_region_data(self) -> dict:
        return self.town_data


if __name__ == '__main__':
    d = DataLoader()
    last_day, last_df = d.get_last_day()
    stats = d.get_country_stats()
    infected = stats['contagiados']['accumulated'][stats['contagiados']['accumulated'].last_valid_index()]
    town = d.get_region_data()
    print("")
