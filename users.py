from replit import db

def add_user(username,password):
  if username in db:
    print("User already exists.")
  else:
    db[username] = password
    print("User added successfully.")

def check_user(username,password):
  stored_password = db[username]

  if stored_password == password:
    print("Login successful!")
  else:
    print("Login failed!")
