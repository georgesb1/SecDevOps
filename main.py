from fastapi import FastAPI, Request
from fastapi.responses import FileResponse, JSONResponse
from fastapi.staticfiles import StaticFiles
from chatlogic import handle_user_message
from chatlogs.database import database, chat_logs

app = FastAPI()

app.mount("/static", StaticFiles(directory="static"), name="static")

@app.get("/")
async def get_frontend(request: Request):
    return FileResponse("static/index.html")

@app.post("/chatbot/")
async def chat(user_message: dict):
    try:
        user_message_text = user_message["user_message"]
        bot_reply = handle_user_message(user_message_text)

        query = chat_logs.insert().values(user_message=user_message_text, bot_reply=bot_reply)
        await database.execute(query)

        return {"user_message": user_message_text, "bot_reply": bot_reply}
    except Exception as e:
        return {"user_message": user_message_text, "bot_reply": "An error occurred: " + str(e)}

@app.post("/submit-feedback/")
async def submit_feedback(feedback: dict):
    try:
        rating = feedback["rating"]
        user_feedback = feedback["feedback"]

        query = chat_logs.update().values(user_feedback=user_feedback).where(chat_logs.c.id == feedback["feedback_id"])
        await database.execute(query)

        return {"message": "Feedback submitted successfully"}
    except Exception as e:
        return {"error": str(e)}

@app.get("/feedbacks/")
async def get_feedbacks():
    try:
        query = chat_logs.select().where(chat_logs.c.user_feedback.isnot(None))
        result = await database.fetch_all(query)

        feedback_data = []
        for row in result:
            feedback_data.append({
                "id": row["id"],
                "user_feedback": row["user_feedback"],
            })

        return JSONResponse(content=feedback_data)
    except Exception as e:
        return JSONResponse(content={"error": str(e)}, status_code=500)

@app.get("/chatlogs/")
async def get_chatlogs():
    try:
        query = chat_logs.select()
        result = await database.fetch_all(query)

        chat_log_data = []
        for row in result:
            chat_log_data.append({
                "id": row["id"],
                "user_message": row["user_message"],
                "bot_reply": row["bot_reply"],
            })

        return JSONResponse(content=chat_log_data)
    except Exception as e:
        return JSONResponse(content={"error": str(e)}, status_code=500)

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
