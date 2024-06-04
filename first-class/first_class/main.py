from fastapi import FastAPI


app = FastAPI()

@app.get("/")
def hello():
    chatgpt = {
        "message": "Hello for Chatgpt",    
    }
    return chatgpt

@app.get("/chatgpt")
def hello():
    chatgpt = {
        "message": "Hello for Chatgpt",    
    }
    return chatgpt


@app.get("/gemini")
def hello():
    Gemini = {
        "message": "Hello for Gemini",    
    }
    return Gemini
@app.post("/gemini")
def hello(a,b):
    gemini = {
        "message": int(a)+int(b),    
    }
    return gemini

@app.post("/todo")
def add_todo(name,message):
    gemini = {
        "message": {"name": name,"message": message}   
    }
    return gemini




