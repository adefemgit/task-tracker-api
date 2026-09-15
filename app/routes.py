from flask import Blueprint, request, jsonify
from app import db
from app.models import Task

bp = Blueprint('tasks', __name__)

@bp.route('/tasks', methods=["POST"])
def create_task():
    data = request.get_json()
    new_task = Task(title=data["title"])
    db.session.add(new_task)
    db.session.commit()

    return jsonify({"id": new_task.id, "title": new_task.title, "completed": new_task.completed}), 201

@bp.route("/tasks",methods= ["GET"])
def get_tasks():
    tasks = Task.query.all()
    result = []
    for task in tasks:
        result.append({"id": task.id, "title": task.title, "completed": task.completed})
    return jsonify({"tasks": result})

@bp.route("/tasks/<int:task_id>", methods= ["GET"])
def get_task(task_id):
    task = db.session.get(Task, task_id)
    if not task:
        return jsonify({"error": "Task not found"}), 404

    return jsonify({"id": task.id, "title": task.title, "completed": task.completed})

@bp.route("/tasks/<int:task_id>", methods= ["PUT"])
def update_task(task_id):
    task = db.session.get(Task, task_id)
    if not task:
        return jsonify({"error": "Task not found"}), 404

    data = request.get_json()
    if "title" in data:
        task.title = data["title"]

    if "completed" in data:
        task.completed = data["completed"]

    db.session.commit()
    return jsonify({"id": task.id, "title": task.title, "completed": task.completed})
