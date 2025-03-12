from merida.lightcurves_cls import LightCurvesNExSciURL

def download_lightcurve(lightcurve_name_, lightcurve_class_, path_to_save_='data/', lightcurve_extension_='.csv'):
    the_lightcurve = LightCurvesNExSciURL(lightcurve_name_=lightcurve_name_,
                                          lightcurve_class_=lightcurve_class_)

    # Choose one of the following methods to save the lightcurve:
    if lightcurve_extension_ == '.csv':
        the_lightcurve.save_lightcurve_from_url_as_csv(path_to_save=path_to_save_)
    elif lightcurve_extension_ == '.feather':
        the_lightcurve.save_lightcurve_from_url_as_feather(path_to_save=path_to_save_)
    else:
        raise ValueError('Extension not recognized. \n Only feather and cvs are supported. \n '
                         'If you want, you can: \n '
                         'the_lightcurve = LightCurvesNExSciURL(lightcurve_name_=lightcurve_name_,'
                         'lightcurve_class_=lightcurve_class_)'
                         '\n and then use the pandas function you need \n '
                         'e.g. the_lightcurve.lightcurve_dataframe.to_excel(path_to_save + lightcurve_name_ + \'.xls\')'
                         ' ')


if __name__ == "__main__":
    # Before: Go to https://exoplanetarchive.ipac.caltech.edu/cgi-bin/MOA/nph-firefly?MOA
    # And find the temporary workspace
    # Change line 19 on lightcurves_cls.py to the new temporary workspace

    # # Example 01:
    lightcurve_name = 'gb1-R-1-1-315'
    lightcurve_class = 'positive'  # you can write anything here.
    #
    # # Example 02:
    # lightcurve_name = 'gb9-R-3-7-9719'
    # lightcurve_class = 'negative'

    # Example 03:
    # lightcurve_name ='gb10-R-5-6-130249'
    download_lightcurve(lightcurve_name, lightcurve_class)


