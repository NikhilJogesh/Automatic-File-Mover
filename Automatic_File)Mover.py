import os
import shutil

main_path = 'D:/Nikhil/Python Projects/Automatic File Mover/Main/'

images_folder_path = 'D:/Nikhil/Python Projects/Automatic File Mover/Images'
doccument_folder_path = 'D:/Nikhil/Python Projects/Automatic File Mover/Documents'
music_folder_path = 'D:/Nikhil/Python Projects/Automatic File Mover/Music'
videos_folder_path = 'D:/Nikhil/Python Projects/Automatic File Mover/Videos'
zips_and_installers_folder_path = 'D:/Nikhil/Python Projects/Automatic File Mover/Zips and Installers'


images_extensions = ['.jpg', '.png', '.gif', '.bmp']
document_extensions = ['.docx', '.txt', '.pdf']
music_extensions = ['.mp3', '.wav']
videos_extensions = ['.mpeg', '.mpg', '.mp4', '.mkv', '.mov', '.avi']
zips_and_installers_extensions = ['.exe', '.gz', '.rar', '.zip']


main_dir = os.listdir(main_path)
 


for file in main_dir:
	
	splited_name = (os.path.splitext(file))
	extention = splited_name[1]
	print(extention)

	file_path = main_path + file
	
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
