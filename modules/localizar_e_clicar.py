import pyautogui
import time

def localizar_e_clicar(imagem, descricao, tentativas=5, pausa=0.5, reiniciar_com_esc=False):
    """
    Localiza e clica em uma imagem na tela.
    
    Args:
        imagem (str): Caminho para a imagem a ser localizada.
        descricao (str): Descrição da ação para logs.
        tentativas (int): Número máximo de tentativas.
        pausa (float): Tempo de espera entre tentativas.
        reiniciar_com_esc (bool): Pressionar 'ESC' antes de tentar novamente.
    
    Returns:
        bool: True se a imagem foi encontrada e clicada, False caso contrário.
    """
    for tentativa in range(1, tentativas + 1):
        try:
            print(f"🔍 Tentativa {tentativa}/{tentativas} para localizar: {descricao}")
            localizacao = pyautogui.locateOnScreen(imagem, confidence=0.8)
            if localizacao:
                print(f"✅ {descricao} localizada! Clicando na posição: {localizacao}")
                pyautogui.click(localizacao)
                time.sleep(pausa)  # Pausa após o clique
                return True
            else:
                print(f"⚠️ {descricao} não encontrada. Tentando novamente...")
        except Exception as e:
            print(f"⚠️ Erro ao localizar {descricao}: {e}")
        
        # Reiniciar com 'ESC' se configurado
        if reiniciar_com_esc:
            print("🔄 Pressionando 'ESC' para reiniciar...")
            pyautogui.press('esc')
            time.sleep(pausa)
    
    print(f"❌ Não foi possível localizar: {descricao} após {tentativas} tentativas.")
    return False