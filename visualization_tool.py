"""
Type in the terminal:
bokeh serve --show visualization_tool.py
"""
from merida.server_for_lightcurves import server_caller

# ======================================================================================================
#                                 =~.oOo.~=  Example URL data   =~.oOo.~=
# ======================================================================================================
# This file contains the parameters for the visualization tool
lightcurve_name = 'gb1-R-1-1-315'
lightcurve_class ='positive'
data_local = False # If you are using URL, set this to False
data_path = None

server_caller(lightcurve_name, lightcurve_class, data_local, data_path)



# ======================================================================================================
#                                =~.oOo.~=  Example local data   =~.oOo.~=
# ======================================================================================================
# This file contains the parameters for the visualization tool
# lightcurve_name = 'gb10-R-6-0-192695'
# lightcurve_name = 'gb9-R-8-5-27219'
# lightcurve_name = 'gb13-R-9-3-489'
# lightcurve_name = 'gb14-R-8-0-44172'
# lightcurve_name = 'gb9-R-8-7-155979'
# lightcurve_name = 'gb18-R-9-7-93997'
# lightcurve_name = 'gb17-R-9-5-51749'
# lightcurve_name = 'gb13-R-3-0-11045'
# lightcurve_name = 'gb21-R-5-6-43515'
# lightcurve_name = 'gb4-R-10-2-141805'
# lightcurve_name = 'gb1-R-9-3-123457'
# lightcurve_name = 'gb10-R-9-4-501965'
# lightcurve_name = 'gb20-R-7-4-39900'
# lightcurve_name = 'gb3-R-9-0-94164'
# lightcurve_name = 'gb18-R-4-2-38447'
# lightcurve_name = 'gb13-R-4-1-74706'
# lightcurve_name = 'gb4-R-9-7-228753'
# lightcurve_name = 'gb4-R-4-1-209486'
# lightcurve_name = 'gb7-R-9-2-171168'
# lightcurve_name = 'gb11-R-7-4-83904'
# lightcurve_name = 'gb5-R-9-4-151844'
# lightcurve_name = 'gb16-R-8-1-11102'
# lightcurve_name = 'gb14-R-5-2-240687'
# lightcurve_name = 'gb5-R-9-7-1046804'
# lightcurve_name = 'gb5-R-9-7-1046804'
# lightcurve_name = 'gb17-R-4-2-57824'
# lightcurve_name = 'gb19-R-3-3-4091'
# lightcurve_name = 'gb8-R-10-7-6442'
# lightcurve_name = 'gb3-R-9-1-74738'
# lightcurve_name = 'gb2-R-9-2-25039'
# lightcurve_name = 'gb4-R-5-7-42508'


# lightcurve_name = 'gb15-R-6-4-65525'
# lightcurve_name = 'gb9-R-1-6-65772'
# lightcurve_name = 'gb5-R-8-3-134608'
# lightcurve_name = 'gb14-R-7-7-53333'
# lightcurve_name = 'gb10-R-7-4-31849'
# lightcurve_name = 'gb9-R-1-2-177243'
# lightcurve_name = 'gb10-R-7-3-372116'
# lightcurve_name = 'gb12-R-4-1-90951'
# lightcurve_name = 'gb7-R-4-5-81028'
# lightcurve_name = 'gb9-R-1-7-716348'
# lightcurve_name = 'gb9-R-9-2-227154'
# lightcurve_name = 'gb10-R-6-2-54495'
# lightcurve_name = 'gb17-R-7-5-121116'
# lightcurve_name = 'gb3-R-7-0-161925'
# lightcurve_name = 'gb5-R-3-7-341125'
# lightcurve_name = 'gb15-R-8-4-71470'
# lightcurve_name = 'gb5-R-8-3-175447'
# lightcurve_name = 'gb16-R-6-3-19298'
# lightcurve_name = 'gb4-R-7-2-264140'
# lightcurve_name = 'gb16-R-1-3-60751'
# lightcurve_name = 'gb14-R-2-3-306276'
# lightcurve_name = 'gb11-R-10-5-60958'
# lightcurve_name = 'gb16-R-5-5-102895'
# lightcurve_name = 'gb5-R-8-1-376643'
# lightcurve_name = 'gb4-R-8-0-190074'
# lightcurve_name = 'gb2-R-8-0-82922'
# lightcurve_name = 'gb4-R-5-6-74195'
# lightcurve_name = 'gb12-R-8-5-63608'
# lightcurve_name = 'gb14-R-6-2-55435'
# lightcurve_name = 'gb14-R-8-4-248720'
# lightcurve_name = 'gb13-R-3-6-116970'
# lightcurve_name = 'gb7-R-6-0-7188'
# lightcurve_name = 'gb2-R-9-1-188238'
# lightcurve_name = 'gb13-R-5-1-106142'
# lightcurve_name = 'gb13-R-6-2-86496'
# lightcurve_name = 'gb10-R-9-3-423070'
# lightcurve_name = 'gb14-R-3-6-206918'
# lightcurve_name = 'gb15-R-9-1-66362'
# lightcurve_name = 'gb8-R-10-4-157680'
# lightcurve_name = 'gb9-R-5-6-728624'
# lightcurve_name = 'gb10-R-2-1-400000'
# lightcurve_name = 'gb9-R-7-3-68085'
# lightcurve_name = 'gb18-R-5-4-89084'
# lightcurve_name = 'gb22-R-7-5-25689'
# lightcurve_name = 'gb13-R-4-5-8836'
# lightcurve_name = 'gb8-R-5-2-46134'
# lightcurve_name = 'gb14-R-5-3-125419'
# lightcurve_name = 'gb9-R-10-6-188759'
# lightcurve_name = 'gb10-R-6-4-55433'
# lightcurve_name = 'gb18-R-1-5-126761'
# lightcurve_name = 'gb9-R-7-4-468311'
# lightcurve_name = 'gb4-R-7-0-130762'
# lightcurve_name = 'gb7-R-4-1-44917'
# lightcurve_name = 'gb10-R-3-6-313915'
# lightcurve_name = 'gb9-R-5-3-342674'
# lightcurve_name = 'gb8-R-4-5-148653'
# lightcurve_name = 'gb20-R-7-4-51897'
# lightcurve_name = 'gb14-R-3-6-90793'
# lightcurve_name = 'gb14-R-4-4-147964'
lightcurve_name = 'gb13-R-8-0-53147'
# lightcurve_name = 'gb10-R-8-5-70149'
# lightcurve_name = 'gb5-R-8-7-565'
# lightcurve_name = 'gb15-R-2-1-103351'
# lightcurve_name = 'gb9-R-1-4-71508'
# lightcurve_name = 'gb13-R-1-6-103072'
# lightcurve_name = 'gb8-R-8-3-6501'
# lightcurve_name = 'gb13-R-1-2-151231'
# lightcurve_name = 'gb9-R-1-3-857881'
# lightcurve_name = 'gb1-R-3-1-58032'
# lightcurve_name = 'gb16-R-9-4-99978'

