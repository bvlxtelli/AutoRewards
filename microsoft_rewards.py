from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from datetime import datetime
import time
import random
import subprocess
import os
import sys
import json

# Configuração de nome de usuário e primeiro acesso -------------------------------------------------

# Diretório seguro para salvar a configuração
CONFIG_DIR = os.path.join(os.path.expanduser("~"), ".msrwd")  # Linux/Mac: ~/.meuapp | Windows: C:\Users\Nome\.msrwd
CONFIG_FILE = os.path.join(CONFIG_DIR, "config.json")

# Criar o diretório se não existir
if not os.path.exists(CONFIG_DIR):
    os.makedirs(CONFIG_DIR)

# Função para carregar configurações
def carregar_config():
    if os.path.exists(CONFIG_FILE):
        with open(CONFIG_FILE, "r") as file:
            return json.load(file)
    return {}

# Função para salvar configurações
def salvar_config(config):
    with open(CONFIG_FILE, "w") as file:
        json.dump(config, file, indent=4)

# Tenta carregar o nome de usuário salvo
config = carregar_config()
nome_de_usuario = config.get("nome_de_usuario", "")
primeiro_acesso = config.get("primeiro_acesso","")

TEMP_DIR = r"C:\\%appdata%\\.msrwd\\temp"

caminho_do_chromedriver = os.path.join(os.path.dirname(__file__), "chromedriver.exe")

# Executa esse processo em segundo plano

subprocess.Popen([caminho_do_chromedriver])

print(" -----------------------------------------------------------------------------------------------------------------\n")

# Inicia o App ------------------------------------------------------------------------------------------

print(" -----------------------------------------------------------------------------------------------------------------\n")
print("▄████▄░██░░░██░████████░▄█████▄░▄██████░▄█████░▄████▄░█████▄░▄█████░██░░░██")
print("██░░██░██░░░██░░░░██░░░░██░░░██░██░░░░░░██░░░░░██░░██░██░░██░██░░░░░██░░░██")
print("██░░██░██░░░██░░░░██░░░░██░░░██░▀█████▄░█████░░██░░██░█████▀░██░░░░░███████")
print("██████░██░░░██░░░░██░░░░██░░░██░░░░░░██░██░░░░░██████░██░░██░██░░░░░██░░░██")
print("██░░██░▀█████▀░░░░██░░░░▀█████▀░██████▀░▀█████░██░░██░██░░██░▀█████░██░░░██")
print("░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░")
print("▄██▄▄██▄░▄██████░░░░░░░░█████▄░▄█████░██░██░██░▄████▄░█████▄░██████▄░▄██████")
print("██░██░██░██░░░░░░░░░░░░░██░░██░██░░░░░██░██░██░██░░██░██░░██░██░░░██░██░░░░░")
print("██░██░██░▀█████▄░░░░░░░░█████▀░█████░░██░██░██░██░░██░█████▀░██░░░██░▀█████▄")
print("██░██░██░░░░░░██░██████░██░░██░██░░░░░██░██░██░██████░██░░██░██░░░██░░░░░░██")
print("██░██░██░██████▀░░░░░░░░██░░██░▀█████░▀██▀▀██▀░██░░██░██░░██░██████▀░██████▀")
print("░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░")
print("\n -------------------------------------------------------------------------------------------------   By BVLXTELLI\n")

time.sleep(3)

print("\n -----------------------------------------------------------------------------------------------------------------\n")

# Configuração do WebDriver para usar o perfil do Chrome

options = webdriver.ChromeOptions()

if not nome_de_usuario:

    # Se não tiver nome de usuário registrado solicita um

    nome_de_usuario = input('Digite CORRETAMENTE seu nome de usuário do PC: ').strip()

    # Confirmaçao do nome de usuário

    confirmacao_nome_de_usuario = input('Digitou CORRETAMENTE? [S] ou [N].').strip().lower()

    # Enquanto o usuário não confirmar o usuário corretamente, não sai do lugar
    
    while confirmacao_nome_de_usuario != 's':
        input_nome_de_usuario = input('Digite CORRETAMENTE seu nome de usuário do PC:')
        nome_de_usuario = input_nome_de_usuario
        confirmacao_nome_de_usuario = input('Agora foi? [S] ou [N]' ).strip().lower()
    
    # Confirmação da confirmação
    
    confirmacao_nome_de_usuario = input(f'Então posso te chamar de {nome_de_usuario.upper()}? [S] ou [N].').strip().lower()

    # Salva o nome de usuário definido

    config["nome_de_usuario"] = nome_de_usuario
    salvar_config(config)

# Dá boas vindas ao usuário

print("\n -----------------------------------------------------------------------------------------------------------------\n")
print(f'\n Boa, {nome_de_usuario.upper()}. Vamo dale, então! \n')
print("\n -----------------------------------------------------------------------------------------------------------------\n")

time.sleep(2)

# Entende se é o primeiro acesso ou não

if primeiro_acesso != 'n':

    # Se for o primeiro acesso, ele configura pra que não se repita da próxima vez

    primeiro_acesso = input('É seu primeiro acesso? [S] ou [N].\nLembre-se que sua conta precisa estar logada no navegador que vamos abrir...').strip().lower()
    config["primeiro_acesso"] = 'n'

    if primeiro_acesso == 's':
        config["primeiro_acesso"] = 'n'

    salvar_config(config)

# Busca as configs do Chrome com a variável do nome de usuário

options.add_argument(f"user-data-dir=C:\\Users\\{nome_de_usuario}\\AppData\\Local\\Google\\Chrome\\User Data\\Default\\Default")  
options.add_argument("profile-directory=Default")  # Ou o nome do perfil, se não for "Default"

print("\n -----------------------------------------------------------------------------------------------------------------\n")

# Libera a tela pro usuário configurar a conta Microsoft

if primeiro_acesso != 'n':
    print('\n Você tem [3 minutos] pra logar na sua conta Microsoft neste navegador que vai abrir... \n')
    print("\n -----------------------------------------------------------------------------------------------------------------\n")
    time.sleep(4)


# Inicializar o driver
driver = webdriver.Chrome(options=options)

# Acesse o Bing já logado na conta Microsoft
driver.get("https://www.bing.com")

if primeiro_acesso != 'n':
    time.sleep(180)

# Contador de pesquisas
contador = 0

# Lista de palavras para pesquisa
letras = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']

palavras = ['instagram.com/bingolinesports','x.com/falamoura','twitch.tv/falamoura']

# Realizar 30 pesquisas
while contador < 30:

    letras_aleatorias = (random.choice(letras) * int((random.uniform(3, 10))))
    palavras_aleatorias = random.choice(palavras)
    termo = [palavras_aleatorias, letras_aleatorias]    

    dia = datetime.now().strftime("%d/%m/%Y")
    hora = datetime.now().strftime("%H:%M:%S")

    termo = (random.choice(termo))
    search_box = driver.find_element(By.NAME, "q")
    search_box.clear()
    search_box.send_keys(termo)
    search_box.send_keys(Keys.RETURN)
    
    contador += 1

    print(f'[ {dia} - {hora} ] Pesquisa número {contador} realizada.')

    time.sleep(random.uniform(9, 20))  # Espera aleatória para evitar bloqueios

print(f'\n ------------------------------------------------------------ \n')
print(f'\n {contador} Pesquisas foram realizadas... Provavelmente... \n')
print(f'\n ------------------------------------------------------------ \n')

# Reseta o contador
contador = 0

driver.quit()

os.system("taskkill /IM chromedriver.exe /F")
os.system("taskkill /IM microsoft_rewards.exe /F")


sys.exit(0)