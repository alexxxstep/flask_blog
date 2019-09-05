from flask import Blueprint
from flask import render_template
from models import Task, Tag
from flask import request

tasks = Blueprint('tasks', __name__, template_folder='templates')


@tasks.route('/')
def index():

    q = request.args.get('q')
    if q:
        tasks = Task.query.filter(Task.title.contains(q) | Task.body.contains(q)).all()
    else:
        pass


    tasks = Task.query.all()
    return render_template('tasks/index.html', tasks=tasks)

@tasks.route('/<slug>')
def task_detail(slug):
    task = Task.query.filter(Task.slug==slug).first()
    tags = task.tags
    return render_template('tasks/task_detail.html', task=task, tags=tags)

#http://localhost/task/tag/python
@tasks.route('/tag/<slug>')
def tag_detail(slug):
    tag = Tag.query.filter(Tag.slug==slug).first()
    tasks = tag.tasks.all()
    return render_template('tasks/tag_detail.html', tag=tag, tasks=tasks)

