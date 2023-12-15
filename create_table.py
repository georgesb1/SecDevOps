import os
from sqlalchemy import create_engine, Column, Integer, String, MetaData, Table

DATABASE_URL = "sqlite:///chatbot.db"
if not os.path.exists("/home/security/Bureau/Chatbot/chatbot.db"):
    print("db doesnt exist")
    open("/home/security/Bureau/Chatbot/chatbot.db", "w").close()

engine = create_engine(DATABASE_URL)

metadata = MetaData()

chat_logs = Table(
    "chat_logs",
    metadata,
    Column("id", Integer, primary_key=True),
    Column("user_message", String),
    Column("bot_reply", String),
    Column("user_feedback", String) 
)

metadata.create_all(engine)

print("Table 'chat_logs' created or updated successfully.")
