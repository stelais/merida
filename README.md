# merida
MERIDA: MOA9yr Exploration and Research Interface for Dataset Analysis

```
git clone https://github.com/stelais/merida.git
pip install -r requirements.txt
```

---
### To visualize a light curve from the MOA 9 year dataset:
* In `visualization_tool.py`:
  * Change the `lightcurve_name` variable to the name of the light curve you want to visualize.
  * Define where your data is `data_path ='data/positive'`
  * If you want to use data from the NEXSci archive, you will have to change line 19 on `lightcurves_cls` in the LightCurvesNExSciURL class.
    
    Note that mine has: 
    ```
    self.url_main_path = 'https://exoplanetarchive.ipac.caltech.edu/workspace/TMP_dk5Wxv_13874/MOA/tab1/data/' 
    ```
    Unfortunately, this is a temporary link. You will have to open https://exoplanetarchive.ipac.caltech.edu/cgi-bin/MOA/nph-firefly?MOA , click to download a lightcurve and then change this `TMP_dk5Wxv_13874` equivalent to the one you have.

After done that, you just have to run the following command in the terminal:
```
bokeh serve --show visualization_tool.py
```

---
### To locally download a single MOA9yr lightcurve from the NExSci archive:
* Change line 19 on `lightcurves_cls` in the LightCurvesNExSciURL class.
    Note that mine has: 
    ```
    self.url_main_path = 'https://exoplanetarchive.ipac.caltech.edu/workspace/TMP_dk5Wxv_13874/MOA/tab1/data/' 
    ```
    Unfortunately, this is a temporary link. You will have to open https://exoplanetarchive.ipac.caltech.edu/cgi-bin/MOA/nph-firefly?MOA , click to download a lightcurve and then change this `TMP_dk5Wxv_13874` equivalent to the one you have. 
* In `lightcurve_downloader.py`:
  * Change the `lightcurve_name` variable to the name of the light curve you want to download.
  * You can change the path by adding the variable `path_to_save_ ='[the_path_you_want_]/'`

After done that, you just have to run the following command in the terminal:
```
python lightcurve_downloader.py
```
---
### To locally download ALL MOA9yr lightcurves from the NExSci archive:
* Change line 19 on `lightcurves_cls` in the LightCurvesNExSciURL class.
    Note that mine has: 
    ```
    self.url_main_path = 'https://exoplanetarchive.ipac.caltech.edu/workspace/TMP_dk5Wxv_13874/MOA/tab1/data/' 
    ```
    Unfortunately, this is a temporary link. You will have to open https://exoplanetarchive.ipac.caltech.edu/cgi-bin/MOA/nph-firefly?MOA , click to download a lightcurve and then change this `TMP_dk5Wxv_13874` equivalent to the one you have. 
* In `all_lightcurves_downloader.py`:
  * You can change the path by changing the variable `path_to_save_ ='[the_path_you_want_]/'`
  * You can also change the extension `lightcurve_extension_='.[extension]'`. Only feather and CSV supported for now. 

After done that, you just have to run the following command in the terminal:
```
python all_lightcurves_downloader.py
```
---
[Currently]
* All lightcurves from MOA 9 year data set from NEXSci archive should work. If it doesn't work, you can let me know.
* Script to download ALL lightcurves from MOA 9 year data set from NEXSci archive.
* Script to read METADATA.

[Future]
* Identify any data for MOA 9 yeardata set from NEXSci archive based on RA and DEC.

[Virtual tool in progress...]
https://merida.onrender.com/visualization_tool
* Only the light curve gb10-R-5-6-130249 as an example (it load this data from this Github repository)

* Takes about one minute to load it
  `visualization_tool.py`  
