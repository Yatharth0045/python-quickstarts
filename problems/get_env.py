import os
from dotenv import load_dotenv

# export NAME='apple'
print(os.environ['NAME'])
load_dotenv()

print('Repo Name is',os.getenv('REPO'))
