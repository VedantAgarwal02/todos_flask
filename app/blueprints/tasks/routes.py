from flask import render_template, request, redirect, url_for, jsonify
from . import tasks_bp
from ...extensions import db
from ...models import Task

@tasks_bp.route("/")
def index():
    tasks = Task.query.order_by(Task.created_at.desc()).all()
    return render_template("tasks/list.html", tasks=tasks)

@tasks_bp.route("/add", methods=["GET", "POST"])
def add_task():
    if request.method == "POST":
        title = request.form.get("title","").strip()
        description = request.form.get("description","").strip()
        if not title:
            return render_template("tasks/add.html", error="Title required", title=title, description=description)
        t = Task(title=title, description=description)
        db.session.add(t)
        db.session.commit()
        return redirect(url_for("tasks.index"))
    return render_template("tasks/add.html")

@tasks_bp.route("/edit/<int:id>", methods=["POST"])
def edit_task(id):
    t = Task.query.get_or_404(id)
    t.title = request.form.get("title","").strip()
    t.description = request.form.get("description","").strip()
    t.done = request.form.get("done")=="on"
    db.session.commit()
    return redirect(url_for("tasks.index"))

@tasks_bp.route("/delete/<int:id>", methods=["POST"])
def delete_task(id):
    t = Task.query.get_or_404(id)
    db.session.delete(t)
    db.session.commit()
    return redirect(url_for("tasks.index"))
