class User:
    def __init__(self, user_name, password):
        self.user_name = user_name
        self.password = password

    def get_user_name(self):
        return self.user_name

    def get_user_password(self):
        return self.password

    def get_dictionary_representation(self):
        self.user_dictionary = dict()
        self.user_dictionary["userName"] = self.user_name
        self.user_dictionary["password"] = self.password
        return self.user_dictionary
        