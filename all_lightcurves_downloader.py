from multiprocessing import Pool

from lightcurve_downloader import download_lightcurve
from merida.lightcurves_cls import Metadata
from tqdm import tqdm


def process_light_curve_name(light_curve_name):
    print('\n', light_curve_name, '\n')
    download_lightcurve(light_curve_name, '', path_to_save_='data/microlensing_2M/', lightcurve_extension_='.feather')


def download_all_light_curves():
    metadata = Metadata()
    df = metadata.dataframe
    with Pool(15) as pool:
        for _ in tqdm(pool.imap_unordered(process_light_curve_name, df['lightcurve_name'])):
            pass


if __name__ == '__main__':
    download_all_light_curves()
