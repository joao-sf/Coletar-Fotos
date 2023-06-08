import os
import shutil
import pandas as pd

# Obter o caminho absoluto do diretório atual
diretorio_atual = os.path.dirname(os.path.abspath(__file__))

# Construir o caminho completo da planilha
caminho_planilha = os.path.join(diretorio_atual, 'Lote.xlsx')

# Ler a planilha e obter os dados da primeira coluna
planilha = pd.read_excel(caminho_planilha)
primeira_coluna = planilha.iloc[:, 0]

# Diretórios de origem e destino dos arquivos
diretorio_origem = os.path.join(diretorio_atual, 'fotos')
diretorio_destino = diretorio_atual

# Adicionar coluna de status na planilha
planilha['Status'] = ''

# Percorrer os valores da primeira coluna
for i, valor in enumerate(primeira_coluna):
    # Converter o valor para string
    valor_str = str(valor)


    # Obter o nome do arquivo correspondente ao valor
    nome_arquivo = next((arquivo for arquivo in os.listdir(diretorio_origem) if arquivo.startswith(valor_str)), None)

    if nome_arquivo:
        # Caminho completo do arquivo de origem
        caminho_origem = os.path.join(diretorio_origem, nome_arquivo)

        # Caminho completo do arquivo de destino
        caminho_destino = os.path.join(diretorio_destino, nome_arquivo)

        # Mover o arquivo para a pasta de destino
        shutil.move(caminho_origem, caminho_destino)

        # Atualizar o status na planilha
        planilha.at[i, 'Status'] = 'Encontrado'
    else:
        # Atualizar o status na planilha
        planilha.at[i, 'Status'] = 'Não encontrado'

# Salvar a planilha atualizada
caminho_planilha_atualizada = os.path.join(diretorio_atual, 'Lote_atualizada.xlsx')
planilha.to_excel(caminho_planilha_atualizada, index=False)