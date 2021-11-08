import os
import shutil
from pathlib import Path

print('Managing Process has been started')

# Download Path
downloads_path = str(Path.home() / "Downloads")

# Path to manage
path = downloads_path
path2 = downloads_path

# Getting All files present in given path
all_files = next(os.walk(path))[2]

# Getting All folders present in given path
all_folders = next(os.walk(path))[1]

# All image extensions
images = ('.jpg','.png','.jpeg','.jfif','.tfif','.psd','.eps','.ai','.indd','.raw','.svg')

# All archieve extensions
archieve = ('.7z','.tar','.wim','.zip','.tar.gz')

# All GIF extensions
gif = ('.gif')

# All softwares extensions
softwares = ('.exe','.msi','.iso')

# All documents extensions
documents = ('.docx','.pdf','.ppt','.pptx','.doc','.html','.htm','.odt','.xls','.xlsx','.odx','.txt','.md')

# All audio extensions
audio = ('.mp3','.wav','.m4a','.flac','.wma','.acc')

# All video extensions
video = ('.mp4','.mov','.wmv','.avi','.avchd','.flv','.f4v','.swf','.mkv','.webm','.html5','.mpeg-2')

# All apps extensions
apps = ('.lnk')

# Folders to make
folders_make = ['Images','Archieves','Documents','Softwares','Apps','Folders','Video','Audio','GIF']

# Folders to ignore
except_folders = ('Images','Softwares','Folders','Archieves','Documents','Apps','Video','Audio','GIF')

print('')
print('Managing Files..')

# Checking All files and arranging them
for files in all_files:
    # Checking for images files
    if files.endswith(images):
        # Checking if folder already exists
        check_dir = os.path.exists(path2 + '\\' + folders_make[0])
        
        # Checking for if directory already exists
        if not check_dir:
            
            # Making Images folder
            os.mkdir(path2 + '\\' + folders_make[0])
            
            # Moving to files to images
            os.replace(path + '\\' + files, path2 + '\\' + folders_make[0] + '\\' + files)
        else:
            # Moving to files to images
            os.replace(path + '\\' + files, path2 + '\\' + folders_make[0] + '\\' + files)
            
    # Checking for archieve files
    if files.endswith(archieve):
        # Checking if folder already exists
        check_dir = os.path.exists(path2 + '\\' + folders_make[1])
        
        # Checking for if directory already exists
        if not check_dir:
            
            # Making archieve folder
            os.mkdir(path2 + '\\' + folders_make[1])
            
            # Moving to files to archieve
            os.replace(path + '\\' + files, path2 + '\\' + folders_make[1] + '\\' + files)
        else:
            # Moving to files to archieve
            os.replace(path + '\\' + files, path2 + '\\' + folders_make[1] + '\\' + files)
            
    # Checking for documents files
    if files.endswith(documents):
        # Checking if folder already exists
        check_dir = os.path.exists(path2 + '\\' + folders_make[2])
        
        # Checking for if directory already exists
        if not check_dir:
            
            # Making documents folder
            os.mkdir(path2 + '\\' + folders_make[2])
            
            # Moving to files to documents
            os.replace(path + '\\' + files, path2 + '\\' + folders_make[2] + '\\' + files)
        else:
            # Moving to files to documents
            os.replace(path + '\\' + files, path2 + '\\' + folders_make[2] + '\\' + files)
            
    # Checking for softwares files
    if files.endswith(softwares):
        # Checking if folder already exists
        check_dir = os.path.exists(path2 + '\\' + folders_make[3])
        
        # Checking for if directory already exists
        if not check_dir:
            
            # Making softwares folder
            os.mkdir(path2 + '\\' + folders_make[3])
            
            # Moving to files to softwares
            os.replace(path + '\\' + files, path2 + '\\' + folders_make[3] + '\\' + files)
        else:
            # Moving to files to softwares
            os.replace(path + '\\' + files, path2 + '\\' + folders_make[3] + '\\' + files)
            
    # Checking for apps files
    if files.endswith(apps):
        # Checking if folder already exists
        check_dir = os.path.exists(path2 + '\\' + folders_make[4])
        
        # Checking for if directory already exists
        if not check_dir:
            
            # Making apps folder
            os.mkdir(path2 + '\\' + folders_make[4])
            
            # Moving to files to apps
            os.replace(path + '\\' + files, path2 + '\\' + folders_make[4] + '\\' + files)
        else:
            # Moving to files to apps
            os.replace(path + '\\' + files, path2 + '\\' + folders_make[4] + '\\' + files)
            
    # Checking for video files
    if files.endswith(video):
        # Checking if folder already exists
        check_dir = os.path.exists(path2 + '\\' + folders_make[6])
        
        # Checking for if directory already exists
        if not check_dir:
            
            # Making video folder
            os.mkdir(path2 + '\\' + folders_make[6])
            
            # Moving to files to video
            os.replace(path + '\\' + files, path2 + '\\' + folders_make[6] + '\\' + files)
        else:
            # Moving to files to video
            os.replace(path + '\\' + files, path2 + '\\' + folders_make[6] + '\\' + files)
            
    # Checking for audio files
    if files.endswith(audio):
        # Checking if folder already exists
        check_dir = os.path.exists(path2 + '\\' + folders_make[7])
        
        # Checking for if directory already exists
        if not check_dir:
            
            # Making audio folder
            os.mkdir(path2 + '\\' + folders_make[7])
            
            # Moving to files to audio
            os.replace(path + '\\' + files, path2 + '\\' + folders_make[7] + '\\' + files)
        else:
            # Moving to files to audio
            os.replace(path + '\\' + files, path2 + '\\' + folders_make[7] + '\\' + files)
            
    # Checking for gif files
    if files.endswith(gif):
        # Checking if folder already exists
        check_dir = os.path.exists(path2 + '\\' + folders_make[8])
        if not check_dir:
            
            # Making gif folder
            os.mkdir(path2 + '\\' + folders_make[8])
            
            # Moving to files to gif
            os.replace(path + '\\' + files, path2 + '\\' + folders_make[8] + '\\' + files)
        else:
            os.replace(path + '\\' + files, path2 + '\\' + folders_make[8] + '\\' + files)

print('Done')
print('')
print('Managing Folders..')

for folders in all_folders:
    # print(len(folders))
    check_for_empty = os.listdir(path + '\\' + folders)
    
    # Cecking if directory contain file or not
    if len(check_for_empty) == 0:
        
        # Deleting empty Directory
        os.rmdir(path + '\\' + folders)
    else:
        
        # Moving all folders except 'Images','Softwares','Folders','Archieves','Documents','Apps','Video','Audio','GIF'
        if not folders in except_folders:
            shutil.move(path + '\\' + folders, path2 + '\\' + folders_make[5])
print('Done')
print('Management Done')
        