# ERE2
# lightcurve_name = 'gb11-R-1-7-58241'
# lightcurve_name = 'gb13-R-5-2-79244'
# lightcurve_name = 'gb10-R-7-6-50340'
# lightcurve_name = 'gb8-R-2-6-258'
# lightcurve_name = 'gb18-R-9-1-165578'
# lightcurve_name = 'gb18-R-3-3-244'
# lightcurve_name = 'gb14-R-1-5-430808'
# lightcurve_name = 'gb18-R-6-3-7079'
# lightcurve_name = 'gb10-R-10-3-6404'
# lightcurve_name = 'gb3-R-7-3-107370'
# lightcurve_name = 'gb10-R-2-7-171157'
# lightcurve_name = 'gb7-R-9-0-131181'
# lightcurve_name = 'gb11-R-4-6-5226'
# lightcurve_name = 'gb17-R-6-2-89442'
# lightcurve_name = 'gb2-R-5-2-20506'
# lightcurve_name = 'gb3-R-10-6-557639'
# lightcurve_name = 'gb9-R-1-3-391453'
# lightcurve_name = 'gb4-R-4-2-60907'
# lightcurve_name = 'gb9-R-2-7-571511'
# lightcurve_name = 'gb9-R-5-0-339810'
# lightcurve_name = 'gb17-R-1-1-1938'
# lightcurve_name = 'gb21-R-4-1-3492'
# lightcurve_name = 'gb5-R-8-1-545988'
# lightcurve_name = 'gb4-R-10-0-20651'
# lightcurve_name = 'gb9-R-3-3-7057'
# lightcurve_name = 'gb14-R-2-3-28763'
# lightcurve_name = 'gb12-R-9-1-1576'
# lightcurve_name = 'gb9-R-3-1-509375'
# lightcurve_name = 'gb14-R-2-4-1062'

# ERE3
# lightcurve_name = 'gb4-R-5-1-18240'
# lightcurve_name = 'gb11-R-3-6-17011'
# lightcurve_name = 'gb8-R-4-5-18771'
# lightcurve_name = 'gb18-R-7-5-20304'
# lightcurve_name = 'gb4-R-2-0-133850'
# lightcurve_name = 'gb5-R-7-0-11035'
# lightcurve_name = 'gb18-R-3-7-21130'
# lightcurve_name = 'gb19-R-2-1-12709'
# lightcurve_name = 'gb13-R-6-0-37914'

# lightcurve_name = 'gb14-R-5-4-137194'
# lightcurve_name = 'gb9-R-9-6-290890'
# lightcurve_name = 'gb3-R-9-0-94303'
# lightcurve_name = 'gb8-R-10-7-215'
# lightcurve_name = 'gb5-R-9-1-95785'
# lightcurve_name = 'gb8-R-4-4-5963'
# lightcurve_name = 'gb4-R-9-7-144619'
# lightcurve_name = 'gb2-R-9-5-134766'
# lightcurve_name = 'gb1-R-2-7-36717'
# lightcurve_name = 'gb4-R-10-6-367078'


# lightcurve_name = 'gb10-R-6-0-192695'
# lightcurve_name = 'gb13-R-9-3-489'
# lightcurve_name = 'gb9-R-8-7-155979'
# lightcurve_name = 'gb13-R-3-0-11045'
# lightcurve_name = 'gb21-R-5-6-43515'
# lightcurve_name = 'gb16-R-8-1-11102'
# lightcurve_name = 'gb2-R-9-2-25039'
# lightcurve_name = 'gb9-R-8-5-27219'


# Planetaries with no correction flux
# lightcurve_name = 'gb21-R-5-6-43515'
# lightcurve_name = 'gb13-R-9-3-489'
# lightcurve_name = 'gb14-R-6-2-55435'

# lightcurve_name = 'gb15-R-9-1-66362'
# lightcurve_name = 'gb13-R-3-0-11045'
# lightcurve_name = 'gb5-R-9-7-1046804'
# lightcurve_name = 'gb12-R-4-1-90951'

# lightcurve_class = 'negative'
# data_local = True
# # internal:
# general_path = '/Users/stela/Documents/Scripts/ai_microlensing/qusi_microlensing/data/microlensing_2M'
# field_path = f'{lightcurve_name.split("-")[0]}'
# # lightcurve_path = f'{general_path}/{field_path}/{lightcurve_name}.feather'
#
#
# server_caller(lightcurve_name, lightcurve_class, data_local, general_path, supercomputer_=True)

