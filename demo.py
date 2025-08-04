from supabase import create_client, Client

SUPABASE_URL = 'https://kfsjdwbycnyoxisdccqn.supabase.co'
SUPABASE_KEY = 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6Imtmc2pkd2J5Y255b3hpc2RjY3FuIiwicm9sZSI6InNlcnZpY2Vfcm9sZSIsImlhdCI6MTc1NDI5MTAxOSwiZXhwIjoyMDY5ODY3MDE5fQ.CrDyByet-xV2mJiMQpkqRuEmliEBJpGCAMf4PR1ISqU'

supabase: Client = create_client(SUPABASE_URL, SUPABASE_KEY)

# Insert a new row into table
# new_row = {'first_name': 'John Doe'}
# supabase.table('demo-table').insert(new_row).execute()

# Update a row in the table
# new_row = {'first_name': 'Jane Doe'}
# supabase.table('demo-table').update(new_row).eq('id',2).execute()

# Delete record
# supabase.table('demo-table').delete().eq('id',2).execute()

# Fetch all record
# results = supabase.table('demo-table').select('*').execute()
# print(results)

response = supabase.storage.from_('demo-bucket').get_public_url('1.jpg')

print(response)




