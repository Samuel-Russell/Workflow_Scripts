import glob
import os
import shutil

# Get a list of files in the given directory 
dir_name = '/Users/samuelrussell/Documents/Satellite_Dataset/Sentinel_2'

list_of_files = filter( os.path.isfile,
                        glob.glob(dir_name + '/**/*', recursive=True) )

# Sorting list of files in the directory by size 
list_of_files = sorted( list_of_files,
                        key =  lambda x: os.stat(x).st_size)

# Iterate over sorted list of files
for file_path in list_of_files:
    file_size  = os.stat(file_path).st_size 
    print('FILE SIZE:', file_size,'bytes.', 'FILE PATH:', file_path)


# Move all tif files to same folder
    
source_dir = '/Users/samuelrussell/Documents/Satellite_Dataset/Sentinel_2/2019-10-15/patch_size_128_patch_overlap_16/patches/'

all_tifs_dir = '/Users/samuelrussell/Documents/Satellite_Dataset/Sentinel_2/2019-10-15/patch_size_128_patch_overlap_16/patches/all_tifs'
os.mkdir(all_tifs_dir)
    
file_names = filter( os.path.isfile,
                        glob.glob(source_dir + '/**/*', recursive=True) )
    
for file_name in file_names:
    shutil.move(os.path.join(source_dir, file_name), all_tifs_dir)

# Remove old empty folders
   
dir_list = glob.iglob(os.path.join(source_dir, "row_*"))
for path in dir_list:
    if os.path.isdir(path):
        shutil.rmtree(path) 

# Create directories for each band

B02_path = '/Users/samuelrussell/Documents/Satellite_Dataset/Sentinel_2/2019-10-15/patch_size_128_patch_overlap_16/patches/all_tifs/B02/'
os.mkdir(B02_path)

B03_path = '/Users/samuelrussell/Documents/Satellite_Dataset/Sentinel_2/2019-10-15/patch_size_128_patch_overlap_16/patches/all_tifs/B03/'
os.mkdir(B03_path)

B04_path = '/Users/samuelrussell/Documents/Satellite_Dataset/Sentinel_2/2019-10-15/patch_size_128_patch_overlap_16/patches/all_tifs/B04/'
os.mkdir(B04_path)

B08_path = '/Users/samuelrussell/Documents/Satellite_Dataset/Sentinel_2/2019-10-15/patch_size_128_patch_overlap_16/patches/all_tifs/B08/'
os.mkdir(B08_path)

# Move Tifs into new directories

# Move B02 files
pattern = all_tifs_dir + "/patched_sentinel_2_2019-10-15_B02*"
for file in glob.iglob(pattern, recursive=True):
    # get file name from path
    file_name = os.path.basename(file)
    shutil.move(file, B02_path + file_name)
    
# Move B03 files
pattern = all_tifs_dir + "/patched_sentinel_2_2019-10-15_B03*"
for file in glob.iglob(pattern, recursive=True):
    file_name = os.path.basename(file)
    shutil.move(file, B03_path + file_name)

# Move B04 files
pattern = all_tifs_dir + "/patched_sentinel_2_2019-10-15_B04*"
for file in glob.iglob(pattern, recursive=True):
    file_name = os.path.basename(file)
    shutil.move(file, B04_path + file_name)

# Move B08 files
pattern = all_tifs_dir + "/patched_sentinel_2_2019-10-15_B08*"
for file in glob.iglob(pattern, recursive=True):
    file_name = os.path.basename(file)
    shutil.move(file, B08_path + file_name)
