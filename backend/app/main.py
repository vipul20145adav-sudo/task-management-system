from fastapi import FastAPI

app =FastAPI()

@app.get("/")
def home():
    return {"message":"welcome to AI Powered Task Management System"}
