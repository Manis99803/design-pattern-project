class User:
    instance = None
    def __init__(self, user_name, password):
        if User.instance == None:
            self.user_name = user_name
            self.password = password
            User.instance = self
        else:
            raise Exception("This is a Singleton Class")

    def __del__(self):
        self.user_name = None
        self.password = None

    @staticmethod
    def reset():
        User.instance = None
        
    def get_user_name(self):
        return self.user_name

    def get_user_password(self):
        return self.password

    def get_dictionary_representation(self):
        self.user_dictionary = dict()
        self.user_dictionary["userName"] = self.user_name
        self.user_dictionary["password"] = self.password
        return self.user_dictionary
        
