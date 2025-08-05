#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# (c) ACE 

import os

class Config(object):
    # get a token from @BotFather
    BOT_TOKEN = os.environ.get("BOT_TOKEN", "7983413191:AAGMbDb9bqTTT68pMjjRd0Q4Y6y4UCyHITo")
    API_ID = int(os.environ.get("API_ID", "22727464"))
    API_HASH = os.environ.get("API_HASH", "f0e595a263c89aa17f6571b8af296ced")
    AUTH_USERS = "887699812"
    LOG_CHAT_ID = int(os.environ.get("LOG_CHAT_ID", "7983413191"))

