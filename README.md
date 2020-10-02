# Bot for Small Senior

Tasks   
- [X] Create posts
- [ ] Collect stats
- [ ] Filter chat

Stack
- Python(3.8.2)
- Aiogram(2.9.2)
- MongoDB

____
### Install on your server
Run `install.sh` and input variables (details below):

| VARIABLES                 | DESCRIPTION                                        |
|---------------------------|-----------------------------------------------------------------------------------------------------------------------|
| `your_env`                | Project environment. Change in `app/config/__init__.py` through switch to another environment, by default, development.
| `TOKEN`                   | Telegram bot token from t.me/BotFather.
| `MONGODB_CONNECTION_STRING`                 | MongoDB connection string to your database.
| `adminID`                 | Telegram user ID of the bot admin.
| `channelID`               | Telegram channel ID to moderate.
| `chatID`                  | Telegram chat ID to moderate.

Run the application
```
python -m app
```

### Install using Docker
```
docker-compose up -d
```