"""
Code for matching star coordinates with MOA and OGLE alerts.
[In the future] This code will be organized in modules, to be easy to give target coordinates
and get back the alert names AND the equivalent lightcurve names.
"""
import pandas as pd
import numpy as np

# Tolerance for matching
tolerance = 0.01

general_path = '/Users/stela/Documents/Scripts/ai_microlensing/merida/data'

# Load the main dataset
selected_metadata_path = f"{general_path}/selected_metadata.csv"
selected_metadata = pd.read_csv(selected_metadata_path)

# List of RA/DEC reference tables to check against
moa_path = f"{general_path}/moa_alerts"
moa_tables = [
    f"{moa_path}/moa2_2006_radec.csv",
    f"{moa_path}/moa2_2007_radec.csv",
    f"{moa_path}/moa2_2008_radec.csv",
    f"{moa_path}/moa2_2009_radec.csv",
    f"{moa_path}/moa2_2010_radec.csv",
    f"{moa_path}/moa2_2011_radec.csv",
    f"{moa_path}/moa2_2012_radec.csv",
    f"{moa_path}/moa2_2013_radec.csv",
    f"{moa_path}/moa2_2014_radec.csv"
]

ogle_path = f"{general_path}/ogle_alerts"
ogle_tables = [
    f"{ogle_path}/ogle3_2006_radec.csv",
    f"{ogle_path}/ogle3_2007_radec.csv",
    f"{ogle_path}/ogle3_2008_radec.csv",
    f"{ogle_path}/ogle3_2009_radec.csv",
    f"{ogle_path}/ogle4_2011_radec.csv",
    f"{ogle_path}/ogle4_2012_radec.csv",
    f"{ogle_path}/ogle4_2013_radec.csv",
    f"{ogle_path}/ogle4_2014_radec.csv"
]

# Initialize columns to store matches
selected_metadata['MOA_alerts'] = np.nan
selected_metadata['OGLE_alerts'] = np.nan


# Function to find matching alerts within the tolerance
def find_alerts(row, reference_data, telescope):
    matches = reference_data[
        (np.abs(reference_data['RA_deg'] - row['ra_j2000']) <= tolerance) &
        (np.abs(reference_data['Dec_deg'] - row['dec_j2000']) <= tolerance)
        ]
    if not matches.empty:
        if telescope == 'MOA':
            return ";".join(matches['Name'].astype(str))  # MOA uses 'Name' column
        elif telescope == 'OGLE':
            return ";".join(matches['Event'].astype(str))  # OGLE uses 'Event' column
    return np.nan


# Iterate over MOA and OGLE tables
for telescope, radec_tables in [('MOA', moa_tables), ('OGLE', ogle_tables)]:
    for table in radec_tables:
        reference_data = pd.read_csv(table)

        # Find matches and accumulate them
        matches = selected_metadata.apply(lambda row: find_alerts(row, reference_data, telescope), axis=1)

        # Combine previous matches with new ones
        selected_metadata[telescope + '_alerts'] = selected_metadata[telescope + '_alerts'].fillna(
            '') + ";" + matches.fillna('')
        selected_metadata[telescope + '_alerts'] = selected_metadata[telescope + '_alerts'].str.strip(";")

# Replace empty strings with NaN
selected_metadata.replace("", np.nan, inplace=True)

# Save the updated file
updated_metadata_path = f"{general_path}/matched_selected_metadata_{tolerance}.csv"
selected_metadata.to_csv(updated_metadata_path, index=False)

print(f"Updated file saved as {updated_metadata_path}")
