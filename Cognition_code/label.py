import os
import pandas as pd

# Folder containing participant CSV files
input_folder = "../excel sheets"  # 🔁 Replace with your actual folder path
output_file = "cog_slider_values.xlsx"

# Columns to extract
slider_columns = ["slider_40.response", "slider_41.response", "slider_42.response"]

# Mapping from values to labels
value_label_mapping = {
    1: "low",
    2: "medium",
    3: "high"
}

# Container for final results
final_data = []

# Loop through each CSV file
for filename in os.listdir(input_folder):
    if filename.endswith(".csv"):
        file_path = os.path.join(input_folder, filename)
        df = pd.read_csv(file_path)

        # Check if all slider columns are present
        if not all(col in df.columns for col in slider_columns):
            print(f"⚠️ Missing slider columns in {filename}, skipping.")
            continue

        # Replace 'nil' with NaN
        df_cleaned = df[slider_columns].replace("nil", pd.NA)

        # Get the last non-null value for each column
        last_values = df_cleaned.apply(lambda col: col.dropna().iloc[-1] if col.dropna().size > 0 else pd.NA)

        # Map numeric value to label (after converting to int, if possible)
        labels = {}
        for col in slider_columns:
            try:
                val = int(last_values[col])
                labels[col] = value_label_mapping.get(val, "unknown")
            except:
                labels[col] = "unknown"

        # Extract participant name from filename
        participant_name = os.path.splitext(filename)[0]

        # Add to results
        final_data.append({
            "Name": participant_name,
            "slider_40": labels["slider_40.response"],
            "slider_41": labels["slider_41.response"],
            "slider_42": labels["slider_42.response"]
        })

# Convert to DataFrame
combined_df = pd.DataFrame(final_data)

# Save to Excel
combined_df.to_excel(output_file, index=False, sheet_name="Slider_Values", engine="openpyxl")

print(f"✅ Final labeled slider values saved to '{output_file}'")
