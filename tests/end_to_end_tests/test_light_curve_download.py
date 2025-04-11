from merida.lightcurves_cls import LightCurvesNExSciURL


def test_light_curve_download():
    """
    Perform a very basic check that the light curve data is obtained.
    """
    lightcurve_name = 'gb1-R-1-1-315'
    lightcurve_class = ''
    light_curve = LightCurvesNExSciURL(lightcurve_name_=lightcurve_name, lightcurve_class_=lightcurve_class)
    assert light_curve.lightcurve_dataframe.shape[0] > 10_000
