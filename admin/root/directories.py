# Build paths inside the project like this: BASE_DIR / 'subdir'.
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent

# dir for render_view
TEMPLATE_DIR = BASE_DIR / 'templates'
# dir for static file / assets
STATIC_DIR = BASE_DIR / 'static'

# set app in here
APP_DIRS = {

    'auth': 'auth',
    'modul': 'modul',
    'materi': 'materi',
    'tilawah': 'tilawah',
    'mawaris': 'mawaris',
    'fiqh': 'fiqh',
    'tajwid': 'tajwid',
    'fathurahman': 'fathurahman',
    'umum': 'umum',
    'diskusi': 'diskusi',
    'latihan': 'latihan',
    'api': 'api'

}
