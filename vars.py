import dotenv, os

dotenv.load_dotenv()

base_robotevents_url = os.getenv('BASE_ROBOTEVENTS_URL')
robotevents_api_key = os.getenv('ROBOTEVENTS_API_KEY')
discord_api_key = os.getenv('DISCORD_API_KEY')