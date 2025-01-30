import pandas as pd

def view_parquet(caminho_parquet):
    df = pd.read_parquet(caminho_parquet, engine='pyarrow')

    print(df.head(10))

if __name__ == "__main__":
    caminho_parquet = 'dados_ixc.parquet'
    view_parquet(caminho_parquet)

