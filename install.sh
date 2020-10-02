#!/bin/bash
ENV=""
TOKEN=""
MONGODB_CONNECTION_STRING=""
adminID=""
channelID=""
chatID=""

read -p "ENV (e.g. development, production, etc.): " ENV
read -p "Telegram bot token: " TOKEN
read -p "MongoDB connection string: " MONGODB_CONNECTION_STRING
read -p "Admin Telegram user ID: " adminID
read -p "Telegram channel ID: " channelID
read -p "Telegram chat ID: " chatID

sudo apt-get install -y python3-venv
python3 -m venv venv
source venv/bin/activate
pip3 install -U pip
pip3 install -r requirements.txt

echo "
[$ENV]
TOKEN = $TOKEN
MONGODB_CONNECTION_STRING = $MONGODB_CONNECTION_STRING
adminID = $adminID
channelID = $channelID
chatID = $chatID
" > app/config/.secrets.toml
