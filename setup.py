import google.generativeai as genai
from kaggle_secrets import UserSecretsClient
#Configure google api key 
GOOGLE_API_KEY=UserSecretsClient().get_secret("GOOGLE_API_KEY")
genai.configure(api_key=GOOGLE_API_KEY)
