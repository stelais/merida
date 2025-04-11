from bokeh.layouts import column
from bokeh.io import curdoc

from merida.zones_for_lightcurves import general_zones, three_highest_intervals_finder
from merida.lightcurves_cls import OldLightCurvesFuguLocal, LightCurvesNExSciLocalCSV, LightCurvesNExSciURL, \
    LightCurvesNExSciLocalFeather, SuperComputerLightCurves


def server_caller(lightcurve_name_, lightcurve_class_, local_, data_path_=None, old_data_in_fugu=False,
                  nexsci_=False, extension_='.csv', supercomputer_=True):
    # Load lightcurve
    print('Loading lightcurve data...')
    if local_:
        if old_data_in_fugu:
            the_lightcurve = OldLightCurvesFuguLocal(lightcurve_name_=lightcurve_name_,
                                                     lightcurve_class_=lightcurve_class_,
                                                     data_path_=data_path_)
        elif nexsci_:
            if extension_ == '.csv':
                the_lightcurve = LightCurvesNExSciLocalCSV(lightcurve_name_=lightcurve_name_,
                                                            lightcurve_class_=lightcurve_class_,
                                                            data_path_=data_path_)
            elif extension_ == '.feather':
                the_lightcurve = LightCurvesNExSciLocalFeather(lightcurve_name_=lightcurve_name_,
                                                               lightcurve_class_=lightcurve_class_,
                                                               data_path_=data_path_)
            else:
                raise ValueError('Extension not recognized. \n Only feather and cvs are supported. \n ')

        elif supercomputer_:
            the_lightcurve = SuperComputerLightCurves(lightcurve_name_=lightcurve_name_,
                                                      data_path_=data_path_)
        else:
            raise ValueError('Class format not recognized. \n Supercomputer? NexSci? Old fugu. \n ')
    else:
        the_lightcurve = LightCurvesNExSciURL(lightcurve_name_=lightcurve_name_,
                                              lightcurve_class_=lightcurve_class_)
    # Calculate high magnification intervals
    print('Calculating high magnification intervals...')
    days, fluxes, cor_fluxes, fluxes_errors = the_lightcurve.get_days_fluxes_errors()
    three_starting_and_ending_days = three_highest_intervals_finder(days, fluxes)
    # Add to server document
    print('Generating plot zones...')
    big_zone_layout, small_zone_layout_1, small_zone_layout_2, small_zone_layout_3 = general_zones(the_lightcurve, three_starting_and_ending_days)
    curdoc().add_root(column(big_zone_layout, small_zone_layout_1, small_zone_layout_2, small_zone_layout_3))
    curdoc().title = f"Light curve {the_lightcurve.lightcurve_name}"
