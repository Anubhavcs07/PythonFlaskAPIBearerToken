from werkzeug.security import generate_password_hash
from app import create_app
from db import db
from models.models import UserModels

# Create an app instance
app = create_app()

# Add a user to the database
with app.app_context():
    # Check if the user already exists
    if not UserModels.query.filter_by(username="testuser").first():
        user = UserModels(username="testuser", password=generate_password_hash("testpass"))
        db.session.add(user)
        db.session.commit()
        print("User 'testuser' has been created!")
    else:
        print("User 'testuser' already exists.")
