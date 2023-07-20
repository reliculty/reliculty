from website.models import User
from . import db

# Create a new user object
user = User(username='admin', password='admin123')

# Add the user to the database session
db.session.add(user)

# Commit the transaction to persist the user to the database
db.session.commit()




