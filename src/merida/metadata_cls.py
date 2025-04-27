import pandas as pd
from dataclasses import dataclass

def moa_metadata_to_df(path ='data/metadata.csv'):
    # dataframe = pd.read_csv(path, float_precision='round_trip')
    dataframe = pd.read_csv(path)
    return dataframe


@dataclass
class MOA_Lightcurve_Metadata:
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

    def __init__(self, internal_lightcurve_name, *,
                 path_to_metadata='data/metadata.csv',
                 pass_info_separately=False,
                 field=None,
                 chip=None,
                 subframe=None,
                 moa_sub_id=None):
        if pass_info_separately is not True:
            self.internal_lightcurve_name = internal_lightcurve_name
        elif pass_info_separately is True:
            self.internal_lightcurve_name = f'gb{field}-R-{chip}-{subframe}-{moa_sub_id}'
        else:
            raise ValueError('pass_info_separately must be a boolean. '
                             'It indicates if you are giving the name as "gb1-R-1-1-315"'
                             'or if you will pass each of them separately, as field=1, chip=1, subframe=1, '
                             'moa_sub_id=315')
        self.all_metadata = moa_metadata_to_df(path_to_metadata)
        self.metadata = self.all_metadata[self.all_metadata['lightcurve_name'] == self.internal_lightcurve_name]
        self.field = self.metadata['field'].values[0]
        self.chip = self.metadata['chip'].values[0]
        self.subframe = self.metadata['subframe'].values[0]
        self.id = self.metadata['id'].values[0]
        self.tag = self.metadata['tag'].values[0]
        self.x = self.metadata['x'].values[0]
        self.y = self.metadata['y'].values[0]
        self.ra_j2000 = self.metadata['ra_j2000'].values[0]
        self.dec_j2000 = self.metadata['dec_j2000'].values[0]
        self.number_of_data_points = self.metadata['number_of_data_points'].values[0]
        self.number_of_frames_object_is_detected = self.metadata['number_of_frames_object_is_detected'].values[0]
        self.max_significance = self.metadata['max_significance'].values[0]
        self.sum_of_continuous_significance = self.metadata['sum_of_continuous_significance'].values[0]
        self.chi_squared_outside_search_window = self.metadata['chi_squared_outside_search_window'].values[0]
        self.dophot_object_reference_image_separation = self.metadata['dophot_object_reference_image_separation'].values[0]
        self.dophot_id = self.metadata['dophot_id'].values[0]
        self.dophot_type = self.metadata['dophot_type'].values[0]
        self.dophot_magnitude = self.metadata['dophot_magnitude'].values[0]
        self.dophot_magnitude_error = self.metadata['dophot_magnitude_error'].values[0]
        self.pspl_t0 = self.metadata['pspl_t0'].values[0]
        self.pspl_tE = self.metadata['pspl_tE'].values[0]
        self.pspl_u0 = self.metadata['pspl_u0'].values[0]
        self.pspl_source_flux = self.metadata['pspl_source_flux'].values[0]
        self.pspl_blending_flux = self.metadata['pspl_blending_flux'].values[0]
        self.pspl_t0_parabolic_error = self.metadata['pspl_t0_parabolic_error'].values[0]
        self.pspl_tE_parabolic_error = self.metadata['pspl_tE_parabolic_error'].values[0]
        self.pspl_tE_error_lower_limit = self.metadata['pspl_tE_error_lower_limit'].values[0]
        self.pspl_tE_error_upper_limit = self.metadata['pspl_tE_error_upper_limit'].values[0]
        self.pspl_u0_parabolic_error = self.metadata['pspl_u0_parabolic_error'].values[0]
        self.pspl_u0_error_lower_limit = self.metadata['pspl_u0_error_lower_limit'].values[0]
        self.pspl_u0_error_upper_limit = self.metadata['pspl_u0_error_upper_limit'].values[0]
        self.pspl_source_flux_error = self.metadata['pspl_source_flux_error'].values[0]
        self.pspl_blending_flux_error = self.metadata['pspl_blending_flux_error'].values[0]
        self.pspl_chi_squared = self.metadata['pspl_chi_squared'].values[0]
        self.fspl_t0 = self.metadata['fspl_t0'].values[0]
        self.fspl_tE = self.metadata['fspl_tE'].values[0]
        self.fspl_u0 = self.metadata['fspl_u0'].values[0]
        self.fspl_rho = self.metadata['fspl_rho'].values[0]
        self.fspl_source_flux = self.metadata['fspl_source_flux'].values[0]
        self.fspl_blending_flux = self.metadata['fspl_blending_flux'].values[0]
        self.fspl_t0_parabolic_error = self.metadata['fspl_t0_parabolic_error'].values[0]
        self.fspl_tE_parabolic_error = self.metadata['fspl_tE_parabolic_error'].values[0]
        self.fspl_tE_error_lower_limit = self.metadata['fspl_tE_error_lower_limit'].values[0]
        self.fspl_tE_error_upper_limit = self.metadata['fspl_tE_error_upper_limit'].values[0]
        self.fspl_u0_parabolic_error = self.metadata['fspl_u0_parabolic_error'].values[0]
        self.fspl_u0_error_lower_limit = self.metadata['fspl_u0_error_lower_limit'].values[0]
        self.fspl_u0_error_upper_limit = self.metadata['fspl_u0_error_upper_limit'].values[0]
        self.fspl_rho_parabolic_error = self.metadata['fspl_rho_parabolic_error'].values[0]
        self.fspl_rho_error_lower_limit = self.metadata['fspl_rho_error_lower_limit'].values[0]
        self.fspl_rho_error_upper_limit = self.metadata['fspl_rho_error_upper_limit'].values[0]
        self.fspl_source_flux_error = self.metadata['fspl_source_flux_error'].values[0]
        self.fspl_blending_flux_error = self.metadata['fspl_blending_flux_error'].values[0]
        self.fspl_chi_squared = self.metadata['fspl_chi_squared'].values[0]
        self.separation_to_alert_position1 = self.metadata['separation_to_alert_position1'].values[0]
        self.alert_id1 = self.metadata['alert_id1'].values[0]
        self.alert_x1 = self.metadata['alert_x1'].values[0]
        self.alert_y1 = self.metadata['alert_y1'].values[0]
        self.separation_to_alert_position2 = self.metadata['separation_to_alert_position2'].values[0]
        self.alert_id2 = self.metadata['alert_id2'].values[0]
        self.alert_x2 = self.metadata['alert_x2'].values[0]
        self.alert_y2 = self.metadata['alert_y2'].values[0]
        self.lightcurve_name = self.metadata['lightcurve_name'].values[0]



if __name__ == '__main__':
    # Example of how to use the class
    # lightcurve = MOA_Lightcurve_Metadata('gb1-R-1-0-1')
    lightcurve = MOA_Lightcurve_Metadata(None,
                                         pass_info_separately=True,
                                         field=1, chip=1, subframe=0, moa_sub_id=1)
    print(lightcurve.field)
    print(lightcurve.chip)
    print(lightcurve.subframe)
    print(lightcurve.id)
    print(lightcurve.x)
    print(lightcurve.y)
    print(lightcurve.ra_j2000)
    print(lightcurve.dec_j2000)

