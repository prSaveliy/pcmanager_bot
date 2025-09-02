# 🖥️ PC Manager Bot

A Telegram bot that lets you **monitor and control your PC remotely**.  
You can get system info, shutdown/restart your computer, and more – right from Telegram.

## 🚀 Features

- 📊 **System Info**
  - CPU, GPU, RAM and Disk Info

- ⚙️ **PC Control**
  - Shutdown
  - Restart
  - Lock workstation

- 🔉**Sound Options**
  - Mute/Unmute
  - Adjust Volume

- 🔆**Brightness Options**
  - Adjust Brightness
  - Night Light

- 📥**Apps Opening**
  - Browser
  - Telegram
  - Discord
  - Spotify

- 🔒 **Security**
  - Only authorized users (by Telegram ID) can control the PC
 
## 📦 Installation

### 1. Clone the repository
```bash
git clone https://github.com/yourusername/pc-manager-bot.git
cd pc-manager-bot
```

### 2. Create a virtual environment
```bash
python -m venv .venv
.venv\Scripts\activate     # Windows
source .venv/bin/activate  # Linux/macOS
```

### 3. Install dependencies
```bash
pip install -r requirements.txt
```

### 4. Configure settings
```config.py
TOKEN=your_telegram_bot_token
ALLOWED_USER_ID=123456789   # your Telegram user ID
```

### 5. Run the bot
```bash
python run.py
```
## ⚡ Usage

- Start a chat with your bot in Telegram (use @BotFather to create your bot)
- Use these commands:

  - `/start` → Start the bot
  - `/main` → SMain menu
  - `/search` → Search for anything directly from your bot

## Get Involved
Feel free to open issues, submit pull requests, or suggest new features!
