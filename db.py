import sqlite3
from datetime import datetime

# Initialize the database connection
def init_db():
    conn = sqlite3.connect('to_achieve.db')
    cursor = conn.cursor()

    # Create tables
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS tasks (
            id INTEGER PRIMARY KEY,
            title TEXT NOT NULL,
            type TEXT NOT NULL,
            category TEXT,
            description TEXT,
            status TEXT DEFAULT 'Not Done',
            date_assigned TEXT,
            start_date TEXT,
            end_date TEXT,
            date_completed TEXT,
            created_at TEXT DEFAULT CURRENT_TIMESTAMP,
            updated_at TEXT
        )
    ''')

    # Commit changes and close the connection
    conn.commit()
    conn.close()

# Function to add a new task
def add_task(title, task_type, category, description, date_assigned, start_date=None, end_date=None, status="Not Done"):
    conn = sqlite3.connect('to_achieve.db')
    cursor = conn.cursor()
    
    cursor.execute('''
        INSERT INTO tasks (title, type, category, description, status, date_assigned, start_date, end_date)
        VALUES (?, ?, ?, ?, ?, ?, ?, ?)
    ''', (title, task_type, category, description, status, date_assigned, start_date, end_date))
    
    conn.commit()
    conn.close()

# Additional database functions will be added as we proceed...

def mark_task_as_done(task_id):
    conn = sqlite3.connect('to_achieve.db')
    cursor = conn.cursor()
    
    date_completed = datetime.now().strftime('%Y-%m-%d')
    cursor.execute('''
        UPDATE tasks
        SET status = 'Done', date_completed = ?, updated_at = CURRENT_TIMESTAMP
        WHERE id = ?
    ''', (date_completed, task_id))
    
    conn.commit()
    conn.close()
    
def view_all_tasks():
    conn = sqlite3.connect('to_achieve.db')
    cursor = conn.cursor()
    
    cursor.execute('SELECT * FROM tasks ORDER BY date_assigned DESC')
    tasks = cursor.fetchall()
    
    conn.close()
    return tasks

def view_completed_tasks():
    conn = sqlite3.connect('to_achieve.db')
    cursor = conn.cursor()

    cursor.execute('''
        SELECT * FROM tasks
        WHERE status = 'Done'
        ORDER BY date_assigned DESC
    ''')
    tasks = cursor.fetchall()

    conn.close()
    return tasks

def filter_tasks_by_category(category_choice):
    categories = {1: 'Academics', 2: 'Health', 3: 'Passion', 4: 'Career', 5: 'Entertainment'}
    category = categories.get(category_choice)

    if not category:
        raise ValueError("Invalid category choice")

    conn = sqlite3.connect('to_achieve.db')
    cursor = conn.cursor()

    cursor.execute('''
        SELECT * FROM tasks
        WHERE category = ?
        ORDER BY date_assigned DESC
    ''', (category,))
    tasks = cursor.fetchall()

    conn.close()
    return tasks

def filter_tasks_by_type(task_type_choice):
    task_types = {1: 'To-Do', 2: 'Project', 3: 'Achievement', 4: 'Motto/Desire'}
    task_type = task_types.get(task_type_choice)

    if not task_type:
        raise ValueError("Invalid task type choice")

    conn = sqlite3.connect('to_achieve.db')
    cursor = conn.cursor()

    cursor.execute('''
        SELECT * FROM tasks
        WHERE type = ?
        ORDER BY date_assigned DESC
    ''', (task_type,))
    tasks = cursor.fetchall()

    conn.close()
    return tasks

def get_task_by_id(task_id):
    conn = sqlite3.connect('to_achieve.db')
    cursor = conn.cursor()

    cursor.execute('''
        SELECT * FROM tasks
        WHERE id = ?
    ''', (task_id,))
    task = cursor.fetchone()

    conn.close()
    return task