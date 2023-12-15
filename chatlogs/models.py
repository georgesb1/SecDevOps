import sqlalchemy

metadata = sqlalchemy.MetaData()

chat_log = sqlalchemy.Table(
    "chat_logs",
    metadata,
    sqlalchemy.Column("id", sqlalchemy.Integer, primary_key=True),
    sqlalchemy.Column("user_message", sqlalchemy.String),
    sqlalchemy.Column("bot_reply", sqlalchemy.String),
    sqlalchemy.Column("user_feedback", sqlalchemy.String) 
)
