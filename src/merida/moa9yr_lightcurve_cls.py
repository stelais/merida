import pandas as pd
import numpy as np


class MOA9yearLightcurve:
    """
      A class for using the light curves downloaded from NExSci platform . You can easily get flux and magnitude
      you need name, and path to the lightcurve
      you can adjust other params like the extension if not phot.cor.feather
    """

    def __init__(self, lightcurve_name_, data_folder_with_field_, *, extension_='.feather'):
        self.lightcurve_name = lightcurve_name_
        self.field = lightcurve_name_.split('-')[0]
        self.band = lightcurve_name_.split('-')[1]
        self.chip = lightcurve_name_.split('-')[2]
        self.subframe = lightcurve_name_.split('-')[3]
        self.id = lightcurve_name_.split('-')[4]
        self.main_data_path = data_folder_with_field_
        self.extension = extension_
        self.lightcurve_path = self.main_data_path + self.lightcurve_name + self.extension
        if self.extension == '.feather':
            self.lightcurve_dataframe = pd.read_feather(self.lightcurve_path)
        elif self.extension == '.csv':
            self.lightcurve_dataframe = pd.read_csv(self.lightcurve_path)
        else:
            raise ValueError('Only .feather and .csv extensions are supported')

    def get_days_fluxes_errors(self):
        """
        Get the days, fluxes, corrected flux, and fluxes errors from the lightcurve data frame
        :return:
        """
        return (self.lightcurve_dataframe['HJD'], self.lightcurve_dataframe['flux'],
                self.lightcurve_dataframe['cor_flux'], self.lightcurve_dataframe['flux_err'])

    def get_days_magnitudes_errors(self, *, fudge_factor=1.0, offset_alternative=False):
        """
        Get the days, magnitudes, corrected magnitudes, magnitudes erros and corrected magnitudes errors
        from the lightcurve data frame
        :return:
        """
        self.flux_to_mag(fudge_factor=fudge_factor, offset_alternative=offset_alternative)
        return (self.lightcurve_dataframe['HJD'], self.lightcurve_dataframe['magnitudes'],
                self.lightcurve_dataframe['cor_magnitudes'], self.lightcurve_dataframe['magnitudes_err'],
                self.lightcurve_dataframe['cor_magnitudes_err'])

    def flux_to_mag(self, *, fudge_factor=1.0, offset_alternative=False):
        """
        The flux taking into account that flux cannot be negative AND taking in consideration the fudge factor!
        :param offset_alternative:
        :param fudge_factor:
        :return:
        """
        # [1.1 x  (-1) x smallest_negative_flux_value]
        # self.lightcurve_dataframe['offset_fluxes'] = self.lightcurve_dataframe['fluxes'] - np.min(self.lightcurve_dataframe['fluxes'])
        self.lightcurve_dataframe['offset_flux'] = self.lightcurve_dataframe['flux'] + 1.1 * (-1) * np.min(
            self.lightcurve_dataframe['flux'])
        self.lightcurve_dataframe['offset_cor_flux'] = self.lightcurve_dataframe['cor_flux'] + 1.1 * (-1) * np.min(
            self.lightcurve_dataframe['cor_flux'])
        self.lightcurve_dataframe['fudge_flux_err'] = self.lightcurve_dataframe['flux_err'] * fudge_factor

        if offset_alternative:
            self.lightcurve_dataframe['offset_flux'] = self.lightcurve_dataframe['flux'] + 1.0 * (-1) * np.min(
                self.lightcurve_dataframe['flux']) + 1e-5
            self.lightcurve_dataframe['offset_cor_flux'] = self.lightcurve_dataframe['cor_flux'] + 1.0 * (-1) * np.min(
                self.lightcurve_dataframe['cor_flux']) + 1e-5
            self.lightcurve_dataframe['fudge_flux_err'] = self.lightcurve_dataframe['flux_err'] * fudge_factor

        magnitudes, magnitudes_err = flux_to_magnitude_zero_point(self.lightcurve_dataframe['offset_flux'],
                                                                  self.lightcurve_dataframe['fudge_flux_err'],
                                                                  zero_point_=21.0)

        cor_magnitudes, cor_magnitudes_err = flux_to_magnitude_zero_point(self.lightcurve_dataframe['offset_cor_flux'],
                                                                          self.lightcurve_dataframe['fudge_flux_err'],
                                                                          zero_point_=21.0)

        self.lightcurve_dataframe['magnitudes'] = magnitudes
        self.lightcurve_dataframe['magnitudes_err'] = magnitudes_err

        self.lightcurve_dataframe['cor_magnitudes'] = cor_magnitudes
        self.lightcurve_dataframe['cor_magnitudes_err'] = cor_magnitudes_err

        return self.lightcurve_dataframe


def flux_to_magnitude_zero_point(flux_, flux_err_, zero_point_=0.0):
    """
    Converting Flux to magnitude considering zero_point
    :param flux_err_:
    :param flux_:
    :param zero_point_:
    :return:
    """
    magnitude = zero_point_ - 2.5 * np.log10(flux_)
    magnitude_err = (2.5 / np.log(10)) * (flux_err_ / flux_)
    return magnitude, magnitude_err