from src.extract_pdf import extract_table_from_pdf
from src.save_data import compactar_csv
import os

def main():
    pdf_path = "data/Anexo_I.pdf"
    output_csv = "output/output.csv"

    os.system('cls' if os.name == 'nt' else 'clear')
    print("Iniciando a extração de dados do PDF...")

    extract_table_from_pdf(pdf_path, output_csv)

    os.system('cls' if os.name == 'nt' else 'clear')
    print("Tabela extraída e salva com sucesso.")

    zip_file = compactar_csv(output_csv)

    os.system('cls' if os.name == 'nt' else 'clear')
    print(f"CSV gerado com sucesso: {output_csv}")
    print(f"Arquivo compactado gerado com sucesso: {zip_file}")

if __name__ == "__main__":
    main()