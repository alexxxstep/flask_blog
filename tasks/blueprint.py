from flask import Blueprint
from flask import render_template
from models import Task

tasks = Blueprint('tasks', __name__, template_folder='templates')


@tasks.route('/')
def index():
    tasks = Task.query.all()
    return render_template('tasks/index.html', tasks=tasks)

@tasks.route('/<slug>')
def task_detail(slug):
    task = Task.query.filter(Task.slug==slug).first()
    return render_template('tasks/task_detail.html', task=task)
