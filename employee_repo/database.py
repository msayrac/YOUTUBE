import os
from supabase import create_client, Client
from dotenv import load_dotenv

load_dotenv()

SUPABASE_URL = os.getenv('SUPABASE_URL')
SUPABASE_KEY = os.getenv('SUPABASE_KEY')
SUPABASE_BUCKET = os.getenv('SUPABASE_BUCKET')

if not all([SUPABASE_URL, SUPABASE_KEY, SUPABASE_BUCKET]):
    raise EnvironmentError('One or more Supabase environment variables are missing.')

supabase: Client = create_client(SUPABASE_URL, SUPABASE_KEY)











