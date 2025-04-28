import pandas as pd
from astropy.coordinates import SkyCoord
import astropy.units as u

def convert_to_decimal_degrees(ra_hms, dec_dms):
    coord = SkyCoord(ra=ra_hms, dec=dec_dms, unit=(u.hourangle, u.deg))
    return coord.ra.deg, coord.dec.deg

# Alternative from jasmine
# Function to convert RA from 'HH:MM:SS' to decimal degrees
def ra_hms_to_deg(ra_hms):
    h, m, s = [float(i) for i in ra_hms.split(':')]
    ra_deg = 15 * (h + m / 60 + s / 3600)
    return ra_deg


# Function to convert Dec from 'DD:MM:SS' to decimal degrees
def dec_dms_to_deg(dec_dms):
    sign = -1 if dec_dms[0] == '-' else 1
    d, m, s = [float(i) for i in dec_dms.split(':')]
    dec_deg = sign * (abs(d) + m / 60 + s / 3600)
    return dec_deg

if __name__ == '__main__':
    # ogle_alerts_path = '/Users/stela/Documents/Scripts/ai_microlensing/merida/data/ogle_alerts'
    # ogle_tables = [f'{ogle_alerts_path}/ogle3_2006.csv',
    #                f'{ogle_alerts_path}/ogle3_2007.csv',
    #                f'{ogle_alerts_path}/ogle3_2008.csv',
    #                f'{ogle_alerts_path}/ogle3_2009.csv',
    #                f'{ogle_alerts_path}/ogle4_2011.csv',
    #                f'{ogle_alerts_path}/ogle4_2012.csv',
    #                f'{ogle_alerts_path}/ogle4_2013.csv',
    #                f'{ogle_alerts_path}/ogle4_2014.csv']
    # for ogle_table in ogle_tables:
    #     df = pd.read_csv(ogle_table)
    #     df[['RA_deg', 'Dec_deg']] = df.apply(lambda row: convert_to_decimal_degrees(row['RA (J2000)'],
    #                                                                                 row['Dec (J2000)']),
    #                                          axis=1, result_type='expand')
    #     new_name = ogle_table.split('.cs')[0]+'_radec.csv'
    #     df.to_csv(new_name, index=False)
    #     print(f'{new_name} saved.')

    moa_alerts_path = '/data/alerts/moa_alerts'
    moa_tables = [f'{moa_alerts_path}/moa2_2006.csv',
                  f'{moa_alerts_path}/moa2_2007.csv',
                  f'{moa_alerts_path}/moa2_2008.csv',
                  f'{moa_alerts_path}/moa2_2009.csv',
                  f'{moa_alerts_path}/moa2_2010.csv',
                  f'{moa_alerts_path}/moa2_2011.csv',
                  f'{moa_alerts_path}/moa2_2012.csv',
                  f'{moa_alerts_path}/moa2_2013.csv',
                  f'{moa_alerts_path}/moa2_2014.csv']
    for moa_table in moa_tables:
        df = pd.read_csv(moa_table)
        df[['RA_deg', 'Dec_deg']] = df.apply(lambda row: convert_to_decimal_degrees(row['RA'],
                                                                                    row['Dec']),
                                             axis=1, result_type='expand')
        new_name = moa_table.split('.cs')[0]+'_radec.csv'
        df.to_csv(new_name, index=False)
        print(f'{new_name} saved.')