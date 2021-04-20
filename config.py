from dotenv import load_dotenv
import os

load_dotenv()

### config.py ###

# Scheme: "postgresql+psycopg2://<USERNAME>:<PASSWORD>@<IP_ADDRESS>:<PORT>/<DATABASE_NAME>"

DATABASE_URI = os.environ.get('DATABASE_URI')
