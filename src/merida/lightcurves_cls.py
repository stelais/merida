import re
import shutil
import urllib.request
from pathlib import Path

import astropy.io.ascii
import pandas as pd
import numpy as np
import requests
from bs4 import BeautifulSoup


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
        self.url_main_path = self.get_workspace_url()
        self.lightcurve_url_path = self.url_main_path + self.lightcurve_extended_name + self.extension
        url = self.lightcurve_url_path
        print(url)
        column_names = ['HJD', 'flux', 'cor_flux', 'flux_err', 'obsID', 'JD', 'fwhm', 'sky', 'airmass', 'nstar',
                        'scale',
                        'exptime', 'skydiff', 'chisq', 'npix', 'airmass1', 'ang1', 'included']
        self.lightcurve_dataframe = pd.read_csv(url, header=3, names=column_names, delimiter=r"\s+", index_col=False)

    @staticmethod
    def get_workspace_url() -> str:
        """
        Connects to the MOA archive site to get a workspace URL.
        :return: The workspace URL.
        """
        url = 'https://exoplanetarchive.ipac.caltech.edu/cgi-bin/MOA/nph-firefly?MOA'
        headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/'
                                 '537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36'}
        response = requests.get(url, headers=headers)
        soup = BeautifulSoup(response.content, 'html.parser')
        body_tag = soup.body
        onload_string = body_tag.attrs['onload']
        workspace_pattern = r'TMP_\w+'
        match = re.search(workspace_pattern, onload_string)
        workspace_string = match.group()
        return f'https://exoplanetarchive.ipac.caltech.edu/workspace/{workspace_string}/MOA/tab1/data/'

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
        self.lightcurve_path = self.main_data_path + self.lightcurve_name + self.extension
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
        self.lightcurve_path = self.main_data_path + self.lightcurve_name + self.extension
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
        self.lightcurve_path = self.main_data_path + self.lightcurve_extended_name \
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


class SuperComputerLightCurves:
    """
      A class for loading light curves into the bokeh server the way it's saved in the supercomputer
      you need name, class, and path
      you can adjust other params like the extension if not phot.cor.feather
    """

    def __init__(self, lightcurve_name_, data_path_):
        self.lightcurve_name = lightcurve_name_
        self.field = lightcurve_name_.split('-')[0]
        self.band = lightcurve_name_.split('-')[1]
        self.chip = lightcurve_name_.split('-')[2]
        self.subframe = lightcurve_name_.split('-')[3]
        self.id = lightcurve_name_.split('-')[4]
        self.main_data_path = data_path_
        self.extension = '.feather'
        self.lightcurve_path = (self.main_data_path + '/'
                                + self.field + '/'
                                + self.lightcurve_name + self.extension)
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

    def __init__(self, path_to_metadata: Path = Path('data/metadata.feather')):
        if not path_to_metadata.exists():
            print(f'Metadata not found at `{path_to_metadata}`. Downloading and converting...')
            self.download_metadata(path_to_metadata)
            print(f'Metadata download and conversion complete.')
        self.dataframe = pd.read_feather(path_to_metadata)

    def get_one_metadata_csv_file(self):
        self.dataframe.to_csv('data/metadata_test.csv', index=False)

    @staticmethod
    def download_metadata(path_to_metadata: Path = Path('data/metadata.feather')) -> None:
        """
        Downloads the metadata for the MOA 9-year dataset.

        :param path_to_metadata: The path to the metadata.
        """
        metadata_url = 'https://exoplanetarchive.ipac.caltech.edu/data/Contributed/MOA/bulk/metadata.ipac.tar.gz'
        data_directory = path_to_metadata.parent
        data_directory.mkdir(parents=True, exist_ok=True)
        gz_path = data_directory.joinpath('metadata.ipac.tar.gz')
        ipac_path = data_directory.joinpath('metadata.ipac')
        if gz_path.exists():
            gz_path.unlink()
        if ipac_path.exists():
            ipac_path.unlink()
        if path_to_metadata.exists():
            path_to_metadata.unlink()
        with urllib.request.urlopen(metadata_url) as response, gz_path.open('wb') as gz_file:
            shutil.copyfileobj(response, gz_file)
        shutil.unpack_archive(gz_path, data_directory)
        astropy_table = astropy.io.ascii.read(ipac_path)
        data_frame = astropy_table.to_pandas()

        def metadata_row_to_light_curve_name(metadata_row: pd.Series) -> str:
            return f'gb{metadata_row["field"]}-R-{metadata_row["chip"]}-{metadata_row["subframe"]}-{metadata_row["id"]}'

        data_frame['lightcurve_name'] = data_frame.apply(metadata_row_to_light_curve_name, axis=1)
        data_frame.to_feather(path_to_metadata)
        gz_path.unlink()
        ipac_path.unlink()


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
