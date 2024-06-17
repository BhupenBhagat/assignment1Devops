from fastapi import FastAPI

app = FastAPI()


@app.get("/home")
def read_root():
    return {"Hello": "home"}

@app.get("/")
def read_root():
    return {"Hello": "duniya"}

@app.get("/v1")
def read_root():
    return {"get": "lost"}

@app.get("/about")
def about():
    return {"msg": "About Us"}