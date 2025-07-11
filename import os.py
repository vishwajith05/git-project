import os
import shutil

# Set the folder to clean (here, Desktop)
desktop_path = os.path.join(os.path.expanduser("~"), "Desktop")

# Grouping files based on extension
def organize_files():
    for file_name in os.listdir(desktop_path):
        file_path = os.path.join(desktop_path, file_name)

        # Skip folders
        if os.path.isfile(file_path):
            # Get the extension
            _, ext = os.path.splitext(file_name)
            ext = ext.lower()

            # Set folder name based on type
            if ext in ['.jpg', '.png', '.jpeg', '.gif']:
                folder = "Images"
            elif ext in ['.pdf', '.txt', '.docx', '.pptx']:
                folder = "Documents"
            elif ext in ['.mp4', '.avi', '.mkv']:
                folder = "Videos"
            elif ext in ['.mp3', '.wav']:
                folder = "Music"
            elif ext in ['.zip', '.rar', '.7z']:
                folder = "Archives"
            else:
                folder = "Others"

            # Create destination folder if it doesn't exist
            dest_folder = os.path.join(desktop_path, folder)
            os.makedirs(dest_folder, exist_ok=True)

            # Move the file
            shutil.move(file_path, os.path.join(dest_folder, file_name))

# Run the function
organize_files()
print("Files moved into folders successfully!")