import dotenv, os, datetime

if os.path.exists('env'):
    dotenv.load_dotenv()

# API vars
BASE_ROBOTEVENTS_URL = os.getenv('BASE_ROBOTEVENTS_URL')
ROBOTEVENTS_API_KEY = os.getenv('ROBOTEVENTS_API_KEY')
DISCORD_API_KEY = os.getenv('DISCORD_API_KEY')
PORT = os.environ.get('PORT', 8080)

# Constants/time vars
DURATION_TILL_TIMEOUT = datetime.timedelta(minutes=15)
CURRENT_SEASON_ID = 197 