from app import app
from app import db
from app_models import view
from tasks.blueprint import tasks

app.register_blueprint(tasks, url_prefix='/tasks')

if __name__ == '__main__':
    app.run()
