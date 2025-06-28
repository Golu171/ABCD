#🇳‌🇮‌🇰‌🇭‌🇮‌🇱‌
# Add your details here and then deploy by clicking on HEROKU Deploy button
import os
from os import environ

API_ID = int(environ.get("API_ID", "16214694"))
API_HASH = environ.get("API_HASH", "8154916973:AAHlVUTje28NxA2pbAwjDseP1TZg1EFW2Gg")
BOT_TOKEN = environ.get("BOT_TOKEN", "7708959953:AAEKxWJZuoWvqn2PiyeNyUhyn10OEDGE3wk")
OWNER = int(environ.get("OWNER", "5543709855"))
CREDIT = "𝙎𝘼𝙄𝙉𝙄 𝘽𝙊𝙏𝙎"
AUTH_USER = os.environ.get('AUTH_USERS', '5543709855').split(',')
AUTH_USERS = [int(user_id) for user_id in AUTH_USER]
if int(OWNER) not in AUTH_USERS:
    AUTH_USERS.append(int(OWNER))
  
#WEBHOOK = True  # Don't change this
#PORT = int(os.environ.get("PORT", 8080))  # Default to 8000 if not set
