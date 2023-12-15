import sqlalchemy
from databases import Database

DATABASE_URL = "sqlite:///chatbot.db"

database = Database(DATABASE_URL)

metadata = sqlalchemy.MetaData()

chat_logs = sqlalchemy.Table(
    "chat_logs",
    metadata,
    sqlalchemy.Column("id", sqlalchemy.Integer, primary_key=True),
    sqlalchemy.Column("user_message", sqlalchemy.String),
    sqlalchemy.Column("bot_reply", sqlalchemy.String),
    sqlalchemy.Column("user_feedback", sqlalchemy.String), 
)

engine = sqlalchemy.create_engine(DATABASE_URL)
metadata.create_all(engine)
