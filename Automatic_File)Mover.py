import os
import shutil
import json

# opens the json file containing the paths 
with open('paths.json', ) as f:
	# loads the file
	paths = json.load(f)
	# access the dictionary present in the list
	paths = paths[0]

# add a "\\" to each path to avoid errors
for key in paths.keys():
	path = paths[key]
	if type(path) == str:
		path = f'{path}\\'
		paths[key] = path
	
# sets the path for the main folder
main_path = paths['main_folder']

#sets the folder path for every file group\type
images_folder_path = paths['images_path']
doccument_folder_path = paths['documents_path']
music_folder_path = paths['songs_path']
videos_folder_path = ['videos_path']
zips_and_installers_folder_path = ['zips_executables_path']

# creating a list of file formats for each file groups\type 
images_extensions = ['.jpg', '.png', '.gif', '.bmp']
document_extensions = ['.docx', '.txt', '.pdf']
music_extensions = ['.mp3', '.wav']
videos_extensions = ['.mpeg', '.mpg', '.mp4', '.mkv', '.mov', '.avi']
zips_and_installers_extensions = ['.exe', '.gz', '.rar', '.zip']

# sets the main folder
main_dir = os.listdir(main_path)
 
# for every file in the main folder, 
# it checks its file type
# and moves it to its respective folder
for file in main_dir:
	# splits the file name and sets the file extension to a variable
	splited_name = (os.path.splitext(file))
	extention = splited_name[1]
	# sets the full path location of the file
	file_path = main_path + file
	
	# checks the file extension and moves to its destination folder
	if images_extensions.count(extention) > 0: 
		shutil.move(file_path , images_folder_path)

	elif document_extensions.count(extention) > 0:
		shutil.move(file_path , doccument_folder_path)

	elif music_extensions.count(extention) > 0:
		shutil.move(file_path , music_folder_path)

	elif videos_extensions.count(extention) > 0:
		shutil.move(file_path , videos_folder_path)

	elif zips_and_installers_extensions.count(extention) > 0:
		shutil.move(file_path , zips_and_installers_folder_path)
