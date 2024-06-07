from flask import Flask, render_template
from models import db, TeacherLoad

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///teachers_load.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)

@app.route('/')
def index():
    loads = TeacherLoad.query.all()
    return render_template('index.html', loads=loads)

if __name__ == '__main__':
    app.run(debug=True)
