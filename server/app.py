from flask import Flask, render_template
from models import db, User
from flask_migrate import Migrate
import os

app = Flask(__name__)
# Use a relative path for SQLite database
db_path = os.path.join(os.path.abspath(os.path.dirname(__file__)), 'app.db')
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + db_path
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = 'your_secret_key_here'

# Initialize the database and migrations
db.init_app(app)
migrate = Migrate(app, db)



if __name__ == '__main__':
    # Create the database tables before running the app
    with app.app_context():
        db.create_all()
    app.run(debug=True)
