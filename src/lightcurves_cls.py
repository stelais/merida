import pandas as pd
import requests
from bs4 import BeautifulSoup


class LightCurvesURL:
    """
        A class for loading light curves into the bokeh server using a URL
    """

    def __init__(self, lightcurve_name_, lightcurve_class_):
        self.lightcurve_name = lightcurve_name_
        self.lightcurve_class = lightcurve_class_
        self.lightcurve_extended_name = lightcurve_name_.split('-')[0] + '/' + lightcurve_name_.split('-')[1] + '/' + \
                                        lightcurve_name_.split('-')[2] + '/' + lightcurve_name_
        self.extension = '.ipac'
        self.url_main_path = 'https://exoplanetarchive.ipac.caltech.edu/workspace/TMP_mjAAoX_30027/MOA/tab1/data/'
        self.lightcurve_url_path = self.url_main_path + self.lightcurve_extended_name + self.extension
        url = self.lightcurve_url_path
        column_names = ['HJD', 'flux', 'cor_flux', 'flux_err', 'obsID', 'JD', 'fwhm', 'sky', 'airmass', 'nstar',
                        'scale',
                        'exptime', 'skydiff', 'chisq', 'npix', 'airmass1', 'ang1', 'included']
        colspecs = [(0, 12), (12, 27), (27, 41), (41, 55), (55, 61), (61, 73), (73, 81), (81, 89), (89, 97), (97, 103),
                    (103, 112),
                    (112, 120), (120, 130), (130, 141), (141, 146), (146, 154), (154, 163), (163, 172)]
        self.lightcurve_dataframe = pd.read_fwf(url, header=3, names=column_names, colspecs=colspecs)

    def get_days_fluxes_errors(self):
        """
        Get the days, fluxes, and fluxes errors from the lightcurve data frame
        :return:
        """
        return self.lightcurve_dataframe['HJD'], self.lightcurve_dataframe['flux'], self.lightcurve_dataframe[
            'flux_err']

    def save_lightcurve_from_url_as_csv(self, path_to_save):
        """
        Saves the lightcurve as a csv file
        :param path_to_save:
        :return:
        """
        self.lightcurve_dataframe.to_csv(path_to_save + self.lightcurve_name + '.csv', index=False)

    def save_lightcurve_from_url_as_feather(self, path_to_save):
        """
        Saves the lightcurve as a feather file
        :param path_to_save:
        :return:
        """
        self.lightcurve_dataframe.to_feather(path_to_save + self.lightcurve_name + '.feather')


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
