# -*- coding: utf-8 -*-
import pyautogui
import subprocess
import time
import os
from typing import Optional
from .popup_manager import show_error_popup

class SRIManager:
    def __init__(self):
        self.exe_path = r"M:\Mactus\Sistema\Sri.exe"
        self.max_attempts = 3
        self.wait_time = 2
        
    def iniciar_sri(self):
        """Iniciar SRI com tratamento de erros melhorado"""
        print("🚀 Iniciando SRI...")
        
        try:
            self._launch_sri_executable()
            self._wait_for_login_form()
            self._perform_login()
            self._close_popups()
            print("✅ SRI iniciado com sucesso!")
            
        except Exception as e:
            self._handle_error(f"Erro geral ao iniciar SRI: {str(e)}", "Inicialização do SRI")
    
    def _launch_sri_executable(self):
        """Lançar executável do SRI"""
        try:
            if not os.path.exists(self.exe_path):
                raise FileNotFoundError(f"Executável não encontrado: {self.exe_path}")
            
            subprocess.Popen(self.exe_path)
            print("📂 Executável SRI lançado")
            time.sleep(3)  # Aguardar inicialização
            
        except Exception as e:
            self._handle_error(
                f"Erro ao lançar executável: {str(e)}", 
                f"Tentativa de abrir: {self.exe_path}"
            )
    
    def _wait_for_login_form(self):
        """Aguardar formulário de login aparecer"""
        print("⏳ Aguardando formulário de login...")
        
        login_form_image = 'fotos/formulario_login.png'  # Sua nova imagem
        attempts = 0
        max_wait_attempts = 15 # 30 tentativas = ~1 minuto
        
        while attempts < max_wait_attempts:
            try:
                form_location = pyautogui.locateOnScreen(login_form_image, confidence=0.8)
                if form_location:
                    print("✅ Formulário de login detectado!")
                    return
                    
            except pyautogui.ImageNotFoundException:
                pass
            except Exception as e:
                print(f"⚠️ Erro ao procurar formulário: {e}")
            
            attempts += 1
            time.sleep(2)
            print(f"🔍 Tentativa {attempts}/{max_wait_attempts} - Procurando formulário...")
        
        # Se chegou aqui, não encontrou o formulário
        self._handle_error(
            "Formulário de login não foi encontrado após 1 minuto de espera",
            "Aguardando formulário de login aparecer",
            login_form_image
        )
    
    def _perform_login(self):
        """Realizar login no SRI"""
        print("🔐 Realizando login...")
        
        campo_nome_image = 'fotos/campo_nome_sri.png'
        
        try:
            campo_nome = pyautogui.locateOnScreen(campo_nome_image, confidence=0.8)
            if not campo_nome:
                raise Exception("Campo de nome não encontrado")
            
            # Clicar no campo e inserir dados
            pyautogui.click(campo_nome)
            time.sleep(0.5)
            
            # Limpar campo antes de digitar
            pyautogui.hotkey('ctrl', 'a')
            time.sleep(0.2)
            
            # Digitar usuário
            pyautogui.write('Automa', interval=0.1)
            pyautogui.press('enter')
            time.sleep(0.5)
            
            # Digitar senha
            pyautogui.write('Cartorio123@', interval=0.1)
            pyautogui.press('enter')
            
            print("✅ Credenciais inseridas")
            time.sleep(2)
            
        except Exception as e:
            self._handle_error(
                f"Erro ao realizar login: {str(e)}",
                "Preenchimento de credenciais de login",
                campo_nome_image
            )
    
    def _close_popups(self):
        """Fechar popups que aparecem após login"""
        print("🗂️ Fechando popups...")
        
        # Caminho para a imagem do popup
        popup_image = 'fotos/popup.png'
        popups_closed = 0
        max_popup_attempts = 5
        
        # Aguardar 10 segundos para garantir que o SRI foi carregado
        print("⏳ Aguardando 10 segundos para garantir que o SRI foi carregado...")
        time.sleep(10)
        
        for attempt in range(max_popup_attempts):
            try:
                print(f"🔍 Tentativa {attempt + 1}/{max_popup_attempts} de localizar popup...")
                popup_location = pyautogui.locateOnScreen(popup_image, confidence=0.8)
                
                if popup_location:
                    print(f"✅ Popup localizado! Fechando popup na posição: {popup_location}")
                    pyautogui.click(popup_location)
                    popups_closed += 1
                    time.sleep(1)  # Pausa para evitar cliques consecutivos rápidos
                else:
                    print("ℹ️ Nenhum popup encontrado nesta tentativa.")
                    break  # Não há mais popups, sair do loop
                    
            except Exception as e:
                print(f"⚠️ Erro ao fechar popup: {e}")
                break  # Interromper em caso de erro inesperado
        
        if popups_closed > 0:
            print(f"✅ {popups_closed} popup(s) fechado(s) com sucesso!")
        else:
            print("ℹ️ Nenhum popup foi encontrado após todas as tentativas.")
            
    def _handle_error(self, error_message: str, action_attempted: str, image_path: Optional[str] = None):
        """Tratar erros com popup"""
        print(f"❌ ERRO: {error_message}")
        
        def retry_action():
            print("🔄 Tentando novamente...")
            self.iniciar_sri()
        
        show_error_popup(
            error_message=error_message,
            action_attempted=action_attempted,
            image_path=image_path,
            retry_callback=retry_action
        )

# Função para manter compatibilidade
def iniciar_sri():
    """Função wrapper para manter compatibilidade com código existente"""
    sri_manager = SRIManager()
    sri_manager.iniciar_sri()