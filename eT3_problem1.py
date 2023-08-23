import os
import shutil
import datetime
import pandas as pd
import argparse

def copy_image(source_path, destination_folder, image_counter):
    new_filename = f"image{image_counter}.jpg"
    destination_path = os.path.join(destination_folder, new_filename)
    shutil.copy(source_path, destination_path)
    return new_filename

def collect_image_details(source_path):

    image_size = os.path.getsize(source_path) / (1024)  # Convert to Kilobytes
    modification_time = datetime.datetime.fromtimestamp(os.path.getmtime(source_path))

    formatted_size = f"{image_size:.2f} KB"
    formatted_modification_time = modification_time.strftime('%a %b %d %H:%M:%S %Y')

    return formatted_size, formatted_modification_time


def main(source_folder, destination_folder):
    # Path to the main folder containing sub-folders
   # source_folder = '/home/mahmoudalaa/Desktop/eT3_assessment/problem1/dairies/'
    # Path to the destination folder where you want to store all images
   # destination_folder = '/home/mahmoudalaa/Desktop/images_dataset/'

    image_counter = 1
    data = []
    for root, _, files in os.walk(source_folder):
        for file in files:
            if file.lower().endswith((".jpg", ".png")):
                source_path = os.path.join(root, file)
                
                new_filename = copy_image(source_path, destination_folder, image_counter)
                image_size, modification_time = collect_image_details(source_path)
                
                data.append({
                    "Image": new_filename,
                    "Image Size": image_size,
                    "Image Modification Date": modification_time
                })
                
                image_counter += 1

    df = pd.DataFrame(data)
    print(df)
    return df


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Copy images from source folder to destination folder and collect details.")
    parser.add_argument("source_folder", help="Path to the source folder containing images")
    parser.add_argument("destination_folder", help="Path to the destination folder where images will be copied")
    args = parser.parse_args()
    
    result_df = main(args.source_folder, args.destination_folder)