from config import carregar_ou_criar_config
from checklist import iniciar_checklist
import customtkinter as ctk
import requests
import tkinter.messagebox as mbox
import webbrowser
from licenca import verificar_licenca  # Importa a função de verificação de licença

ctk.set_appearance_mode("dark")  # Tema fixo escuro
ctk.set_default_color_theme("blue")

# Função para verificar se há uma atualização
def verificar_atualizacao():
    try:
        # URL do arquivo versao.json no GitHub
        response = requests.get("https://raw.githubusercontent.com/SEU_USUARIO/checklist-programa/main/checklist/versao.json", timeout=5)
        dados = response.json()

        # Versão atual do programa
        versao_atual = "1.0.0"  # Atualize essa versão com a versão atual do seu programa
        if dados["versao"] != versao_atual:
            # Se a versão remota for diferente, avisa o usuário
            msg = f"Nova versão disponível: {dados['versao']}\n\n{dados['changelog']}\n\nDeseja abrir o link de download?"
            if mbox.askyesno("Atualização disponível", msg):
                # Abre o link de download da nova versão
                webbrowser.open(dados["link_download"])
    except Exception as e:
        print(f"Erro ao verificar atualização: {e}")

# Função principal para iniciar o programa
def iniciar_programa():
    # Verifica a licença antes de qualquer coisa
    if not verificar_licenca():  # Se a licença for inválida, não continua
        mbox.showerror("Erro de Licença", "A licença do programa não é válida. O programa será fechado.")
        exit()

    # Verifica se há uma atualização antes de iniciar o programa
    verificar_atualizacao()

    # Carrega a configuração (do arquivo config)
    config = carregar_ou_criar_config()

    # Inicia o checklist com a configuração carregada
    iniciar_checklist(config)

if __name__ == "__main__":
    # Chama a função para iniciar o programa
    iniciar_programa()
