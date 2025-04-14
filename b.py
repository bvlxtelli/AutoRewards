from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from datetime import datetime
import time
import random
import subprocess
import os
import sys

# Define o caminho do driver do Chrome (Para executar sem maiores problemas)

caminho_do_chromedriver = os.path.join(os.path.dirname(__file__), "chromedriver.exe")

# Executa esse processo em segundo plano

subprocess.Popen([caminho_do_chromedriver])

print(" -----------------------------------------------------------------------------------------------------------------\n")

# Inicia o App

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

if getattr(sys, 'frozen', False):  # Se estiver rodando como .exe
    base_dir = sys._MEIPASS
else:
    base_dir = os.path.dirname(__file__)

caminho_do_log = os.path.join(base_dir, "user_log.txt")

log_de_usuario = open(caminho_do_log, encoding='utf-8')
log_de_usuario = log_de_usuario.readlines()

# Recebe o nome de usuário e salva

if not log_de_usuario:
    input_nome_de_usuario = input('Digite CORRETAMENTE seu nome de usuário do PC:')
    nome_de_usuario = input_nome_de_usuario

    # Confirmaçao do nome de usuário

    confirmacao_nome_de_usuario = input('Digitou CORRETAMENTE? [S] ou [N].').strip().lower()

    while confirmacao_nome_de_usuario != 's':
        input_nome_de_usuario = input('Digite CORRETAMENTE seu nome de usuário do PC:')
        nome_de_usuario = input_nome_de_usuario
        confirmacao_nome_de_usuario = input('Agora foi? [S] ou [N]' ).strip().lower()

    escrever_log_de_usuario = open(caminho_do_log, 'w', encoding='utf-8')
    escrever_log_de_usuario.write(str(nome_de_usuario))
    escrever_log_de_usuario.close()

log_de_usuario = open(caminho_do_log, encoding='utf-8')
log_de_usuario = log_de_usuario.readlines()
log_de_usuario = log_de_usuario[0]
nome_de_usuario = log_de_usuario

print('\n ----------------------------------------- \n')
print(f'\n Boa, {nome_de_usuario.upper()}. Vamo dale, então! \n')
print('\n ----------------------------------------- \n')

# ---

caminho_do_log = os.path.join(os.path.dirname(__file__), "user_log.txt")

log_de_usuario = open(caminho_do_log, encoding='utf-8')
log_de_usuario = log_de_usuario.readlines()

# Recebe o nome de usuário e salva

if not log_de_usuario:
    input_nome_de_usuario = input('Digite CORRETAMENTE seu nome de usuário do PC:')
    nome_de_usuario = input_nome_de_usuario

    # Confirmaçao do nome de usuário

    confirmacao_nome_de_usuario = input('Digitou CORRETAMENTE? [S] ou [N].').strip().lower()

    while confirmacao_nome_de_usuario != 's':
        input_nome_de_usuario = input('Digite CORRETAMENTE seu nome de usuário do PC:')
        nome_de_usuario = input_nome_de_usuario
        confirmacao_nome_de_usuario = input('Agora foi? [S] ou [N]' ).strip().lower()

    escrever_log_de_usuario = open(caminho_do_log, 'w', encoding='utf-8')
    escrever_log_de_usuario.write(str(nome_de_usuario))
    escrever_log_de_usuario.close()

log_de_usuario = open(caminho_do_log, encoding='utf-8')
log_de_usuario = log_de_usuario.readlines()
log_de_usuario = log_de_usuario[0]
nome_de_usuario = log_de_usuario

pyinstaller --onefile --runtime-tmpdir=C:\Users\%USERPROFILE%\.msrwd\temp --add-binary "chromedriver.exe;." --hidden-import selenium microsoft_rewards.py