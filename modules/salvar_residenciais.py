
import pyautogui

def salvar_residenciais(nome_residencial):
    while True:
        try:
            button_listagem = pyautogui.locateOnScreen('fotos/listagem.png', confidence=0.9)
            if button_listagem:
                pyautogui.click(button_listagem)
                break
        except:
            pyautogui.PAUSE = 0.3
            print("Não foi possível encontrar o botão para listar o residencial!")

    while True:
        try:
            button_salvar_listagem = pyautogui.locateOnScreen('fotos/salvar.png', confidence=0.9)
            if button_salvar_listagem:
                pyautogui.press('enter')
                break
        except:
            pyautogui.PAUSE = 0.3
            print("Não foi possível encontrar o botão pequeno de salvar listagem!")
            try:
                button_listagem = pyautogui.locateOnScreen('fotos/listagem.png', confidence=0.9)
                if button_listagem:
                    pyautogui.click(button_listagem)
                    break
            except:
                pyautogui.PAUSE = 0.3
                print("Não foi possível encontrar o botão para listar o residencial! Pela segunda vez")


    while True:
        try:
            pasta_mycart = pyautogui.locateOnScreen('fotos/pasta_mycart.png', confidence=0.8)
            if pasta_mycart:
                pyautogui.doubleClick(pasta_mycart)
                break
        except:
            pyautogui.PAUSE = 0.3
            print("Não foi possível encontrar a pasta 'pasta_mycart'!")

    while True:
        try:
            pasta_automacao = pyautogui.locateOnScreen('fotos/pasta_automacao.png', confidence=0.8)
            if pasta_automacao:
                pyautogui.doubleClick(pasta_automacao)
                break
        except:
            pyautogui.PAUSE = 0.3
            print("Não foi possível encontrar a pasta 'pasta_automacao'!")

    while True:
        try:
            pasta_residenciais = pyautogui.locateOnScreen('fotos/residencial.png', confidence=0.8)
            if pasta_residenciais:
                pyautogui.doubleClick(pasta_residenciais)
                break
        except:
            pyautogui.PAUSE = 0.3
            print("Não foi possível encontrar a pasta 'pasta_residenciais'!")

    while True:
        try:
            label_selecionar_extencao = pyautogui.locateOnScreen('fotos/selecionarExtencao.png', confidence=0.8)
            if label_selecionar_extencao:
                pyautogui.click(label_selecionar_extencao)
                break
        except:
            pyautogui.PAUSE = 0.3
            print("Não foi possível encontrar o label 'label_selecionar_extencao'!")

    while True:
        try:
            opcao_csv = pyautogui.locateOnScreen('fotos/selecionarCsv.png', confidence=0.8)
            if opcao_csv:
                pyautogui.click(opcao_csv)
                break
        except:
            pyautogui.PAUSE = 0.3
            print("Não foi possível encontrar a opcao 'csv'!")

    while True:
        try:
            campo_escrever_nome_condominio = pyautogui.locateOnScreen('fotos/escrevaCondominio.png', confidence=0.8)
            if campo_escrever_nome_condominio:
                pyautogui.click(campo_escrever_nome_condominio)
                pyautogui.PAUSE = 0.3
                pyautogui.write(nome_residencial)
                break
        except:
            pyautogui.PAUSE = 0.3
            print("Não foi possível encontrar o campo para escrever o nome do condominio!")

    while True:
        try:
            button_salvar_residencial = pyautogui.locateOnScreen('fotos/salvar_residencial.png', confidence=0.8)
            if button_salvar_residencial:
                pyautogui.click(button_salvar_residencial)
                break
        except:
            pyautogui.PAUSE = 0.3
            print("Não foi possível encontrar o botao 'salvar'!")

    while True:
        try:
            fechar_aba_listagem = pyautogui.locateOnScreen('fotos/fechar_rar.png', confidence=0.8)
            if fechar_aba_listagem:
                pyautogui.click(fechar_aba_listagem)
                break
        except:
            pyautogui.PAUSE = 0.3
            print("Não foi possível encontrar o botao de fechar a aba de listagem!")

    while True:
        try:
            fechar_aba_pesquisa_residencial = pyautogui.locateOnScreen('fotos/fechar_popups.png', confidence=0.8)
            if fechar_aba_pesquisa_residencial:
                pyautogui.click(fechar_aba_pesquisa_residencial)
                break
        except:
            pyautogui.PAUSE = 0.3
            print("Não foi possível encontrar o botao de fechar a aba de pesquisar residencial!")
