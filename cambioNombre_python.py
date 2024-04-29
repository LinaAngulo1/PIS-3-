import os

# Obtener la ruta absoluta de la carpeta principal
script_dir = os.path.dirname(os.path.abspath(__file__))
main_folder = os.path.join(script_dir, 'BraTS2021_Training_Data')

for root, dirs, files in os.walk(main_folder):
    for dir_name in dirs:
        new_dir_name = dir_name.replace('sub_', 'sub-')
        os.rename(os.path.join(root, dir_name), os.path.join(root, new_dir_name))

    print(files)
    for file_name in files:
        print(file_name)
        new_file_name = file_name.replace('sub_', 'sub-').replace('t1', 'T1w').replace('t1ce', 'T1ce').replace('t2', 'T2w').replace('flair', 'FLAIR')
        print(new_file_name)
        os.rename(os.path.join(root, file_name), os.path.join(root, new_file_name))