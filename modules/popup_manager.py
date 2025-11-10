# -*- coding: utf-8 -*-
import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk
import threading
import time
from typing import Optional, Callable
import os

class ErrorPopup:
    def __init__(self):
        self.root = None
        self.retry_callback = None
        self.auto_retry_active = False
        self.countdown_active = False
        
    def show_error(self, 
                   error_message: str, 
                   action_attempted: str, 
                   image_path: Optional[str] = None,
                   retry_callback: Optional[Callable] = None):
        """
        Exibe popup de erro com informações detalhadas
        
        Args:
            error_message: Mensagem de erro
            action_attempted: Ação que estava sendo tentada
            image_path: Caminho para imagem relacionada ao erro
            retry_callback: Função para tentar novamente
        """
        self.retry_callback = retry_callback
        
        # Criar nova janela se não existir
        if self.root is None or not self.root.winfo_exists():
            self.root = tk.Tk()
        
        self._setup_window()
        self._create_widgets(error_message, action_attempted, image_path)
        self._start_auto_retry_countdown()
        
        # Manter janela em foco
        self.root.lift()
        self.root.attributes('-topmost', True)
        self.root.mainloop()
    
    def _setup_window(self):
        """Configurar propriedades da janela"""
        self.root.title("🚨 Erro na Automação SRI")
        self.root.geometry("600x500")
        self.root.resizable(False, False)
        
        # Centralizar janela
        self.root.update_idletasks()
        x = (self.root.winfo_screenwidth() // 2) - (600 // 2)
        y = (self.root.winfo_screenheight() // 2) - (500 // 2)
        self.root.geometry(f"600x500+{x}+{y}")
        
        # Configurar estilo
        style = ttk.Style()
        style.theme_use('clam')
    
    def _create_widgets(self, error_message: str, action_attempted: str, image_path: Optional[str]):
        """Criar widgets da interface"""
        main_frame = ttk.Frame(self.root, padding="20")
        main_frame.pack(fill=tk.BOTH, expand=True)
        
        # Título
        title_label = ttk.Label(
            main_frame, 
            text="⚠️ Erro Detectado na Automação",
            font=("Arial", 16, "bold"),
            foreground="red"
        )
        title_label.pack(pady=(0, 20))
        
        # Frame para informações
        info_frame = ttk.LabelFrame(main_frame, text="Detalhes do Erro", padding="10")
        info_frame.pack(fill=tk.X, pady=(0, 20))
        
        # Ação tentada
        ttk.Label(info_frame, text="Ação Tentada:", font=("Arial", 10, "bold")).pack(anchor=tk.W)
        action_text = tk.Text(info_frame, height=2, wrap=tk.WORD, font=("Arial", 9))
        action_text.insert(tk.END, action_attempted)
        action_text.config(state=tk.DISABLED)
        action_text.pack(fill=tk.X, pady=(5, 10))
        
        # Erro
        ttk.Label(info_frame, text="Erro Encontrado:", font=("Arial", 10, "bold")).pack(anchor=tk.W)
        error_text = tk.Text(info_frame, height=3, wrap=tk.WORD, font=("Arial", 9))
        error_text.insert(tk.END, error_message)
        error_text.config(state=tk.DISABLED)
        error_text.pack(fill=tk.X, pady=(5, 0))
        
        # Imagem (se fornecida)
        if image_path and os.path.exists(image_path):
            self._add_image_widget(main_frame, image_path)
        
        # Frame para botões e countdown
        button_frame = ttk.Frame(main_frame)
        button_frame.pack(fill=tk.X, pady=(20, 0))
        
        # Label para countdown
        self.countdown_label = ttk.Label(
            button_frame, 
            text="Tentativa automática em: 5s",
            font=("Arial", 10)
        )
        self.countdown_label.pack(pady=(0, 10))
        
        # Botões
        btn_frame = ttk.Frame(button_frame)
        btn_frame.pack()
        
        retry_btn = ttk.Button(
            btn_frame,
            text="🔄 Tentar Novamente",
            command=self._manual_retry,
            style="Accent.TButton"
        )
        retry_btn.pack(side=tk.LEFT, padx=(0, 10))
        
        stop_btn = ttk.Button(
            btn_frame,
            text="⏹️ Parar Automação",
            command=self._stop_automation
        )
        stop_btn.pack(side=tk.LEFT)
    
    def _add_image_widget(self, parent, image_path: str):
        """Adicionar widget de imagem"""
        try:
            image_frame = ttk.LabelFrame(parent, text="Imagem Relacionada", padding="10")
            image_frame.pack(fill=tk.X, pady=(0, 20))
            
            # Carregar e redimensionar imagem
            pil_image = Image.open(image_path)
            pil_image.thumbnail((300, 200), Image.Resampling.LANCZOS)
            photo = ImageTk.PhotoImage(pil_image)
            
            image_label = ttk.Label(image_frame, image=photo)
            image_label.image = photo  # Manter referência
            image_label.pack()
            
        except Exception as e:
            print(f"Erro ao carregar imagem {image_path}: {e}")
    
    def _start_auto_retry_countdown(self):
        """Iniciar countdown para retry automático"""
        if not self.retry_callback:
            return
            
        self.countdown_active = True
        self.auto_retry_active = True
        
        def countdown():
            for i in range(5, 0, -1):
                if not self.countdown_active:
                    return
                    
                self.countdown_label.config(text=f"Tentativa automática em: {i}s")
                time.sleep(1)
            
            if self.auto_retry_active and self.countdown_active:
                self._auto_retry()
        
        threading.Thread(target=countdown, daemon=True).start()
    
    def _manual_retry(self):
        """Retry manual pelo usuário"""
        self.countdown_active = False
        self.auto_retry_active = False
        self._close_and_retry()
    
    def _auto_retry(self):
        """Retry automático"""
        if self.auto_retry_active:
            self._close_and_retry()
    
    def _close_and_retry(self):
        """Fechar popup e executar retry"""
        if self.root and self.root.winfo_exists():
            self.root.quit()
            self.root.destroy()
        
        if self.retry_callback:
            threading.Thread(target=self.retry_callback, daemon=True).start()
    
    def _stop_automation(self):
        """Parar automação"""
        self.countdown_active = False
        self.auto_retry_active = False
        
        if self.root and self.root.winfo_exists():
            self.root.quit()
            self.root.destroy()
        
        print("Automação interrompida pelo usuário")
        exit()

# Função utilitária para uso fácil
def show_error_popup(error_message: str, 
                    action_attempted: str, 
                    image_path: Optional[str] = None,
                    retry_callback: Optional[Callable] = None):
    """
    Função utilitária para exibir popup de erro
    """
    popup = ErrorPopup()
    popup.show_error(error_message, action_attempted, image_path, retry_callback)