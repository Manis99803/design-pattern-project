from User import User

#Objects
user = ''

def create_user_object(user_data):
    global user
    user = User(user_data["name"], user_data["password"])

def delete_user_object():
    global user
    del(user)
    User.reset()
    user = ''
    
