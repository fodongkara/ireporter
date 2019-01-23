from api import create_app
from api.database.db import DatabaseConnection

my_db = DatabaseConnection()

api = create_app()

if __name__ == "__main__":
    api.run(debug=True)
    
