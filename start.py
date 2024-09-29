import os
os.system("screen -dmS 'moosify_dev' venv/bin/python3 manage.py runserver")    
os.system("screen -dmS 'moosify_cleaner' venv/bin/python3 cleaner.py")
