import pandas as pd
import os
import re
# Specify the directory containing .prn files
directory = r"C:\simind\mew20_10\spectral\static"

# Initialize an empty DataFrame to store the data
data = pd.DataFrame()

# Loop through all .prn files in the directory
for filename in os.listdir(directory):
    if filename.endswith(".prn"):
        file_path = os.path.join(directory, filename)
        # Read the .prn file and extract the second column data
        file_data = pd.read_csv(file_path, header=None, sep='\s+', usecols=[1], names=[filename])
        # Merge the data into the main DataFrame using the index from the first column
        data = pd.concat([data, file_data], axis=1)

output_filename = os.path.join(directory, "output.ods")

data.to_excel(output_filename, engine='odf')
