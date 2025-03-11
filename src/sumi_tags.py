"""
This function exists to read Takahiro Sumi (OsakaU/MOA) tags
Note that creating_complete_metadata() is a function that reads the metadata.csv file, adds the Sumi tags to it and
the alert names.
"""

import numpy as np
import pandas as pd


def meaning_of_sumi_tags(tag):
    if tag == 'v':
        meaning = 'Variable star'
    elif tag == 'n':
        meaning = 'Novalike objects'
    elif tag == 'nr':
        meaning = 'CV with repeating flares'
    elif tag == 'm':
        meaning = 'Moving objects'
    elif tag == 'j':
        meaning = 'Junk'
    elif tag == 'no_tag':
        meaning = 'No tag'
    elif tag == '':
        meaning = 'No tag'
    elif tag == np.nan:
        meaning = 'No tag'
    elif tag == 'c':
        meaning = 'Single-lens candidate'
    elif tag == 'cf':
        meaning = 'Single-lens candidate with finite source'
    elif tag == 'cp':
        meaning = 'Single-lens candidate with parallax'
    elif tag == 'cw':
        meaning = 'Weak candidate'
    elif tag == 'cs':
        meaning = 'Short event single-lens candidate'
    elif tag == 'cb':
        meaning = 'Binary lens candidate'
    else:
        meaning = np.nan
    return meaning


def read_sumi_nine_year_label(
        filepath_="data/candlist_2023Oct12.txt") -> pd.DataFrame:
    """
    Reads Takahiro Sumi's 9-year events table as a Pandas data frame
    :param path: The path to the events table file.
    :return: The data frame.
    """
    column_names = ['field', 'band', 'chip', 'subframe', 'ID',
                    'sumi_tag',
                    'x', 'y',
                    'tag06_07', 'separation06_07', 'ID06_07',
                    'x06_07', 'y06_07',
                    'tag_alert', 'separation_alert', 'name_alert',
                    'x_alert', 'y_alert',
                    'tag_extra_alert', 'separation_extra_alert', 'name_extra_alert',
                    'x_extra_alert', 'y_extra_alert',
                    'tag_extra_alert2', 'separation_extra_alert2', 'name_extra_alert2',
                    'x_extra_alert2', 'y_extra_alert2',
                    'tag_extra_alert3', 'separation_extra_alert3', 'name_extra_alert3',
                    'x_extra_alert3', 'y_extra_alert3'
                    ]
    column_types = {'field': np.str_, 'band': np.str_, 'chip': np.int_, 'subframe': np.int_, 'ID': np.int_,
                    'sumi_tag': np.str_,
                    'x': np.float64, 'y': np.float64,
                    'tag06_07': np.str_, 'separation06_07': np.float64, 'ID06_07': 'Int64',
                    'x06_07': np.float64, 'y06_07': np.float64,
                    'tag_alert': np.str_, 'separation_alert': np.float64, 'name_alert': np.str_,
                    'x_alert': np.float64, 'y_alert': np.float64,
                    'tag_extra_alert': np.str_, 'separation_extra_alert': np.float64,
                    'name_extra_alert': np.str_,
                    'x_extra_alert': np.float64, 'y_extra_alert': np.float64,
                    'tag_extra_alert2': np.str_, 'separation_extra_alert2': np.float64,
                    'name_extra_alert2': np.str_,
                    'x_extra_alert2': np.float64, 'y_extra_alert2': np.float64,
                    'tag_extra_alert3': np.str_, 'separation_extra_alert3': np.float64,
                    'name_extra_alert3': np.str_,
                    'x_extra_alert3': np.float64, 'y_extra_alert3': np.float64
                    }
    sumi_df = pd.read_table(filepath_, delim_whitespace=True, header=None,
                            names=column_names,
                            comment='#', dtype=column_types)
    sumi_df['lightcurve_name'] = sumi_df['field'].astype(str) + '-' + sumi_df['band'].astype(
        str) + '-' + sumi_df['chip'].astype(str) \
                                 + '-' + sumi_df['subframe'].astype(str) + '-' + sumi_df['ID'].astype(
        str)
    return sumi_df


def creating_complete_metadata():
    complete_dataframe = pd.read_csv('data/metadata.csv')
    complete_dataframe = complete_dataframe.set_index('lightcurve_name')
    sumi_df = read_sumi_nine_year_label()
    sumi_df = sumi_df.set_index('lightcurve_name')
    complete_dataframe['sumi_tag'] = sumi_df['sumi_tag']
    complete_dataframe['sumi_tag_meaning'] = complete_dataframe['sumi_tag'].apply(meaning_of_sumi_tags)
    complete_dataframe['name_alert'] = sumi_df['name_alert']
    complete_dataframe.loc[~complete_dataframe['name_alert'].astype(str).str.startswith('20'), 'name_alert'] = pd.NA
    complete_dataframe['name_extra_alert'] = sumi_df['name_extra_alert']
    complete_dataframe.loc[
        ~complete_dataframe['name_extra_alert'].astype(str).str.startswith('20'), 'name_extra_alert'] = pd.NA
    complete_dataframe['name_extra_alert2'] = sumi_df['name_extra_alert2']
    complete_dataframe.loc[
        ~complete_dataframe['name_extra_alert2'].astype(str).str.startswith('20'), 'name_extra_alert2'] = pd.NA

    # Step 1: If name_alert is NaN and name_extra_alert has a value, move it
    complete_dataframe.loc[
        complete_dataframe["name_alert"].isna() & complete_dataframe["name_extra_alert"].notna(), "name_alert"] = \
    complete_dataframe[
        "name_extra_alert"]
    complete_dataframe.loc[
        complete_dataframe["name_alert"] == complete_dataframe["name_extra_alert"], "name_extra_alert"] = np.nan

    # Step 2: If name_alert is still NaN but name_extra_alert2 has a value, move it
    complete_dataframe.loc[
        complete_dataframe["name_alert"].isna() & complete_dataframe["name_extra_alert2"].notna(), "name_alert"] = \
        complete_dataframe["name_extra_alert2"]
    complete_dataframe.loc[
        complete_dataframe["name_alert"] == complete_dataframe["name_extra_alert2"], "name_extra_alert2"] = np.nan

    # Step 3: Drop name_extra_alert2 if it only contains NaN
    if complete_dataframe["name_extra_alert2"].isna().all():
        complete_dataframe.drop(columns=["name_extra_alert2"], inplace=True)

    complete_dataframe.to_csv('data/complete_metadata.csv')

