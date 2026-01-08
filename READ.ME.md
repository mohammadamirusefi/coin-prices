# Telegram Bot – Simple Python Bot

This Telegram bot is built using the **python-telegram-bot** library and provides several basic features:

### Features
- `/start` → say Hi to user  
- `/help` → Shows a help message  
- `/who_am_i` → shows the user id 
- `/btc_price` → Fetches Bitcoin price from CoinMarketCap  
- Any text message → The bot echoes the message back  

---

## Requirements

Make sure the following tools and libraries are installed:

- Python 3.10+
- Libraries:
  - `python-telegram-bot`
  - `requests`
  - `beautifulsoup4`
  - `lxml`

Install all dependencies:

```bash
pip install python-telegram-bot requests beautifulsoup4 lxml
```

---

## Setup Token

Replace the token in your script with the one obtained from BotFather:

```python
application = Application.builder().token("YOUR_TOKEN_HERE").build()
```

**Important:** Do NOT upload your real token to public repositories.

---

## How to Run

Open a terminal inside the project folder and run:

```bash
python main.py
```

If everything is correct, the bot will start polling:

```
Bot is polling...
```

You can now send the following commands to your bot in Telegram:

- `/start`
- `/help`
- `/who_am_i`
- `/btc_price`

---

