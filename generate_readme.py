import sqlite3
from datetime import datetime

def fetch_tasks():
    conn = sqlite3.connect('to_achieve.db')
    cursor = conn.cursor()
    
    cursor.execute("SELECT title, type, category, description, status, date_assigned, start_date, end_date, date_completed FROM tasks")
    tasks = cursor.fetchall()
    
    conn.close()
    return tasks

def format_tasks(tasks):
    achievements = []
    mottos = []
    todos = []
    projects = []
    
    for task in tasks:
        title, task_type, category, description, status, date_assigned, start_date, end_date, date_completed = task
        if task_type == "Achievement":
            achievements.append(f"- **{title}**: {description} *(Completed on {date_assigned})*")
        if task_type == "Project":
            projects.append(f"- **{title}**: {description} *({date_assigned} -> {date_completed})*")
        elif task_type == "Motto/Desire":
            mottos.append(f"- **{title}**: {description} \n *Wished on:* {start_date} *(Status: {status})*")
        elif task_type == "To-Do":
            todos.append(f"- **{title}**: {description} *(Due: {date_assigned}, Status: {status})*")
    
    readme_content = f"""
# My Task List

## Achievements
{chr(10).join(achievements) if achievements else 'No achievements yet.'}

## Projects
{chr(10).join(projects) if projects else 'No projects yet.'}

## Mottos/Desires
{chr(10).join(mottos) if mottos else 'No mottos/desires yet.'}

## To-Dos
{chr(10).join(todos) if todos else 'No to-dos yet.'}
    """
    
    return readme_content

def update_readme(content):
    with open("README.md", "w") as f:
        f.write(content)

if __name__ == "__main__":
    tasks = fetch_tasks()
    formatted_content = format_tasks(tasks)
    update_readme(formatted_content)
