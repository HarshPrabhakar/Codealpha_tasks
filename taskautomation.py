import os
import shutil
from pathlib import Path

# Define the folder mapping based on file extensions
EXTENSION_FOLDERS = {
    'Images': ['.jpg', '.jpeg', '.png', '.gif', '.bmp'],
    'Documents': ['.pdf', '.docx', '.txt', '.xlsx', '.pptx'],
    'Audio': ['.mp3', '.wav', '.aac'],
    'Video': ['.mp4', '.mov', '.avi'],
    'Archives': ['.zip', '.rar', '.tar', '.gz'],
    'Code': ['.py', '.js', '.html', '.css', '.java'],
}

# Base directory to organize
BASE_DIR = Path.home() / 'Downloads'  # Change to your target directory

# Create folders for each file type if they don't exist
for folder in EXTENSION_FOLDERS.keys():
    folder_path = BASE_DIR / folder
    if not folder_path.exists():
        folder_path.mkdir()

def move_file(file_path, destination_folder):
    try:
        shutil.move(str(file_path), str(destination_folder))
        print(f"Moved: {file_path} -> {destination_folder}")
    except Exception as e:
        print(f"Error moving file {file_path}: {e}")

def organize_files():
    for item in BASE_DIR.iterdir():  # Iterate over items in the base directory
        if item.is_file():  # If the item is a file
            file_extension = item.suffix.lower()
            
            moved = False
            for folder, extensions in EXTENSION_FOLDERS.items():
                if file_extension in extensions:
                    move_file(item, BASE_DIR / folder)
                    moved = True
                    break

            if not moved:
                # Move files with unknown extensions to a folder called 'Others'
                other_folder = BASE_DIR / 'Others'
                if not other_folder.exists():
                    other_folder.mkdir()
                move_file(item, other_folder)

if __name__ == "__main__":
    organize_files()
