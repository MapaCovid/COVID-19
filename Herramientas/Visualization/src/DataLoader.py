import pathlib
import pandas as pd
from tqdm import tqdm
from datetime import datetime as dt
import glob


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


class DataLoader:

    def __init__(self):
        self.data = None
        self.__initialize_data()

    def __initialize_data(self):
        """
        Initialize the data stored in a specific folder.
        """

        # get relative data folder
        PATH = pathlib.Path(__file__).parent.parent.parent.parent
        DATA_PATH = PATH.joinpath("informes_minsal/informes_diarios_Region_CSV").resolve()
        csv_filenames = glob.glob(f'{DATA_PATH}/*.csv')

        # load the data
        csv_data = {}
        for filename in tqdm(csv_filenames, desc='Loading data'):
            date = self._get_date_from_filename(filename)
            csv_data[date] = pd.read_csv(filename)
        self.data = csv_data

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
                'casos':
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
        index = [dt.strptime(date, '%Y-%m-%d') for date in self.data.keys()]

        stats = {}
        for segment in ['casos', 'fallecidos', 'recuperados']:
            # getting accumulated values of infected cases
            accumulated_chile = [self.data[date][f'{segment}_totales'].sum() for date in self.data]
            accumulated_chile = pd.Series(index=index, data=accumulated_chile)

            # getting detailed values of infected cases
            detailed_chile = [self.data[date][f'{segment}_nuevos'].sum() for date in self.data]
            detailed_chile = pd.Series(index=index, data=detailed_chile)

            stats[segment] = {'detailed': detailed_chile, 'accumulated': accumulated_chile}

        return stats

    def get_region_stats(self):
        pass


if __name__ == '__main__':
    d = DataLoader()
    stats = d.get_country_stats()
