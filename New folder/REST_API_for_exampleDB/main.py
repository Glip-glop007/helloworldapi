from fastapi import FastAPI
from database import conn, cur

app = FastAPI()

@app.get("/")
def root():
    return {"message":"FastAPI is connected to PostgreSQL"}

@app.get("/users")
def get_users():
    cur.execute("select * from user_table")
    return {"user_table": cur.fetchall()}

@app.get("/users/{userid}")
def get_user(userid: int):
    cur.execute("select * from user_table where userid = %s", (userid,))
    return {"user": cur.fetchall()}

@app.post("/users")
def create_user(name: str, email: str):
    cur.execute("insert into user_table (name, email) values (%s, %s)", (name, email))
    conn.commit()
    return {"message":"User created successfully"}

@app.delete("/users/{userid}")
def delete_user(userid: int):
    cur.execute("delete from user_table where userid = %s", (userid,))
    conn.commit()
    return {"message":"User deleted successfully"}

@app.put("/users/{userid}")
def update_user(userid: int, name: str, email: str):
    cur.execute("update user_table set name = %s, email = %s where userid = %s", (name, email, userid,))
    conn.commit()
    return {"message":"User updated successfully"}