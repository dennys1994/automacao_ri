# -*- coding: utf-8 -*-
"""
Sistema de Automação SRI - Versão Melhorada
Desenvolvido com práticas ágeis e tratamento robusto de erros
"""

import sys
import os

# Adicionar diretórios ao path
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from modules.sri_manager import iniciar_sri
from modules.apagar_planilhas import apagar_planilhas
from modules.procurar_residenciais import procurar_varios_residenciais
#
## Importações dos residenciais (mantidas como estavam)
#from aguasclaras import aguas_claras
#from alphaville import alphaville
#from bosqueveneza import bosque_veneza
#from boulevar import boulevard_felice
#from cityVillage import city_village
#from florestalago import floresta_do_lago
#from franciscogorski import francisco_gorski
#from itaqui import itaqui
#from mestre import mestre
#from michigan import michigan
#from oregon import oregon
#from passauna import passauna
#from paysagedipiero import paysage_di_piero
#from toscana import toscana
#from veredas import veredas
#from verona import veronna
#from fontanaMaggiore import fontanaMaggiore
#from fontanaTrevi import fontanaTrevi
#from villaAlvoredo import villa_alvoredo
#from vittimachado import vitti_machado_ii
#from salvar_winrar import salvar_winrar

def main():
    """Função principal da automação"""
    print("🤖 Iniciando Automação SRI - Versão Melhorada")
    print("=" * 50)
    
    try:
        # Etapa 1: Inicializar SRI
        print("\n📋 Etapa 1: Inicializando SRI...")
        iniciar_sri()
        
        # Etapa 2: Preparar planilhas
        print("\n📋 Etapa 2: Preparando planilhas...")
        apagar_planilhas()
        
        ## Etapa 3: Procurar residenciais
        print("\n📋 Etapa 3: Procurando residenciais...")
        procurar_varios_residenciais()
        #
        ## Etapa 4: Processar residenciais
        #print("\n📋 Etapa 4: Processando residenciais...")
        #residenciais = [
        #    ("Fontana Maggiore", fontanaMaggiore),
        #    ("Fontana Trevi", fontanaTrevi),
        #    ("Águas Claras", aguas_claras),
        #    ("Alphaville", alphaville),
        #    ("Bosque Veneza", bosque_veneza),
        #    ("Boulevard Felice", boulevard_felice),
        #    ("City Village", city_village),
        #    ("Floresta do Lago", floresta_do_lago),
        #    ("Francisco Gorski", francisco_gorski),
        #    ("Itaqui", itaqui),
        #    ("Mestre", mestre),
        #    ("Michigan", michigan),
        #    ("Oregon", oregon),
        #    ("Passauna", passauna),
        #    ("Paysage Di Piero", paysage_di_piero),
        #    ("Toscana", toscana),
        #    ("Veredas", veredas),
        #    ("Veronna", veronna),
        #    ("Villa Alvoredo", villa_alvoredo),
        #    ("Vitti Machado II", vitti_machado_ii),
        #]
        #
        #for nome, funcao in residenciais:
        #    print(f"  🏘️ Processando: {nome}")
        #    funcao()
        #
        ## Etapa 5: Salvar resultados
        #print("\n📋 Etapa 5: Salvando resultados...")
        #salvar_winrar()
        
        print("\n✅ Automação concluída com sucesso!")
        print("=" * 50)
        
    except KeyboardInterrupt:
        print("\n⏹️ Automação interrompida pelo usuário")
    except Exception as e:
        print(f"\n❌ Erro crítico na automação: {e}")
        print("Verifique os logs para mais detalhes")

if __name__ == "__main__":
    main()