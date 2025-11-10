
import os

def apagar_planilhas():
    caminho_planilhas = 'RESIDENCIAIS'
    for file in os.listdir(caminho_planilhas):
        file_delete = os.path.join(caminho_planilhas, file)
        os.remove(file_delete)