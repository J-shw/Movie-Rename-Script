import os
import shutil

def organize_files(directory):
    print(f'Running through - {directory}')

    video_extensions = (".mp4", ".avi", ".mkv", ".mov", ".wmv", ".flv")

    for filename in os.listdir(directory):
        print(f'- - Checking {filename} - -')
        if os.path.isfile(os.path.join(directory, filename)):

            if filename.lower().endswith(video_extensions):
                file_path = os.path.join(directory, filename)
                filename_split = os.path.splitext(filename)

                folder_name = filename_split[0]
                folder_path = os.path.join(directory, folder_name)

                os.makedirs(folder_path, exist_ok=True)

                new_filename = filename_split[0] + " DVD" + filename_split[1] # Comment out if not setting quality to DVD
                new_file_path = os.path.join(folder_path, new_filename)

                shutil.move(file_path, new_file_path)
            else: print('Not a movie')

if __name__ == "__main__":
    directory_to_organize = "C:\Films"  # Replace with the actual directory
    organize_files(directory_to_organize)