# merida
MERIDA: MOA9yr Exploration and Research Interface for Dataset Analysis

Installing from github (should be most updated available version):
```
git clone https://github.com/stelais/merida.git
pip install -r requirements.txt
```
Installing as a pip package:
```
pip install merida
```

---
### To visualize a light curve from the MOA 9 year dataset:
* In `visualization_tool.py`:
  * Change the `lightcurve_name` variable to the name of the light curve you want to visualize.
  * Define where your data is `data_path ='data/positive'`

After done that, you just have to run the following command in the terminal:
```
bokeh serve --show visualization_tool.py
```

---
### To locally download a single MOA9yr lightcurve from the NExSci archive:
* In `lightcurve_downloader.py`:
  * Change the `lightcurve_name` variable to the name of the light curve you want to download.
  * You can change the path by adding the variable `path_to_save_ ='[the_path_you_want_]/'`

After done that, you just have to run the following command in the terminal:
```
python lightcurve_downloader.py
```
---
### To locally download ALL MOA9yr lightcurves from the NExSci archive [can be improved]:
* In `all_lightcurves_downloader.py`:
  * You can change the path by changing the variable `path_to_save_ ='[the_path_you_want_]/'`
  * You can also change the extension `lightcurve_extension_='.[extension]'`. Only `feather` and `CSV` supported for now.
  * Single threaded, this will take ~55 days. The script parallelizes this across 15 processes, and this is adjustable. 

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
