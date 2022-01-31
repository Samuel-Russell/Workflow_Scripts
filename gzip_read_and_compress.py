# Reading a compressed file using gzip

import gzip
with gzip.open('/home/Sam/file.txt.gz', 'rb') as f:
    file_content = f.read()
    
# Example of how to create a compressed GZIP file:

import gzip
content = b"Lots of content here"
with gzip.open('/home/Sam/file.txt.gz', 'wb') as f:
    f.write(content)

## Ensure file is in working directory
## Module zlib is needed to suport gzip format