'''In Python, ZIP is used to compress and decompress files and directories. 
    The `zipfile` module provides tools for working with ZIP archives. ZIP archives 
    can be used to bundle multiple files into a single file, which is useful for 
    distribution and storage.
'''

### `zipfile` Module

'''
The `zipfile` module in Python allows you to create, read, write, append, and
 extract ZIP files. Here's how to use it:
'''

#### Creating a ZIP File
'''
To create a ZIP file and add files to it, you can use the `ZipFile` class in write mode.
'''

# **Example**:
import zipfile

# Create a new ZIP file and add files to it
with zipfile.ZipFile('archive.zip', 'w') as zipf:
    zipf.write('file1.txt', arcname='file1.txt')
    zipf.write('file2.txt', arcname='file2.txt')

'''
**Parameters**:
- `'archive.zip'`: The name of the ZIP file to create.
- `'w'`: Write mode. Other modes include `'r'` for reading and `'a'` for appending.
- `arcname`: Optional parameter specifying the name to use within the ZIP file.
'''

#### Extracting a ZIP File
'''
To extract files from a ZIP archive, you can use the `extractall` or `extract` method.
'''

# **Example**:
import zipfile

# Extract all files from a ZIP archive to the current directory
with zipfile.ZipFile('archive.zip', 'r') as zipf:
    zipf.extractall()

# Extract a specific file
with zipfile.ZipFile('archive.zip', 'r') as zipf:
    zipf.extract('file1.txt')

'''
**Parameters**:
- `extractall()`: Extracts all files to the current directory or a specified directory.
- `extract()`: Extracts a specific file from the ZIP archive.
'''

#### Listing Files in a ZIP Archive
'''
To list the files contained in a ZIP archive, you can use the `namelist` method.
'''

# **Example**:
import zipfile

# List files in a ZIP archive
with zipfile.ZipFile('archive.zip', 'r') as zipf:
    file_list = zipf.namelist()
    print(file_list)

# **Output**:
['file1.txt', 'file2.txt']

#### Adding Files to an Existing ZIP File

'''
To add files to an existing ZIP file, use the append mode `'a'`.
'''

# **Example**:
import zipfile

# Add a file to an existing ZIP file
with zipfile.ZipFile('archive.zip', 'a') as zipf:
    zipf.write('file3.txt', arcname='file3.txt')

### Working with ZIP Compression

# The `zipfile` module supports different compression methods:

'''
- **No Compression**: `zipfile.ZIP_STORED`
- **Deflate Compression**: `zipfile.ZIP_DEFLATED`
'''

# **Example with Compression**:
import zipfile

# Create a new ZIP file with deflate compression
with zipfile.ZipFile('compressed_archive.zip', 'w', zipfile.ZIP_DEFLATED) as zipf:
    zipf.write('file1.txt', arcname='file1.txt')
    zipf.write('file2.txt', arcname='file2.txt')

### Summary

'''
- **Creating ZIP Files**: Use `zipfile.ZipFile` in write mode to create and add files
     to a ZIP archive.
- **Extracting ZIP Files**: Use `extractall` or `extract` to extract files from a ZIP
     archive.
- **Listing Files**: Use `namelist` to list files in a ZIP archive.
- **Adding to Existing ZIP**: Use append mode `'a'` to add files to an existing ZIP file.
- **Compression Methods**: You can choose between no compression (`ZIP_STORED`) and deflate
     compression (`ZIP_DEFLATED`).
'''