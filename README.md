# Discord Bot

A simple Discord bot built with discord.py.

## Setup

1. Create a Discord Application and Bot:
   - Go to [Discord Developer Portal](https://discord.com/developers/applications)
   - Create a new application
   - Go to the Bot section and create a bot
   - Copy the bot token

2. Configure the bot:
   - Copy your bot token into the `.env` file:
     ```
     DISCORD_TOKEN=your_bot_token_here
     ```

3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

4. Run the bot:
   ```bash
   python bot.py
   ```

## Commands

- `!hello`: Bot responds with a friendly hello message
- `!ping`: Check the bot's latency

## Adding the Bot to Your Server

1. Go to OAuth2 > URL Generator in your Discord Developer Portal
2. Select the following scopes:
   - bot
   - applications.commands
3. Select bot permissions:
   - Send Messages
   - Read Messages/View Channels
4. Copy and open the generated URL
5. Select your server and authorize the bot
