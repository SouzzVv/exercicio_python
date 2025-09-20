import pandas as pd
import matplotlib as mp
import kagglehub

# Download latest version
file_path = 'C:\\Users\\Aluno\\Desktop\\vini - projeto\\archive\\goalscorers.csv'

df = pd.read_csv(file_path)

df['minImpar'] = df['minute']%2!=0


for index, linha in df.iterrows():
    if linha['minImpar']:
        print(f'index: {index}, nome:{linha['scorer']}, minuto:{linha['minute']}')