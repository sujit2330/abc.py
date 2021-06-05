import os
# this will return a tuple of roots and extension
split_tuple=os.path.splitext("abc_file.python")
print(split_tuple)
#extract the file name and extension
file_name=split_tuple[0]
file_extension=split_tuple[1]
print("File Name:",file_name)
print("File Extension",file_extension)
