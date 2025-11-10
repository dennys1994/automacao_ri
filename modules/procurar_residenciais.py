import pyautogui
from modules.salvar_residenciais import salvar_residenciais
from modules.localizar_e_clicar import localizar_e_clicar
import time

def procurar_residenciais(nome_residencial, especifico=False, contenha=False):
    # Navegação inicial
    if not localizar_e_clicar('fotos/indicadores.png', "Aba Indicadores", reiniciar_com_esc=True):
        return
    if not localizar_e_clicar('fotos/real.png', "Opção Real na aba Indicadores", reiniciar_com_esc=True):
        return
    if not localizar_e_clicar('fotos/consultar.png', "Opção Consultar", reiniciar_com_esc=True):
        return

    # Abrindo a janela de matrícula
    coordenadas_matricula = localizar_e_clicar('fotos/matricula-selecao.png', "Label Matrículas para selecionar opções", reiniciar_com_esc=True)
    if not coordenadas_matricula:
        return

    # Clique no centro da imagem localizada
    input("Pressione [ESPAÇO] e depois ENTER para continuar...")
    try:
        print("🖱️ Clicando no centro da imagem localizada para exibir opções específicas...")
        x, y = pyautogui.position()
        pyautogui.moveTo(x + 190, y + 130, duration=0.1)
        pyautogui.PAUSE = 0.3
        pyautogui.click()
    except Exception as e:
        print(f"⚠️ Erro ao clicar no centro da imagem: {e}")
        return

    # Selecionando opções específicas ou "contenha"
    if especifico:
        if not localizar_e_clicar('fotos/condominio.png', "Opção Condomínio (Específico)", reiniciar_com_esc=True):
            return
    if contenha:
        if not localizar_e_clicar('fotos/condominioContenha.png', "Opção Condomínio (Contenha)", reiniciar_com_esc=True):
            return

    # Selecionando o campo para escrever o nome do residencial
    if not localizar_e_clicar('fotos/escrevaCondo.png', "Campo para selecionar o condomínio", reiniciar_com_esc=True):
        return

    # Escrevendo o nome do residencial
    try:
        print(f"🖊️ Escrevendo o nome do residencial: {nome_residencial}")
        pyautogui.write(nome_residencial, interval=0.1)
        time.sleep(0.5)
    except Exception as e:
        print(f"⚠️ Erro ao escrever o nome do residencial: {e}")
        return

    # Clicando no botão pesquisar
    if not localizar_e_clicar('fotos/pesquisar.png', "Botão Pesquisar", reiniciar_com_esc=True):
        return

    print("✅ Residencial extraído com sucesso! Chamando função para salvar.")
    salvar_residenciais(nome_residencial)

def procurar_varios_residenciais():
    # Lista de residenciais para busca
    residenciais_especificos = [
        "RESIDENCIAL AGUAS CLARAS",
        "BOSQUE VENEZA",
        "CITY VILLAGE RESIDENCE",
        "RESIDENCIAL RESERVA FLORESTA DO LAGO",
        "RESIDENCIAL FRANCISCO GORSKI",
        "RESIDENCIAL ITAQUI",
        "RESIDENCIAL MESTRE",
        "RESIDENCIAL MICHIGAN",
        "RESIDENCIAL OREGON",
        "RESIDENCIAL PAYSAGE DI PIERO",
        "RESIDENCIAL TOSCANA",
        "VERDE PASSAUNA",
        "RESIDENCIAL VEREDAS",
        "RESIDENCIAL VERONA",
        "RESIDENCIAL VILLA ALVOREDO",
        "RESIDENCIAL VITTI MACHADO II",
        "RESIDENCIAL FONTANA DI TREVI",
        "RESIDENCIAL FONTANA MAGGIORE"
    ]

    residenciais_contenha = [
        "BOULEVARD FELICE",
        "ALPHAVILLE PARANA"
    ]

    # Chamando a função para os residenciais que contenham o nome
    for residencial in residenciais_contenha:
        procurar_residenciais(residencial, contenha=True)

        # Chamando a função para os residenciais específicos
    for residencial in residenciais_especificos:
        procurar_residenciais(residencial, especifico=True)