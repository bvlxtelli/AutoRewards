# 🤖 **AutoRewards** - *Automated Searches on Rewards*

Python automation using Selenium to perform Bing searches and earn points in the Microsoft Rewards program.

## 🧠 About the Project

This script automates up to **30 daily Bing searches** using the Chrome browser already logged in with the user's profile. It's ideal for those who want to maximize their daily Microsoft Rewards points safely, with a touch of customization and data persistence.

## ⚙️ Features

- ✅ Detection and saving of system username  
- ✅ Configuration persistence in `config.json`  
- ✅ Hidden execution of `chromedriver` in the background  
- ✅ Integration with logged-in Chrome profile  
- ✅ Random delay between searches to simulate human behavior  
- ✅ Terminal interface with ASCII art and dynamic messages

## 📂 Project Structure

```bash
📦ms_rewards_automator/
┣ 📁dependencies/
┃ ┗ 📄chromedriver.exe
┣ 📄main.py
┣ 📄README.md
```

> 📝 The script automatically creates a `.msrwd` folder in the user's directory to save configurations.

## 🚀 How to Use

### 1. Prerequisites

- Python 3.8+
- Google Chrome installed
- Microsoft account
- Install dependencies
- Download the [ChromeDriver](https://chromedriver.chromium.org/downloads) compatible with your Chrome version and place `chromedriver.exe` inside the `dependencies/` folder.

### 2. Run the Script

```bash
python main.py
```

## 🖥️ First Run

- The script will ask for your PC username to configure the correct Chrome path.
- A browser will open for you to log in with your Microsoft account (if not already logged in).
- From the next run, it will remember your profile.

### 🔐 Where are the configurations saved?

```bash
C:\Users\YourName\AppData\Roaming\.msrwd\config.json
```

## 📌 Important Notes

- ⚠️ This project is for educational and personal use only.
- ⚠️ Automating rewards systems may violate Microsoft’s terms of use. Use responsibly.

### 🧑‍💻 Author

- Developed by `@bvlxtelli`.
