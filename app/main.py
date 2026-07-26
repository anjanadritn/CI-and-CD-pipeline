from fastapi import FastAPI

app = FastAPI(title="CI/CD Demo App")


@app.get("/")
def home():
    return {"message": "CI/CD Demo App is running!"}


@app.get("/hello")
def hello(name: str = "World"):
    return {"message": f"Hello, {name}!"}


@app.get("/version")
def version():
    return {"version": "1.0.0"}


@app.get("/health")
def health():
    return {"status": "ok"}
