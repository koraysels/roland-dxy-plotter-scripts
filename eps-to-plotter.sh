#!/bin/bash

if [ $# -ne 1 ] || [ "${1##*.}" != "eps" ]; then
  echo "Usage: $0 input.eps"
  exit 1
fi

input_file="$1"
output_file="output/$(basename "${input_file%.*}")-distilled.hpgl"

# Create output directory if it doesn't exist
mkdir -p output

# Convert EPS to HPGL using pstoedit
pstoedit -f plot-hpgl "$input_file" output.hpgl

# Distill HPGL using hpgl-distiller
hpgl-distiller -i output.hpgl -o "$output_file"

echo "plotting $output_file"
# Plot the distilled HPGL file using plot_hpgl_file.py
python plot_hpgl_file.py "$output_file"

# Remove the intermediate output file
rm output.hpgl

echo "Done. Output file: $output_file"
