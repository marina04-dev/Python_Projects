import os
import shutil


# define file categories
FILE_CATEGORIES = {
    "Images": [".jpg", ".jpeg", ".png", ".gif", ".bmp", ".tiff"],
    "Videos": [".mp4", ".mkv", ".flv", ".avi", ".mov"],
    "Documents": [".pdf", ".doc", ".docx", ".txt", ".ppt", ".pptx", ".xls", ".xlsx"],
    "Audio": [".mp3", ".wav", ".aac", ".flac"],
    "Archives": [".zip", ".rar", ".7z", ".tar", ".gz"],
    "Data": [".csv", ".json", ".xml"],
    "Others": []
}

# function which organizes files of the directory path given
def organize_files(directory):
    # 1. Check for valid directory input
    if not os.path.isdir(directory):
        print("Error: {directory} is not a valid directory.")
        return

    # 2. Create folders for each category if they don't already exist
    for category in FILE_CATEGORIES:
        folder_path = os.path.join(directory, category)
        os.makedirs(folder_path, exist_ok=True)

    # 3. Move files into the appropriate folder
        for filename in os.listdir(directory):
            file_path = os.path.join(directory, filename)

            # 3.i. Skip if it's a directory
            if os.path.isdir(file_path):
                continue

            # 3.ii. Check file extension and move to
            # the corresponding folder
            file_moved = False
            for category, extensions in FILE_CATEGORIES.items():
                if any(filename.lower().endswith(ext) for ext in extensions):
                    shutil.move(file_path, os.path.join(directory, category, filename))
                    file_moved = True
                    break

            # 3.iii. Move to "Others" if no match
            if not file_moved:
                shutil.move(file_path, os.path.join(directory, "Others", filename))

        print(f"Files in '{directory}' have been organized successfully!")
        
        
directory_to_organize = input("Enter the directory path to organize: ")
organize_files(directory_to_organize)
