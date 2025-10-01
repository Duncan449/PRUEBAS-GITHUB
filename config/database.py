from databases import Database

DATABASE_URL = "mysql+aiomysql://root:admin@localhost:3306/ventas"

db = Database(DATABASE_URL)
