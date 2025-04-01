import zipfile
import os

def compactar_csv(output_csv):
    zip_filename = "output/Teste_NicholasStuartAlmeida.zip"
    
    with zipfile.ZipFile(zip_filename, 'w', zipfile.ZIP_DEFLATED) as zipf:
        zipf.write(output_csv, os.path.basename(output_csv))
        
    if os.path.exists(output_csv):
        os.remove(output_csv)
    
    return zip_filename
