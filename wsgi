import sys
import logging
logging.basicConfig(stream=sys.stderr)
sys.path.insert(0, "/var/www/flaskapp")

from flaskapp import app as application
application.secret_key = 'your_secret_key'

# Set up the same logging configuration here to ensure it works with Apache
handler = logging.handlers.RotatingFileHandler('/var/log/flaskapp/flaskapp.log', maxBytes=10000, backupCount=1)
handler.setLevel(logging.INFO)
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
handler.setFormatter(formatter)
application.logger.addHandler(handler)
