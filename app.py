from api import create_app
from api.database.db import DatabaseConnection
from config import env_config, runtime_mode

my_db = DatabaseConnection()

api = create_app(env_config.get("{}".format(runtime_mode)))

if __name__ == "__main__":
    api.run()
    
