import pandas as pd

merida_data_path = "/Users/stela/Documents/Scripts/ai_microlensing/merida/data"
qusi_data_path = ("/Users/stela/Documents/Scripts/ai_microlensing/qusi_microlensing/data/"
                  "microlensing_2M")

lightcurves_from_nn_df = pd.read_csv(f"{merida_data_path}/matched_selected_metadata.csv")
event_names = lightcurves_from_nn_df["lightcurve_name"].tolist()



# Initialize a list to store counting flux/cor_flux data points
results = []

# Loop through each event_name and process its corresponding Feather file
for event_name in event_names:
    field = event_name.split('-')[0]
    file_path = f"{qusi_data_path}/{field}/{event_name}.feather"

    try:
        # Read the Feather file
        lc_df = pd.read_feather(file_path)

        # Count data points
        flux_count = lc_df["flux"].count()
        flux_cor_count = lc_df["cor_flux"].count()

        # Print details
        print(f"File: {event_name}.feather, Flux Data Points: {flux_count}, Flux_Cor Data Points: {flux_cor_count}")

        # Append to results
        results.append([event_name, flux_count, flux_cor_count])

    except Exception as e:
        print(f"Could not process {event_name}.feather: {e}")

# Create a DataFrame with the new columns
df_updated = lightcurves_from_nn_df.merge(pd.DataFrame(results, columns=["lightcurve_name", "flux_count", "cor_flux_count"]),
                                          on="lightcurve_name", how="left")

# Save the updated CSV file
updated_file_path = f"{merida_data_path}/counting_selected_metadata.csv"
df_updated.to_csv(updated_file_path, index=False)
