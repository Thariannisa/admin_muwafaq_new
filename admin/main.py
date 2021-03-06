from root import app
from root import routes
from dotenv import load_dotenv
from root.directories import BASE_DIR
import os

credential_path = "C:\gcloud_key\key_rio\key.json"
os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = credential_path

load_dotenv(BASE_DIR / '.env')

if __name__ == '__main__':
    app.config['SECRET_KEY'] = '5791628bb0b13ce0c676dfde280ba288'
    app.run(debug=True if os.getenv('FLASK_ENV') == 'development' else False)
