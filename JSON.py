import json
class JsonSerializable(object):

    def serialize(self):
        return json.dumps(self.__dict__)

    def __repr__(self):
        return self.serialize()

    @staticmethod
    def dumper(obj):
        if "serialize" in dir(obj):
            return obj.serialize()

        return obj.__dict__

class name(JsonSerializable):
    def __init__(self, name):
        self.name = name

    def get_name(self):
        return self.name    

obj1 = name("Manish")
j_object = json.dumps( obj1 , default=JsonSerializable.dumper)
print(j_object)
