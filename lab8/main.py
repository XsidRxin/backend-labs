from fastapi import FastAPI
from fastapi.responses import HTMLResponse
import uvicorn


app = FastAPI()


@app.get("/", response_class=HTMLResponse)
def home():
    html = """
    <h1>Welcome to FastAPI</h1>
    <p>This is the home page</p>
    <a href="/about">About</a> | <a href="/contact">Contact</a>
    """
    return html


@app.get("/about", response_class=HTMLResponse)
def about():
    html = """
    <h1>About</h1>
    <p>This is about page</p>
    <p>FastAPI is a modern web framework</p>
    <a href="/">Home</a>
    """
    return html


@app.get("/contact", response_class=HTMLResponse)
def contact():
    html = """
    <h1>Contact</h1>
    <p>Email: test@example.com</p>
    <p>Phone: 123-456-7890</p>
    <a href="/">Home</a>
    """
    return html


@app.get("/user/{user_id}", response_class=HTMLResponse)
def get_user(user_id: int):
    html = f"""
    <h1>User Profile</h1>
    <p>User ID: {user_id}</p>
    <a href="/">Home</a>
    """
    return html


if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8000)
