from src.lightcurves_cls import LightCurvesNExSciURL

# lightcurve_name ='gb10-R-5-6-130249'
lightcurve_name = 'gb1-R-1-1-315'
lightcurve_class ='positive' # you can write anything here.
the_lightcurve = LightCurvesNExSciURL(lightcurve_name_=lightcurve_name,
                                      lightcurve_class_=lightcurve_class)
the_lightcurve.save_lightcurve_from_url_as_feather(path_to_save='data/')
the_lightcurve.save_lightcurve_from_url_as_csv(path_to_save='data/')

