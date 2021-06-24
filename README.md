# isfcr-project

## About
A discord bot that automatically checks for offensive and NSFW content.

## Contents
1.  [Requirements](#Requirements)
2.  [Running](#Running)
3.  [Commands](#Commands)

## Requirements
1.  Python 3

## Running

Create a virtual environment(optional) in python using
```bash
python3 -m venv .
```

Install the dependencies using
```bash
pip install -r requirements.txt
```

Add a `.env` file in the root of the project directory and the following two fields
```text
PREFIX=PREFIX_YOU_WANT_TO_INVOKE_THE_BOT_WITH
TOKEN=TOKEN_FOR_THE_SERVER
```

To start the bot
```bash
python3 app.py
```

## Commands
1.  whoareu<br>
    Gives a short description of what exactly the bot does.
