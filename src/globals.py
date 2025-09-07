import dotenv, os

def env_file_exists():
    if os.path.exists('/RobotEvents Bot/env'):
        dotenv.load_dotenv()
        return True

# API vars
ENVIRONMENT = os.getenv('ENVIRONMENT')
BASE_ROBOTEVENTS_URL = os.getenv('BASE_ROBOTEVENTS_URL')
ROBOTEVENTS_API_KEY = os.getenv('ROBOTEVENTS_API_KEY')
DISCORD_API_KEY = os.getenv('DISCORD_API_KEY')