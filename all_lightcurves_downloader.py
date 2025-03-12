from lightcurve_downloader import download_lightcurve
from merida.lightcurves_cls import Metadata
from tqdm import tqdm

metadata = Metadata()
df = metadata.dataframe

for lightcurve_name in tqdm(df['lightcurve_name']):
    print('\n', lightcurve_name, '\n')
    download_lightcurve(lightcurve_name, '', path_to_save_='data/microlensing_2M/', lightcurve_extension_='.feather')
