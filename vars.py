import dotenv, os, datetime

dotenv.load_dotenv()

# API vars
base_robotevents_url = os.getenv('BASE_ROBOTEVENTS_URL')
robotevents_api_key = os.getenv('ROBOTEVENTS_API_KEY')
discord_api_key = os.getenv('DISCORD_API_KEY')

# Constants/time vars
std_reaction_timeout = datetime.timedelta(minutes=15)