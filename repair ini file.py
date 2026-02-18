import configparser
import shutil
import os
from datetime import datetime

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
CONFIG_FILE = os.path.join(BASE_DIR, "config.ini")

DEFAULTS = {
    "database": {
        "host": "127.0.0.1",
        "port": "5432",
        "name": "mydb"
    }
}

config = configparser.ConfigParser()
config.read(CONFIG_FILE)

fixed = False

for section, values in DEFAULTS.items():
    if not config.has_section(section):
        config.add_section(section)
        fixed = True

    for key, default_value in values.items():
        if not config.get(section, key, fallback="").strip():
            config.set(section, key, default_value)
            fixed = True

if fixed:
    backup_name = f"{CONFIG_FILE}.{datetime.now().strftime('%Y%m%d_%H%M%S')}.bak"
    shutil.copy(CONFIG_FILE, backup_name)

    with open(CONFIG_FILE, "w") as f:
        config.write(f)

    print("Конфиг исправлен, создан бэкап:", backup_name)
else:
    print("Конфиг в порядке")