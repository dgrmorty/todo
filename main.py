from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import Optional, List
import sqlite3
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

# Настройка CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://127.0.0.1:8080"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


# Модель задачи
class Task(BaseModel):
    id: Optional[int] = None
    title: str
    description: Optional[str] = None
    completed: bool = False
    category: Optional[str] = None
    due_date: Optional[str] = None


# Инициализация базы данных
def init_db():
    conn = sqlite3.connect("tasks.db")
    c = conn.cursor()
    c.execute(
        """
        CREATE TABLE IF NOT EXISTS tasks (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            title TEXT NOT NULL,
            description TEXT,
            completed BOOLEAN NOT NULL,
            category TEXT,
            due_date TEXT
        )
    """
    )
    conn.commit()
    conn.close()


init_db()


# Получение всех задач
@app.get("/tasks/", response_model=List[Task])
async def get_tasks():
    conn = sqlite3.connect("tasks.db")
    c = conn.cursor()
    c.execute("SELECT id, title, description, completed, category, due_date FROM tasks")
    tasks = [
        Task(
            id=row[0],
            title=row[1],
            description=row[2],
            completed=bool(row[3]),
            category=row[4],
            due_date=row[5],
        )
        for row in c.fetchall()
    ]
    conn.close()
    return tasks


# Создание задачи
@app.post("/tasks/", response_model=Task)
async def create_task(task: Task):
    conn = sqlite3.connect("tasks.db")
    c = conn.cursor()
    c.execute(
        """
        INSERT INTO tasks (title, description, completed, category, due_date)
        VALUES (?, ?, ?, ?, ?)
    """,
        (task.title, task.description, task.completed, task.category, task.due_date),
    )
    conn.commit()
    task_id = c.lastrowid
    c.execute(
        "SELECT id, title, description, completed, category, due_date FROM tasks WHERE id = ?",
        (task_id,),
    )
    new_task = c.fetchone()
    conn.close()
    if new_task:
        return Task(
            id=new_task[0],
            title=new_task[1],
            description=new_task[2],
            completed=bool(new_task[3]),
            category=new_task[4],
            due_date=new_task[5],
        )
    raise HTTPException(status_code=500, detail="Ошибка создания задачи")


# Обновление задачи
@app.put("/tasks/{task_id}", response_model=Task)
async def update_task(task_id: int, task: Task):
    conn = sqlite3.connect("tasks.db")
    c = conn.cursor()
    c.execute("SELECT id FROM tasks WHERE id = ?", (task_id,))
    if not c.fetchone():
        conn.close()
        raise HTTPException(status_code=404, detail="Задача не найдена")
    c.execute(
        """
        UPDATE tasks
        SET title = ?, description = ?, completed = ?, category = ?, due_date = ?
        WHERE id = ?
    """,
        (
            task.title,
            task.description,
            task.completed,
            task.category,
            task.due_date,
            task_id,
        ),
    )
    conn.commit()
    c.execute(
        "SELECT id, title, description, completed, category, due_date FROM tasks WHERE id = ?",
        (task_id,),
    )
    updated_task = c.fetchone()
    conn.close()
    if updated_task:
        return Task(
            id=updated_task[0],
            title=updated_task[1],
            description=updated_task[2],
            completed=bool(updated_task[3]),
            category=updated_task[4],
            due_date=updated_task[5],
        )
    raise HTTPException(status_code=500, detail="Ошибка обновления задачи")


# Удаление задачи
@app.delete("/tasks/{task_id}")
async def delete_task(task_id: int):
    conn = sqlite3.connect("tasks.db")
    c = conn.cursor()
    c.execute("SELECT id FROM tasks WHERE id = ?", (task_id,))
    if not c.fetchone():
        conn.close()
        raise HTTPException(status_code=404, detail="Задача не найдена")
    c.execute("DELETE FROM tasks WHERE id = ?", (task_id,))
    conn.commit()
    conn.close()
    return {"message": "Задача удалена"}
