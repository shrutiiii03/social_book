from sqlalchemy import create_engine, text

DATABASE_URI = "postgresql://user:12345@localhost:5432/testdb"
# establish connection
engine = create_engine(DATABASE_URI)
try:
    with engine.connect() as connection:
        result = connection.execute(text("SELECT version();"))
        for row in result:
            print("Database version:", row[0])
except Exception as e:
    print("Error connecting to the database:", e)
finally:
    engine.dispose()

from sqlalchemy import create_engine, Table, Column, Integer, String, MetaData
from sqlalchemy.orm import sessionmaker

# insert data into the database
DATABASE_URI = "postgresql://user:12345@localhost:5432/testdb"
engine = create_engine(DATABASE_URI, echo=True)
metadata = MetaData()

books_table = Table(
    'books', metadata,
    Column('id', Integer, primary_key=True),
    Column('title', String, nullable=False),
    Column('author', String),
    Column('published_year', Integer),
)

metadata.create_all(engine)

Session = sessionmaker(bind=engine)
session = Session()

ins = books_table.insert().values(title='1984', author='George Orwell', published_year=1949)

session.execute(ins)
session.commit()  
print("Added new book with title '1984' by George Orwell")



# fetching data from the database
from sqlalchemy import create_engine, Table, Column, Integer, String, MetaData
from sqlalchemy.orm import sessionmaker

DATABASE_URI = "postgresql://user:12345@localhost:5432/testdb"
engine = create_engine(DATABASE_URI, echo=True)
metadata = MetaData()

books_table = Table(
    'books', metadata,
    Column('id', Integer, primary_key=True),
    Column('title', String, nullable=False),
    Column('author', String),
    Column('published_year', Integer),
)
Session = sessionmaker(bind=engine)
session = Session()


query = books_table.select()
result = session.execute(query)
for row in result:
    print(f"ID: {row[0]}, Title: {row[1]}, Author: {row[2]}, Year: {row[3]}")
session.close()
