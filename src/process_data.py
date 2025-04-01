import pandas as pd

def substituir_abreviacoes(df):
    legenda = {
        'OD': 'Seg. Odontológica',
        'AMB': 'Seg. Ambulatorial'
    }
    
    df.columns = df.columns.map(lambda x: legenda.get(x, x))
    
    if 'Seg. Odontológica' in df.columns:
        df['Seg. Odontológica'] = df['Seg. Odontológica'].replace(legenda)
    
    if 'Seg. Ambulatorial' in df.columns:
        df['Seg. Ambulatorial'] = df['Seg. Ambulatorial'].replace(legenda)
    
    return df

def formatar_datas(df):
    data_columns = ['VIGÊNCIA']
    
    for col in data_columns:
        if col in df.columns:
            df[col] = pd.to_datetime(df[col], errors='coerce', dayfirst=True).dt.strftime('%d/%m/%Y')
    
    return df
