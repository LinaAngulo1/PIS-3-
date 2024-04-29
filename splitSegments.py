import os
import nibabel as nib
import numpy as np

'''
Este script permite tomar un archivo que contenga varias máscaras de segmentación y separarlas en archivos separados,
en este caso se ignora la máscara de la porción del cerebro sano debido a que no se extraerán características de ese segmento.
'''

# Carpeta principal que contiene las carpetas de cada sujeto
carpeta_principal = "C:\\Users\\ORMAN\\Desktop\\cambio de nombre\\BraTS2021_Training_Data"

# Nombre de la carpeta que contendrá las segmentaciones individuales
carpeta_segmentaciones = "seg"

# Recorrer cada carpeta de sujeto en la carpeta principal
for sujeto in os.listdir(carpeta_principal):
    ruta_sujeto = os.path.join(carpeta_principal, sujeto)
    
    # Verificar si la ruta es una carpeta
    if os.path.isdir(ruta_sujeto):
        print(f"Procesando sujeto: {sujeto}")
        
        # Carpeta de salida para las segmentaciones individuales
        carpeta_salida = os.path.join(ruta_sujeto, carpeta_segmentaciones)
        os.makedirs(carpeta_salida, exist_ok=True)
        
        # Recorrer los archivos dentro de la carpeta de cada sujeto
        for archivo in os.listdir(ruta_sujeto):
            ruta_archivo = os.path.join(ruta_sujeto, archivo)
            
            # Comprobar si el archivo es una imagen de segmentación
            if archivo.endswith(".nii.gz") and "seg" in archivo:
                # Cargar la máscara de segmentación
                mascara_segmentacion = nib.load(ruta_archivo)
                
                # Obtener los datos de la máscara como un array NumPy
                datos_mascara = mascara_segmentacion.get_fdata()
                
                # Obtener los valores únicos presentes en la máscara de segmentación
                segmentos_unicos = np.unique(datos_mascara)
                
                # Crear una nueva imagen Nifti para cada segmento y guardarlas
                for idx_segmento in segmentos_unicos:
                    # No guardar el segmento con valor cero
                    if idx_segmento == 0:
                        continue
                    
                    # Crear una máscara para el segmento actual
                    mascara_segmento = np.zeros_like(datos_mascara)
                    mascara_segmento[datos_mascara == idx_segmento] = 1
                    
                    # Convertir la máscara a un objeto Nifti
                    mascara_segmento_nifti = nib.Nifti1Image(mascara_segmento, mascara_segmentacion.affine)
                    
                    # Guardar la máscara segmentada como un archivo nifti
                    nombre_archivo = f"segmento_{int(idx_segmento)}.nii.gz"
                    ruta_salida = os.path.join(carpeta_salida, nombre_archivo)
                    nib.save(mascara_segmento_nifti, ruta_salida)

                    print(f'Se ha guardado el segmento {int(idx_segmento)} de {archivo} en {ruta_salida}')
