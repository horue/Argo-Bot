


# Argo-Bot

Argo-Bot is a multi-functional Discord bot designed to enhance user interactions with a variety of commands and features. It offers basic utilities, fun commands, and custom prefix support for different servers.

## Table of Contents

-   [Features](#features)
-   [Installation](#installation)
-   [Configuration](#configuration)
-   [Commands](#commands)
-   [License](#license)

## Features

-   Customizable prefix per server
-   Fun commands like rolling dice, flipping coins, and generating random characters
-   Interaction commands like hugging and kissing other users
-   Informative commands such as sending the bot version and server invite links
-   Anime-related commands including image fetching from an API
-   Basic music command to join voice channels

## Installation

### Prerequisites

-   Python 3.7 or higher
-   Discord.py library
-   Requests library
-   dotenv library

### Steps

1.  Clone the repository:
    
    `git clone https://github.com/your-username/argo-bot.git
    cd argo-bot` 
    
2.  Install the required libraries:
    
    `pip install discord.py requests python-dotenv` 
    
3.  Set up your environment variables: Create a `.env` file in the root directory of the project and add your bot token:
    
    `DISCORD_TOKEN=your_bot_token_here` 
    
4.  Create a `key.py` file and add your bot token:
    
    `key = 'your_bot_token_here'` 
    
5.  Create the necessary JSON files for prefixes and other lists:
    
    -   `sample.json` for prefixes
    -   `lists.py` for various random lists
    -   `embeds.py` for embedded messages

## Configuration

### sample.json

This file holds the custom prefixes for each server. Example structure:



`{
  "server_id": {
    "prefix": "!"
  }
}` 

### lists.py

This file holds various lists used in the bot, such as phrases, anime images, etc. Example:

    frases_do_dia = [
        "Seize the day!",
        "Carpe Diem!"
    ]
    
    suguestão = [
        "Fullmetal Alchemist: Brotherhood",
        "Steins;Gate"
    ]

### embeds.py

This file contains embedded message templates. Example:


    import discord
    
    ajuda = discord.Embed(
        title = "Ajuda",
        description = "Lista de comandos disponíveis",
        color = 0x00ff00
    )

## Commands

### Basic Commands

-   `log` - Sends a log of changes and updates.
-   `olá` (aliases: bom dia, boa tarde, boa noite) - Greets the user.
-   `frase` - Sends a random phrase of the day.
-   `servidor` - Sends an invite link to the bot's official server.
-   `l` - Sends a fun message.

### Rolling Commands

-   `roll` (aliases: r, dado, dice) - Rolls a die with specified sides.
-   `multiroll` (aliases: m, mr) - Rolls multiple dice.
-   `moeda` - Flips a coin.
-   `dp` (aliases: dilmas pernetas, dinossauros pelados, duas peles) - Sends a random amount of currency.
-   `per` - Generates a random character.
-   `permedi` (aliases: personagem medieval) - Generates a medieval character.

### Interaction Commands

-   `hug` - Sends an embed of a hug.
-   `kiss` - Sends an embed of a kiss.
-   `eat` - Sends an embed of eating.
-   `jav` - Sends an embed of a joke.

### Custom Prefix

-   `prefix` - Sets a custom prefix for the server.

### Utility Commands

-   `version` (aliases: versão, versao, ver) - Displays the current bot version.
-   `avatar` (aliases: foto, perfil, imagem, profile) - Displays a user's avatar.
-   `sugestão` - Sends a link to submit suggestions.

### Fun Commands

-   `sessão` (aliases: sessão?) - Sends a fun message.
-   `recomendar` (aliases: rec, sug, sugerir) - Recommends an anime.
-   `anime` (aliases: waifu, wa, garota, girl) - Fetches an anime image from an API.
-   `trap` - Sends a random trap image.
-   `pobre` - Sends a meme image.
-   `multi` - Sends a fun message.

### Music Command

-   `joi` - Joins the user's voice channel.
-   `join` - Joins the user's voice channel.

### Embed Help

-   `ajuda` - Sends an embedded help message.

## License

This project is licensed under the MIT License.