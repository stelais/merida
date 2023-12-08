from bokeh.layouts import column
from bokeh.io import curdoc

from src.zones_for_lightcurves import general_zones, three_highest_intervals_finder
from src.lightcurves_cls import LightCurvesLocal, LightCurvesURL


def server_caller(lightcurve_name_, lightcurve_class_, local_, data_path_=None):
    # Load lightcurve
    print('Loading lightcurve data...')
    if local_:
        the_lightcurve = LightCurvesLocal(lightcurve_name_=lightcurve_name_,
                                          lightcurve_class_=lightcurve_class_,
                                          data_path_=data_path_)
    else:
        the_lightcurve = LightCurvesURL(lightcurve_name_=lightcurve_name_,
                                        lightcurve_class_=lightcurve_class_)
    # Calculate high magnification intervals
    print('Calculating high magnification intervals...')
    days, fluxes, fluxes_errors = the_lightcurve.get_days_fluxes_errors()
    three_starting_and_ending_days = three_highest_intervals_finder(days, fluxes)
    # Add to server document
    print('Generating plot zones...')
    big_zone_layout, small_zone_layout_1, small_zone_layout_2, small_zone_layout_3 = general_zones(the_lightcurve, three_starting_and_ending_days)
    curdoc().add_root(column(big_zone_layout, small_zone_layout_1, small_zone_layout_2, small_zone_layout_3))
    curdoc().title = f"Light curve {the_lightcurve.lightcurve_name}"
