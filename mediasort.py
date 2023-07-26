import shutil
import os

def move_files_by_type(source_folder, destination_folder, media_type):
    media_extensions = {
        'image': ['.jpg', '.jpeg', '.png', '.gif', '.bmp', '.svg'],
        'video': ['.mp4', '.avi', '.mov', '.mkv', '.wmv', '.flv'],
        'audio': ['.mp3', '.wav', '.ogg', '.aac', '.flac']
    }

    if media_type not in media_extensions:
        print("Invalid media type. Choose from 'image', 'video', or 'audio'.")
        return

    if not os.path.exists(destination_folder):
        os.mkdir(destination_folder)

    for filename in os.listdir(source_folder):
        ext = os.path.splitext(filename)[1].lower()

        if ext in media_extensions[media_type]:
            source_path = os.path.join(source_folder, filename)
            destination_path = os.path.join(destination_folder, filename)

            try:
                shutil.move(source_path, destination_path)
                print(f"Moved: {filename} -> {destination_folder}")
            except shutil.Error as e:
                print(f"Error while moving {filename}: {e}")

if __name__ == "__main__":
    source_folder = input("Enter the path to the source folder: ")
    destination_folder = input("Enter the path to the destination folder: ")
    media_type = input("Enter the media type ('image', 'video', or 'audio'): ")

    move_files_by_type(source_folder, destination_folder, media_type)