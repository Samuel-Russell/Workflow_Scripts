# Building Raster Mosaic
import rasterio
from rasterio.merge import merge
from rasterio.plot import show
import glob
import os

# File and folder path - Can be updated for each band directory (B02, B03, B04, B08)
dirpath = "FILE_PATH_PLACEHOLDER"

# Search criteria to select the tif files
search_key = "p*.tif"
q = os.path.join(dirpath, search_key)
print(q)

# glob function to list files
tif_fps = glob.glob(q)

# Files that were found:
tif_fps

# Empty list to populate with tif files
tif_files_to_mosaic = []

# Iterate over tif files and add them to list
for fp in tif_fps:
    src = rasterio.open(fp)
    tif_files_to_mosaic.append(src)

print(tif_files_to_mosaic)

# Apply rasterio merge function to obtain a single mosaic array and transformation info
mosaic, out_trans = merge(tif_files_to_mosaic)

# Plot the result
show(mosaic)

# Copy the metadata
out_meta = src.meta.copy()

# Update the metadata
out_meta.update({"driver": "GTiff",
                 "height": mosaic.shape[1],
                 "width": mosaic.shape[2],
                 "transform": out_trans,
                 }
                )

# Write the mosaic raster to desired location
out_file_path = os.path.join(dirpath, "MOSAIC_FILE_NAME.tif")

with rasterio.open(out_file_path, "w", **out_meta) as dest:
    dest.write(mosaic)