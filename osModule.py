import os
import datetime
# print(dir(os)) #gives all methods and attributes which we have access to
# print(os.getcwd())  # get current working directory
# os.chdir("/Users/darsh/Desktop/")
# print(os.getcwd())
# print(os.listdir()) #lists all sub directories under cwd
# creating a directory
# os.mkdir('dsh')
# creating a tree of directories
# os.makedirs('dsh1/subdir')
# deleting
# os.rmdir('dsh1/subdir')  # this only removes the inner mentioned directory
# os.removedirs('dsh1/subdir')#removes the complete parh of directories
# renaming a file
# os.rename('dsh', 'dsh2')
# print(os.stat('dsh2')) #gives the stat-fields like timestamp, size etc
# atime = os.stat('dsh2').st_atime
# mtime = os.stat('dsh2').st_mtime
# ctime = os.stat('dsh2').st_ctime
# print(datetime.datetime.fromtimestamp(atime))
# print(datetime.datetime.fromtimestamp(mtime))
# print(datetime.datetime.fromtimestamp(ctime))
# walk() traverses through and gives an object containing dirpath(current directory path), dirnames(list of sub-directories in that), filenames(list of files in that)
# for dirpath, dirnames, filenames in os.walk('/Users/darsh/Desktop/6th'):
#     print('Current directory: ', dirpath)
#     print('Directories: ', dirnames)
#     print('Files: ', filenames)
#     print()
# gives the environment variable path for name "TEMP"
# print(os.environ.get('TEMP'))
# craeting a file a specified path
file_path = os.path.join(os.environ.get(
    'TEMP'), 'test.txt')  # this prepares the path
# print(file_path)

print(os.path.basename(file_path))  # gives the filename
print(os.path.dirname(file_path))  # gives the directory name
print(os.path.split(file_path))  # gives both
print(os.path.exists(file_path))  # checks if the file exists
print(os.path.isdir(file_path))  # checks if its a directory
print(os.path.isfile(file_path))  # checks if its a file
print(os.path.splitext(file_path))  # gives the path of file and its extension
