from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from datetime import datetime
import time
import random
import subprocess
import os

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

caminho_do_chromedriver = os.path.join(os.path.dirname(__file__), "chromedriver.exe")  # No Windows
subprocess.Popen([caminho_do_chromedriver])

time.sleep(3)

caminho_do_log = os.path.join(os.path.dirname(__file__), "user_log.txt")

# Recebe o nome de usuário e salva

input_nome_de_usuario = input('Digite CORRETAMENTE seu nome de usuário do PC:')
nome_de_usuario = input_nome_de_usuario

# Confirmaçao do nome de usuário

confirmacao_nome_de_usuario = input('Digitou CORRETAMENTE, seu pau no cu? [S] ou [N].').strip().lower()

# Loop se não der certo

while confirmacao_nome_de_usuario != 's':
    input_nome_de_usuario = input('Digite CORRETAMENTE seu nome de usuário do PC:')
    nome_de_usuario = input_nome_de_usuario
    confirmacao_nome_de_usuario = input('Agora foi, seu merda? [S] ou [N]' ).strip().lower()

print('\n ----------------------------------------- \n')
print(f'\n Boa, {nome_de_usuario.upper()}. Vamo dale, então! \n')
print('\n ----------------------------------------- \n')

time.sleep(2)

print('fim')