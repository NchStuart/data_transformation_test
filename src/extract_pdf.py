import pdfplumber
import pandas as pd
import os
from src.process_data import substituir_abreviacoes, formatar_datas

def garantir_pasta_output():
    output_folder = 'output'
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

def extract_table_from_pdf(pdf_path, output_csv):
    garantir_pasta_output()
    
    with pdfplumber.open(pdf_path) as pdf:
        all_data = []
        total_pages = len(pdf.pages)
        
        for page_num in range(total_pages):
            page = pdf.pages[page_num]
            table = page.extract_table()
            
            if table:
                df = pd.DataFrame(table[1:], columns=table[0])
            
                df = df.dropna(axis=1, how='all')
                
                all_data.append(df)
        
        final_df = pd.concat(all_data, ignore_index=True)
        
        final_df = substituir_abreviacoes(final_df)
        
        final_df = formatar_datas(final_df)
        
        final_df.to_csv(output_csv, index=False, encoding='utf-8-sig', sep=';')
