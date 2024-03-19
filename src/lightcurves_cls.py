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
        self.lightcurve_dataframe.to_feather(path_to_save + self.lightcurve_name + '.feather')

class LightCurvesNExSciLocalCSV:
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


class LightCurvesNExSciLocalFeather:
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
        self.extension = '.feather'
        self.lightcurve_path = self.main_data_path + '/' + self.lightcurve_name + self.extension
        self.lightcurve_dataframe = pd.read_feather(self.lightcurve_path)

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

class Metadata:
    """
    A class for loading the light curves metadata (the two pieces)
    ['field', 'chip', 'subframe', 'id', 'tag', 'x', 'y', 'ra_j2000',
    'dec_j2000', 'number_of_data_points', 'number_of_frames_object_is_detected',
    'max_significance', 'sum_of_continuous_significance', 'chi_squared_outside_search_window',
    'dophot_object_reference_image_separation', 'dophot_id', 'dophot_type', 'dophot_magnitude',
    'dophot_magnitude_error', 'pspl_t0', 'pspl_tE', 'pspl_u0', 'pspl_source_flux', 'pspl_blending_flux',
    'pspl_t0_parabolic_error', 'pspl_tE_parabolic_error', 'pspl_tE_error_lower_limit', 'pspl_tE_error_upper_limit',
    'pspl_u0_parabolic_error', 'pspl_u0_error_lower_limit', 'pspl_u0_error_upper_limit', 'pspl_source_flux_error',
    'pspl_blending_flux_error', 'pspl_chi_squared', 'fspl_t0', 'fspl_tE', 'fspl_u0', 'fspl_rho', 'fspl_source_flux',
    'fspl_blending_flux', 'fspl_t0_parabolic_error', 'fspl_tE_parabolic_error', 'fspl_tE_error_lower_limit',
    'fspl_tE_error_upper_limit', 'fspl_u0_parabolic_error', 'fspl_u0_error_lower_limit', 'fspl_u0_error_upper_limit',
    'fspl_rho_parabolic_error', 'fspl_rho_error_lower_limit', 'fspl_rho_error_upper_limit', 'fspl_source_flux_error',
    'fspl_blending_flux_error', 'fspl_chi_squared', 'separation_to_alert_position1', 'alert_id1', 'alert_x1',
    'alert_y1', 'separation_to_alert_position2', 'alert_id2', 'alert_x2', 'alert_y2', 'ROW_IDX', 'ROW_NUM',
    'lightcurve_name']
    """

    def __init__(self):
        self.path1 = 'data/metadata_1of2.feather'
        self.path2 = 'data/metadata_2of2.feather'
        self.dataframe1 = pd.read_feather(self.path1)
        self.dataframe2 = pd.read_feather(self.path2)
        self.dataframe = pd.concat([self.dataframe1, self.dataframe2], ignore_index=True)

    def get_one_metadata_csv_file(self):
        self.dataframe.to_csv('data/metadata_test.csv', index=False)



class MetadataLocal:
    """
    A class for loading the light curves metadata Local an entire piece.
    ['field', 'chip', 'subframe', 'id', 'tag', 'x', 'y', 'ra_j2000',
    'dec_j2000', 'number_of_data_points', 'number_of_frames_object_is_detected',
    'max_significance', 'sum_of_continuous_significance', 'chi_squared_outside_search_window',
    'dophot_object_reference_image_separation', 'dophot_id', 'dophot_type', 'dophot_magnitude',
    'dophot_magnitude_error', 'pspl_t0', 'pspl_tE', 'pspl_u0', 'pspl_source_flux', 'pspl_blending_flux',
    'pspl_t0_parabolic_error', 'pspl_tE_parabolic_error', 'pspl_tE_error_lower_limit', 'pspl_tE_error_upper_limit',
    'pspl_u0_parabolic_error', 'pspl_u0_error_lower_limit', 'pspl_u0_error_upper_limit', 'pspl_source_flux_error',
    'pspl_blending_flux_error', 'pspl_chi_squared', 'fspl_t0', 'fspl_tE', 'fspl_u0', 'fspl_rho', 'fspl_source_flux',
    'fspl_blending_flux', 'fspl_t0_parabolic_error', 'fspl_tE_parabolic_error', 'fspl_tE_error_lower_limit',
    'fspl_tE_error_upper_limit', 'fspl_u0_parabolic_error', 'fspl_u0_error_lower_limit', 'fspl_u0_error_upper_limit',
    'fspl_rho_parabolic_error', 'fspl_rho_error_lower_limit', 'fspl_rho_error_upper_limit', 'fspl_source_flux_error',
    'fspl_blending_flux_error', 'fspl_chi_squared', 'separation_to_alert_position1', 'alert_id1', 'alert_x1',
    'alert_y1', 'separation_to_alert_position2', 'alert_id2', 'alert_x2', 'alert_y2', 'ROW_IDX', 'ROW_NUM',
    'lightcurve_name']
    """

    def __init__(self):
        self.path = 'data/metadata.csv'
        self.dataframe = pd.read_csv(self.path, float_precision='round_trip')