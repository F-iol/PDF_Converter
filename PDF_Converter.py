from PIL import Image
import os
import time

folder_path=input("Paste path to files you want to convert: ")
suffix=('.jpg', '.jpeg', '.png', '.bmp', '.gif', '.webp', '.tiff')  # change/add img types if you need to convert smth else 

try:
    img_files = sorted([
        file for file in os.listdir(folder_path)
        if file.lower().endswith(suffix)
    ])
    if not img_files:
        print('No images found to convert')
        time.sleep(3)
        exit()

    image_list = []

    for file in img_files:
        image_path = os.path.join(folder_path,file)
        img = Image.open(image_path).convert('RGB')
        image_list.append(img)
        
        

    if image_list:
        output_path = os.path.join(folder_path,'Output.pdf')
        try:
            image_list[0].save(output_path,save_all=True,append_images=image_list[1:])
            print("It's saved")
        except Exception:
            print("Saving didnt work")
    else:
        print('Nothing valid to convert')
        
 
except FileNotFoundError:
    print('Folder not found, check if path is correct')
except PermissionError:
    print("Permission denied, if it's still zipped ,unzip folder first")
except Exception as e:
    print(f"What have you done ;-; {e}")

input("Press Enter to exit...")