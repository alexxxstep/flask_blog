from flask import Blueprint
from flask import render_template
from models import Task, Tag
from flask import request
from .forms import TaskForm
from app import db

from flask import redirect
from flask import url_for

from flask_security import login_required

tasks = Blueprint('tasks', __name__, template_folder='templates')


# http://localhost/tasks/create
@tasks.route('/create', methods=['POST', 'GET'])
@login_required
def create_task():
    if request.method == 'POST':
        title = request.form['title']
        body = request.form['body']

        try:
            task = Task(title=title, body=body)
            db.session.add(task)
            db.session.commit()
        except:
            print('Something wrong')

        return redirect(url_for('tasks.index'))

    form = TaskForm()
    return render_template('tasks/create_task.html', form=form)

@tasks.route('/<slug>/edit/', methods=['POST', 'GET'])
@login_required
def edit_task(slug):

    task = Task.query.filter(Task.slug == slug).first()
    if request.method == 'POST':
        form = TaskForm(formdata=request.form, obj=task)
        form.populate_obj(task)
        db.session.commit()

        return redirect(url_for('tasks.task_detail', slug=task.slug))

    form = TaskForm(obj=task)
    return render_template('tasks/edit_task.html', task=task, form=form)


@tasks.route('/')
def index():

    q = request.args.get('q')

    page = request.args.get('page')

    if page and page.isdigit():
        page = int(page)
    else:
        page = 1

    if q:
        tasks = Task.query.filter(Task.title.contains(q) | Task.body.contains(q)).all()
    else:
        tasks = Task.query.order_by(Task.created.desc())

    pages = tasks.paginate(page=page,per_page=5)

    return render_template('tasks/index.html', tasks=tasks, pages=pages)

@tasks.route('/<slug>')
def task_detail(slug):
    task = Task.query.filter(Task.slug==slug).first()
    tags = task.tags
    created =task.created.strftime("%d-%b-%Y %H:%M")
    return render_template('tasks/task_detail.html', task=task, tags=tags, created=created)

#http://localhost/task/tag/python
@tasks.route('/tag/<slug>')
def tag_detail(slug):
    tag = Tag.query.filter(Tag.slug==slug).first()
    tasks = tag.tasks.all()
    return render_template('tasks/tag_detail.html', tag=tag, tasks=tasks)

