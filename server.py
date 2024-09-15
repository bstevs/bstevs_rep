from flask import Flask, render_template, request
from database.db import insert_employee_task

app = Flask(__name__)

@app.route('/register_task_page')
def register_task_page():
    return render_template("register_task.html")

@app.route('/register_task', methods=["POST"])
def register_task():
    data = request.form
    employee_name, job_activity, job_description, employee_id = data["employee_name"], data["job_activity"], data["job_description"], data["employee_id"]
    insert_employee_task(employee_name, job_activity, job_description, employee_id)
    return "Task added"

if __name__ == "__main__":    
    app.run(host="127.0.0.1", port=5000, debug=True)


    #para buscar la pagina en google. http://localhost:5000/register_task_page
