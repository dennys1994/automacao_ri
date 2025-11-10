# -*- coding: utf-8 -*-
import os
from typing import Optional

def validate_image_path(image_path: str) -> bool:
    """Validar se o caminho da imagem existe e é válido"""
    if not image_path:
        return False
    
    if not os.path.exists(image_path):
        print(f"⚠️ Imagem não encontrada: {image_path}")
        return False
    
    valid_extensions = ['.png', '.jpg', '.jpeg', '.bmp', '.gif']
    file_extension = os.path.splitext(image_path)[1].lower()
    
    if file_extension not in valid_extensions:
        print(f"⚠️ Formato de imagem não suportado: {file_extension}")
        return False
    
    return True

def get_image_path(relative_path: str) -> Optional[str]:
    """Obter caminho absoluto da imagem"""
    base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    full_path = os.path.join(base_dir, relative_path)
    
    if validate_image_path(full_path):
        return full_path
    
    return None