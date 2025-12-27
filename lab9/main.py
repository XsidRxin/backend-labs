from fastapi import FastAPI, Depends, Form
from fastapi.responses import HTMLResponse
from sqlalchemy.orm import Session
from database import engine, SessionLocal, Base
from models import User, Post
import crud
import uvicorn

Base.metadata.create_all(bind=engine)

app = FastAPI()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


# ---------- Главная ----------
@app.get("/", response_class=HTMLResponse)
def home():
    return """
    <h1>Home</h1>
    <a href="/users">Users</a><br>
    <a href="/posts">Posts</a><br>
    <a href="/user/create">Create user</a><br>
    <a href="/post/create">Create post</a>
    """


# ---------- Пользователи ----------
@app.get("/users", response_class=HTMLResponse)
def users(db: Session = Depends(get_db)):
    users = db.query(User).all()
    html = "<h1>Users</h1><ul>"
    for user in users:
        html += f"""
        <li>
            {user.username} ({user.email})
            <a href="/user/edit/{user.id}">[edit]</a>
        </li>
        """
    html += "</ul><a href='/'>Home</a>"
    return html


@app.get("/user/create", response_class=HTMLResponse)
def create_user_form():
    return """
    <h1>Create User</h1>
    <form method="post">
        <input name="username" placeholder="Username"><br>
        <input name="email" placeholder="Email"><br>
        <input name="password" placeholder="Password" type="password"><br>
        <button>Create</button>
    </form>
    <a href="/">Home</a>
    """


@app.post("/user/create", response_class=HTMLResponse)
def create_user(
    username: str = Form(...),
    email: str = Form(...),
    password: str = Form(...),
    db: Session = Depends(get_db)
):
    crud.create_user(db, username, email, password)
    return "<p>User created</p><a href='/users'>Back</a>"


# ---------- РЕДАКТИРОВАНИЕ ПОЛЬЗОВАТЕЛЯ ----------
@app.get("/user/edit/{user_id}", response_class=HTMLResponse)
def edit_user_form(user_id: int, db: Session = Depends(get_db)):
    user = db.query(User).get(user_id)
    return f"""
    <h1>Edit User</h1>
    <form method="post">
        <input name="username" value="{user.username}"><br>
        <input name="email" value="{user.email}"><br>
        <button>Save</button>
    </form>
    <a href="/users">Back</a>
    """


@app.post("/user/edit/{user_id}", response_class=HTMLResponse)
def edit_user(
    user_id: int,
    username: str = Form(...),
    email: str = Form(...),
    db: Session = Depends(get_db)
):
    crud.update_user(db, user_id, username, email)
    return "<p>User updated</p><a href='/users'>Back</a>"


# ---------- Посты ----------
@app.get("/posts", response_class=HTMLResponse)
def posts(db: Session = Depends(get_db)):
    posts = db.query(Post).all()
    html = "<h1>Posts</h1><ul>"
    for post in posts:
        html += f"""
        <li>
            <b>{post.title}</b> – {post.content}
            <a href="/post/edit/{post.id}">[edit]</a>
        </li>
        """
    html += "</ul><a href='/'>Home</a>"
    return html


@app.get("/post/create", response_class=HTMLResponse)
def create_post_form(db: Session = Depends(get_db)):
    users = db.query(User).all()
    html = """
    <h1>Create Post</h1>
    <form method="post">
        <input name="title" placeholder="Title"><br>
        <textarea name="content" placeholder="Content"></textarea><br>
        <select name="user_id">
    """
    for user in users:
        html += f"<option value='{user.id}'>{user.username}</option>"
    html += """
        </select><br>
        <button>Create</button>
    </form>
    <a href="/">Home</a>
    """
    return html


@app.post("/post/create", response_class=HTMLResponse)
def create_post(
    title: str = Form(...),
    content: str = Form(...),
    user_id: int = Form(...),
    db: Session = Depends(get_db)
):
    crud.create_post(db, title, content, user_id)
    return "<p>Post created</p><a href='/posts'>Back</a>"


@app.get("/post/edit/{post_id}", response_class=HTMLResponse)
def edit_post_form(post_id: int, db: Session = Depends(get_db)):
    post = db.query(Post).get(post_id)
    users = db.query(User).all()

    html = f"""
    <h1>Edit Post</h1>
    <form method="post">
        <input name="title" value="{post.title}"><br>
        <textarea name="content">{post.content}</textarea><br>
        <select name="user_id">
    """
    for user in users:
        selected = "selected" if user.id == post.user_id else ""
        html += f"<option value='{user.id}' {selected}>{user.username}</option>"
    html += """
        </select><br>
        <button>Save</button>
    </form>
    <a href="/posts">Back</a>
    """
    return html


@app.post("/post/edit/{post_id}", response_class=HTMLResponse)
def edit_post(
    post_id: int,
    title: str = Form(...),
    content: str = Form(...),
    user_id: int = Form(...),
    db: Session = Depends(get_db)
):
    crud.update_post(db, post_id, title, content)
    return "<p>Post updated</p><a href='/posts'>Back</a>"


if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8000)
