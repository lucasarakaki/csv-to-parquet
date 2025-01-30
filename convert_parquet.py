import pandas as pd

def convert_to_parquet(input_csv, output_parquet):
    
    df = pd.read_csv(input_csv, delimiter=';', on_bad_lines='skip')
    
    
    df.to_parquet(output_parquet, engine='pyarrow') 

    print(f'Arquivo {input_csv} convertido para {output_parquet} com sucesso!')

if __name__ == "__main__":
    input_csv = 'dados.csv'  # Caminho para arquivo CSV
    output_parquet = 'dados_ixc.parquet'  # Caminho para o arquivo Parquet

    convert_to_parquet(input_csv, output_parquet)

