import pandas as pd
import requests


class LightCurvesURL:
    """
        A class for loading light curves into the bokeh server using a URL
    """
    def __init__(self, lightcurve_name_, lightcurve_class_):
        self.lightcurve_name = lightcurve_name_
        self.lightcurve_class = lightcurve_class_

    def get_data_from_url(self) -> pd.DataFrame:
        """
            Loads the events data from NExSci website
            :return: The data frame of the events.
        """
        url = 'https://exoplanetarchive.ipac.caltech.edu' + self.lightcurve_name
        page = requests.get(url)
        # soup = BeautifulSoup(page.content, 'lxml')
        # tbl = soup.find("table")
        # events_data_frame = pd.read_html(str(tbl))[0]
        # events_data_frame[['field', 'clr', 'chip', 'subfield', 'id']] = events_data_frame['MOA INTERNAL ID'].str.split(
        #     '-', 4, expand=True)
        # events_data_frame['chip'] = events_data_frame['chip'].astype(int)
        # events_data_frame['subfield'] = events_data_frame['subfield'].astype(int)
        # events_data_frame['id'] = events_data_frame['id'].astype(int)
        # events_data_frame = events_data_frame.set_index(['field', 'clr', 'chip', 'subfield', 'id'], drop=False)
        # events_data_frame = events_data_frame.sort_index()
        # return events_data_frame
        return None


class LightCurvesLocal:
    """
      A class for loading light curves into the bokeh server
      you need name, class, and path
      you can adjust other params like the extension if not phot.cor.feather
    """

    def __init__(self, lightcurve_name_, lightcurve_class_, data_path_):
        self.lightcurve_name = lightcurve_name_
        self.lightcurve_extended_name = lightcurve_name_.split('-')[0] + '_' + lightcurve_name_.split('-')[1] + '_' + \
                                        lightcurve_name_.split('-')[2] + '_' + lightcurve_name_
        self.lightcurve_class = lightcurve_class_
        self.main_data_path = data_path_
        self.extension = '.phot.cor.feather'
        self.lightcurve_path = self.main_data_path + '/' + self.lightcurve_extended_name \
                               + self.extension
        self.lightcurve_dataframe = pd.read_feather(self.lightcurve_path)

    def get_days_fluxes_errors(self):
        """
        Get the days, fluxes, and fluxes errors from the lightcurve data frame
        :return:
        """
        return self.lightcurve_dataframe['HJD'], self.lightcurve_dataframe['flux'], self.lightcurve_dataframe[
            'flux_err']
