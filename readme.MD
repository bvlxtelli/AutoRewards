# 🤖 **AutoRewards** - *Pesquisas automáticas no Rewards*

Automação em Python usando Selenium para realizar pesquisas no Bing e acumular pontos no programa Microsoft Rewards.

## 🧠 Sobre o Projeto

Este script automatiza até **30 pesquisas diárias no Bing**, usando o navegador Chrome já logado com o perfil do usuário. É ideal para quem deseja maximizar os pontos diários do Microsoft Rewards de forma segura, com um toque de personalização e persistência de dados.

## ⚙️ Funcionalidades

- ✅ Detecção e salvamento do nome de usuário do sistema  
- ✅ Persistência de configurações em `config.json`  
- ✅ Execução oculta do `chromedriver` em segundo plano  
- ✅ Integração com o perfil logado do Chrome  
- ✅ Delay aleatório entre pesquisas para simular comportamento humano  
- ✅ Interface de terminal com arte ASCII e mensagens dinâmicas

## 📂 Estrutura do Projeto

```bash
📦ms_rewards_automator/
┣ 📁dependencies/
┃ ┗ 📄chromedriver.exe
┣ 📄main.py
┣ 📄README.md
```

> 📝 O script cria automaticamente uma pasta `.msrwd` no diretório do usuário para salvar as configurações.

## 🚀 Como usar

### 1. Pré-requisitos

- Python 3.8+
- Google Chrome instalado
- Conta Microsoft
- Instale as dependências
- Baixe o [ChromeDriver](https://chromedriver.chromium.org/downloads) compatível com a versão atual do Google Chrome e coloque o `chromedriver.exe` dentro da pasta `dependencies/`.

### 2. Execute o script

```bash
python main.py
```

## 🖥️ Primeira execução

- O script pedirá seu nome de usuário do PC para configurar o caminho correto do Chrome.
- Será aberto um navegador para que você possa logar com sua conta Microsoft (caso não esteja logado).
- A partir da próxima execução, ele lembrará do seu perfil.

### 🔐 Onde as configurações são salvas?

```bash
C:\Users\SeuNome\AppData\Roaming\.msrwd\config.json
```

## 📌 Observações importantes

- ⚠️ Este projeto é apenas para uso educacional e pessoal.
- ⚠️ A automação de sistemas de recompensa pode violar os termos de uso da Microsoft. Use com responsabilidade.

### 🧑‍💻 Autor

- Desenvolvido por `@bvlxtelli`.