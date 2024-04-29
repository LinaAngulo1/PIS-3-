import os

# Carpeta principal que contiene las carpetas de cada sujeto
carpeta_principal = "C:\\Users\\ORMAN\\Desktop\\cambio de nombre\\BraTS2021_Training_Data"

# Archivo de salida para los archivos faltantes
archivo_faltantes = "C:\\Users\\ORMAN\\Desktop\\cambio de nombre\\faltantes.txt"

# Lista de segmentos a verificar
segmentos_verificar = ["segmento_1.nii.gz", "segmento_2.nii.gz", "segmento_4.nii.gz"]

# Función para verificar la existencia de archivos en una carpeta
def verificar_archivos_en_carpeta(carpeta):
    archivos_encontrados = os.listdir(carpeta)
    faltantes = [seg for seg in segmentos_verificar if seg not in archivos_encontrados]
    return faltantes

# Recorrer cada carpeta de sujeto en la carpeta principal
with open(archivo_faltantes, "w") as f:
    for sujeto in os.listdir(carpeta_principal):
        ruta_sujeto = os.path.join(carpeta_principal, sujeto)
        
        # Verificar si la ruta es una carpeta
        if os.path.isdir(ruta_sujeto):
            carpeta_seg = os.path.join(ruta_sujeto, "seg")
            if os.path.exists(carpeta_seg):
                faltantes = verificar_archivos_en_carpeta(carpeta_seg)
                if faltantes:
                    f.write(f"Archivos faltantes en {sujeto}: {', '.join(faltantes)}\n")
            else:
                f.write(f"No se encontró la carpeta 'seg' en {sujeto}\n")
