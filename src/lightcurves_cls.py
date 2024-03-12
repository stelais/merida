import pandas as pd
import numpy as np

class LightCurvesNExSciURL:
    """
        A class for loading a single light curve into the bokeh server using a URL
    """

    def __init__(self, lightcurve_name_, lightcurve_class_):
        self.lightcurve_name = lightcurve_name_
        self.lightcurve_class = lightcurve_class_
        self.field = lightcurve_name_.split('-')[0]
        self.band = lightcurve_name_.split('-')[1]
        self.chip = lightcurve_name_.split('-')[2]
        self.subframe = lightcurve_name_.split('-')[3]
        self.id = lightcurve_name_.split('-')[4]
        self.lightcurve_extended_name = self.field + '/' + self.band + '/' + self.chip + '/' + lightcurve_name_
        self.extension = '.ipac'
        self.url_main_path = 'https://exoplanetarchive.ipac.caltech.edu/workspace/TMP_dk5Wxv_13874/MOA/tab1/data/'
        self.lightcurve_url_path = self.url_main_path + self.lightcurve_extended_name + self.extension
        url = self.lightcurve_url_path
        print(url)
        column_names = ['HJD', 'flux', 'cor_flux', 'flux_err', 'obsID', 'JD', 'fwhm', 'sky', 'airmass', 'nstar',
                        'scale',
                        'exptime', 'skydiff', 'chisq', 'npix', 'airmass1', 'ang1', 'included']
        self.lightcurve_dataframe = pd.read_csv(url, header=3, names=column_names, delimiter=r"\s+", index_col=False)


    def get_days_fluxes_errors(self):
        """
        Get the days, fluxes, and fluxes errors from the lightcurve data frame
        :return:
        """
        return (self.lightcurve_dataframe['HJD'], self.lightcurve_dataframe['flux'],
                self.lightcurve_dataframe['cor_flux'], self.lightcurve_dataframe['flux_err'])

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
        self.lightcurve_dataframe.to_feather(path_to_save + self.lightcurve_name + '.feather', index=False)

class LightCurvesNExSciLocal:
    """
      A class for loading light curves downloaded from NExSci platform
      you need name, class, and path
      you can adjust other params like the extension if not phot.cor.feather
    """

    def __init__(self, lightcurve_name_, lightcurve_class_, data_path_):
        self.lightcurve_name = lightcurve_name_
        self.field = lightcurve_name_.split('-')[0]
        self.band = lightcurve_name_.split('-')[1]
        self.chip = lightcurve_name_.split('-')[2]
        self.subframe = lightcurve_name_.split('-')[3]
        self.id = lightcurve_name_.split('-')[4]
        self.lightcurve_extended_name = self.field + '/' + self.band + '/' + self.chip + '/' + lightcurve_name_
        self.lightcurve_class = lightcurve_class_
        self.main_data_path = data_path_
        self.extension = '.csv'
        self.lightcurve_path = self.main_data_path + '/' + self.lightcurve_name + self.extension
        self.lightcurve_dataframe = pd.read_csv(self.lightcurve_path)

    def get_days_fluxes_errors(self):
        """
        Get the days, fluxes, and fluxes errors from the lightcurve data frame
        :return:
        """
        return (self.lightcurve_dataframe['HJD'], self.lightcurve_dataframe['flux'],
                self.lightcurve_dataframe['cor_flux'], self.lightcurve_dataframe['flux_err'])



class OldLightCurvesFuguLocal:
    """
      A class for loading light curves into the bokeh server the way it's saved in fugu
      you need name, class, and path
      you can adjust other params like the extension if not phot.cor.feather
    """

    def __init__(self, lightcurve_name_, lightcurve_class_, data_path_):
        self.lightcurve_name = lightcurve_name_
        self.field = lightcurve_name_.split('-')[0]
        self.band = lightcurve_name_.split('-')[1]
        self.chip = lightcurve_name_.split('-')[2]
        self.subframe = lightcurve_name_.split('-')[3]
        self.id = lightcurve_name_.split('-')[4]
        self.lightcurve_extended_name = self.field + '_' + self.band + '_' + self.chip + '_' + lightcurve_name_
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
        return (self.lightcurve_dataframe['HJD'], self.lightcurve_dataframe['flux'],
                np.full(shape=len(self.lightcurve_dataframe['HJD']), fill_value=np.nan),
                self.lightcurve_dataframe['flux_err'])



class LightCurveMetadata:
    """
    A class for loading light curves metadata
    """

    def __init__(self, lightcurve_name_, lightcurve_class_):
        # TODO working here
        self.lightcurve_name = lightcurve_name_
        self.field = lightcurve_name_.split('-')[0]
        self.band = lightcurve_name_.split('-')[1]
        self.chip = lightcurve_name_.split('-')[2]
        self.subframe = lightcurve_name_.split('-')[3]
        self.id = lightcurve_name_.split('-')[4]
        self.lightcurve_class = lightcurve_class_

        metadata_url = 'https://exoplanetarchive.ipac.caltech.edu/workspace/TMP_mjAAoX_30027/MOA/tab1/data/metadata.ipac'

