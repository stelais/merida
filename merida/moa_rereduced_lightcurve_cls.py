import pandas as pd
from merida.zones_for_lightcurves import plotter
from bokeh.io import save, output_file
from bokeh.models import Range1d


class MOAReReducedLightcurve:
    """
      A class for loading/reading "si" light curves downloaded from Ian's personal page
      you need number, and path to the folder hosting the lightcurve
    """

    def __init__(self, lightcurve_number_, data_folder_, master_file_path_=None):
        self.lightcurve_number_ = lightcurve_number_
        self.name_prefix = f'si{lightcurve_number_:02}'
        self.lightcurve_name = f'{self.name_prefix}-MOA2R-10000.phot.dat'
        self.lightcurve_path = data_folder_ + self.lightcurve_name
        column_names = ['HJD', 'flux', 'flux_err', 'observation_id', 'magnitude', 'magnitude_err',
                        'fwhm', 'background', 'photometric_scale', 'JD']
        self.lightcurve_dataframe = pd.read_table(self.lightcurve_path,
                                                  delim_whitespace=True, names=column_names, header=None)
        self.lightcurve_dataframe['new_HJD'] = self.lightcurve_dataframe['HJD'] - 2450000.0
        self.master_file_path = master_file_path_
        if self.master_file_path is not None:
            self.master_dataframe = reading_master_file(self.master_file_path)
            self.master_row = self.master_dataframe[self.master_dataframe['name_prefix'] == self.name_prefix]

    def get_days_fluxes_errors(self):
        """
        Get the days, fluxes, and fluxes errors from the lightcurve data frame
        :return:
        """
        return (self.lightcurve_dataframe['new_HJD'], self.lightcurve_dataframe['flux'],
                self.lightcurve_dataframe['flux_err'])

    def get_days_magnitudes_errors(self):
        """
        Get the days, magnitudes and magnitudes errors from the lightcurve data frame
        :return:
        """
        lightcurve_dropped = self.lightcurve_dataframe[self.lightcurve_dataframe['magnitude'] != 99.99]
        return (lightcurve_dropped['new_HJD'], lightcurve_dropped['magnitude'],
                lightcurve_dropped['magnitude_err'])

    def quick_flux_plot(self, output_folder_=None):
        """
        Quick plot of the lightcurve
        :return:
        """
        if self.master_file_path is None:
            print("Master file path is not set. Please set it before calling this method.")
            peak_day = input("Alternatively, type the day peak... (- 2450000.0) and press Enter")
        else:
            # Get the peak day from the master file
            peak_day = self.master_row['approximate_peak'].values[0]
        plot, widget_inputs = plotter(self, height_and_width_=(325, 900), high_mag_plotting_=False,
                                      starting_and_ending_days_1_=None,
                                      starting_and_ending_days_2_=None, starting_and_ending_days_3_=None,
                                      if_cor_flux=False)
        plot.xaxis.axis_label = 'Days'
        plot.yaxis.axis_label = 'Flux'
        plot.x_range = Range1d(peak_day - 300, peak_day + 300)
        output_file(f"{output_folder_}{self.lightcurve_name}_flux.html")
        save(plot)

    def quick_magnitude_plot(self, output_folder_=None):
        """
        Quick plot of the lightcurve for magnitude
        :return:
        """
        if self.master_file_path is None:
            print("Master file path is not set. Please set it before calling this method.")
            peak_day = input("Alternatively, type the day peak... (- 2450000.0) and press Enter")
        else:
            # Get the peak day from the master file
            peak_day = self.master_row['approximate_peak'].values[0]
        plot, widget_inputs = plotter(self, height_and_width_=(325, 900), high_mag_plotting_=False,
                                      starting_and_ending_days_1_=None,
                                      starting_and_ending_days_2_=None, starting_and_ending_days_3_=None,
                                      if_cor_flux=False, if_mag=True)
        plot.xaxis.axis_label = 'Days'
        plot.yaxis.axis_label = 'Magnitude'
        plot.x_range = Range1d(peak_day - 30, peak_day + 30)
        plot.y_range.flipped = True
        output_file(f"{output_folder_}{self.lightcurve_name}_mag.html")
        save(plot)


def reading_master_file(master_file_path):
    """
    Read the master file and return a dataframe
    :param master_file_path:
    :return:
    """
    column_master_names = ['name_prefix', 'taka_lightcurve_name',
                           'RA', 'DEC',
                           'x_pixel', 'y_pixel',  # SIS: I'm not sure about these columns
                           'approximate_peak',
                           'priority_coefficient']
    master_dataframe = pd.read_table(master_file_path, names=column_master_names,
                                     header=None, delim_whitespace=True)
    return master_dataframe


if __name__ == '__main__':
    # Example usage of the MOAReReducedLightcurve class:
    for lightcurve_number in range(1, 10):
        if lightcurve_number == 4 or lightcurve_number == 8:
            continue
        # path of the folder with the Ian's lightcurves
        data_folder = '/Users/stela/Documents/Scripts/ai_microlensing/merida/data/lightcurves_from_ian/'
        lightcurve = MOAReReducedLightcurve(lightcurve_number, data_folder,
                                            '/Users/stela/Documents/Scripts/ai_microlensing/merida/data/'
                                            'lightcurves_from_ian/stela_list.txt')  # path to the master file
        days, fluxes, flux_errors = lightcurve.get_days_fluxes_errors()
        print(days, fluxes, flux_errors)
        days, magnitudes, magnitudes_errors = lightcurve.get_days_magnitudes_errors()
        print(days, magnitudes, magnitudes_errors)
        # Path of the folder where you want to save the plots
        output_folder = '/Users/stela/Documents/Scripts/ai_microlensing/merida/data/lightcurves_from_ian/plots/'
        lightcurve.quick_flux_plot(output_folder)
        lightcurve.quick_magnitude_plot(output_folder)
