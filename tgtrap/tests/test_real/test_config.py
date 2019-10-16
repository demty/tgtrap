from envparse import env

env.read_envfile()

BOT_TOKEN = env("BOT_TOKEN")
PROXY_URL = env("PROXY_URL")
