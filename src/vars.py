import dotenv, os, datetime

def env_file_exists():
    if os.path.exists('/RobotEvents Bot/env'):
        dotenv.load_dotenv()
        return True

# API vars
BASE_ROBOTEVENTS_URL = os.getenv('BASE_ROBOTEVENTS_URL')
ROBOTEVENTS_API_KEY = os.getenv('ROBOTEVENTS_API_KEY')
DISCORD_API_KEY = os.getenv('DISCORD_API_KEY')

# Constants/time vars
DURATION_TILL_TIMEOUT = datetime.timedelta(minutes=15)
CURRENT_SEASON_ID = 197 