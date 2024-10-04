import os
os.system("screen -dmS 'moosify' gunicorn --chdir /home/ubuntu/hamzastuff/var/www/moosify.azmindroma.de moosify.wsgi:application --bind 127.0.0.1:8000 --workers 3")    
os.system("screen -dmS 'moosify_cleaner' venv/bin/python3 cleaner.py")
os.system("screen -r moosify")