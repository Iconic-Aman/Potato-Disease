from fastapi import FastAPI

app = FastAPI()

@app.get('/hello')
def func():
    return "Fastapi is a server used to show the file into local host.."




