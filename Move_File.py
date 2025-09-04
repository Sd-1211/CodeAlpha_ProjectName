import os
import shutil
source_folder = source_folder = r"C:\Users\Admin\Pictures\Camera Roll"
destination_folder = path = r"C:\Users\Admin\Pictures\Moved_Filess"
if not os.path.exists(destination_folder):
    os.makedirs(destination_folder)
for filename in os.listdir(source_folder):
    if filename.lower().endswith(".jpg"):  
        source_path = os.path.join(source_folder, filename)
        destination_path = os.path.join(destination_folder, filename)

        # Move the file
        shutil.move(source_path, destination_path)
        print(f"Moved: {filename}")
print("✅ All .jpg files have been moved successfully!")