def table_selection_based_on_names(list_of_names):
    complete_dataframe = pd.read_csv('data/complete_metadata.csv')
    complete_dataframe = complete_dataframe.set_index('lightcurve_name')
    selected_df = complete_dataframe.loc[list_of_names]
    selected_df.to_csv('data/selected_metadata.csv')

if __name__ == '__main__':
     list_of_names = ['gb10-R-6-0-192695', 'gb9-R-8-5-27219', 'gb13-R-9-3-489', 'gb14-R-8-0-44172', 'gb9-R-8-7-155979',
      'gb18-R-9-7-93997', 'gb17-R-9-5-51749', 'gb13-R-3-0-11045', 'gb21-R-5-6-43515', 'gb4-R-10-2-141805',
      'gb1-R-9-3-123457', 'gb10-R-9-4-501965', 'gb20-R-7-4-39900', 'gb3-R-9-0-94164', 'gb18-R-4-2-38447',
      'gb13-R-4-1-74706', 'gb4-R-9-7-228753', 'gb4-R-4-1-209486', 'gb7-R-9-2-171168', 'gb11-R-7-4-83904',
      'gb5-R-9-4-151844', 'gb16-R-8-1-11102', 'gb14-R-5-2-240687', 'gb5-R-9-7-1046804', 'gb17-R-4-2-57824',
      'gb19-R-3-3-4091', 'gb8-R-10-7-6442', 'gb3-R-9-1-74738', 'gb2-R-9-2-25039', 'gb4-R-5-7-42508',
      'gb15-R-6-4-65525', 'gb9-R-1-6-65772', 'gb5-R-8-3-134608', 'gb14-R-7-7-53333', 'gb10-R-7-4-31849',
      'gb9-R-1-2-177243', 'gb10-R-7-3-372116', 'gb12-R-4-1-90951', 'gb7-R-4-5-81028', 'gb9-R-1-7-716348',
      'gb9-R-9-2-227154', 'gb10-R-6-2-54495', 'gb17-R-7-5-121116', 'gb3-R-7-0-161925', 'gb5-R-3-7-341125',
      'gb15-R-8-4-71470', 'gb5-R-8-3-175447', 'gb16-R-6-3-19298', 'gb4-R-7-2-264140', 'gb16-R-1-3-60751',
      'gb14-R-2-3-306276', 'gb11-R-10-5-60958', 'gb16-R-5-5-102895', 'gb5-R-8-1-376643', 'gb4-R-8-0-190074',
      'gb2-R-8-0-82922', 'gb4-R-5-6-74195', 'gb12-R-8-5-63608', 'gb14-R-6-2-55435', 'gb14-R-8-4-248720',
      'gb13-R-3-6-116970', 'gb7-R-6-0-7188', 'gb2-R-9-1-188238', 'gb13-R-5-1-106142', 'gb13-R-6-2-86496',
      'gb10-R-9-3-423070', 'gb14-R-3-6-206918', 'gb15-R-9-1-66362', 'gb8-R-10-4-157680', 'gb9-R-5-6-728624',
      'gb10-R-2-1-400000', 'gb9-R-7-3-68085', 'gb18-R-5-4-89084', 'gb22-R-7-5-25689', 'gb13-R-4-5-8836',
      'gb8-R-5-2-46134', 'gb14-R-5-3-125419', 'gb9-R-10-6-188759', 'gb10-R-6-4-55433', 'gb18-R-1-5-126761',
      'gb9-R-7-4-468311', 'gb4-R-7-0-130762', 'gb7-R-4-1-44917', 'gb10-R-3-6-313915', 'gb9-R-5-3-342674',
      'gb8-R-4-5-148653', 'gb20-R-7-4-51897', 'gb14-R-3-6-90793', 'gb14-R-4-4-147964', 'gb13-R-8-0-53147',
      'gb10-R-8-5-70149', 'gb5-R-8-7-565', 'gb15-R-2-1-103351', 'gb9-R-1-4-71508', 'gb13-R-1-6-103072',
      'gb8-R-8-3-6501', 'gb13-R-1-2-151231', 'gb9-R-1-3-857881', 'gb1-R-3-1-58032', 'gb16-R-9-4-99978']
     table_selection_based_on_names(list_of_names)

