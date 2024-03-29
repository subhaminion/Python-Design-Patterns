import json


class Person(object):
    def __init__(self, first_name=None, last_name=None):
        self.first_name = first_name
        self.last_name = last_name

    def name(self):
        return ("%s %s" % (self.first_name, self.last_name))

    @classmethod
    def get_all(self):
        """
        return all people inside db.txt as list of Person objects
        """
        database = open("db.txt", "r")
        result = []
        json_list = json.loads(database.read())
        for item in json_list:
            person = Person(item['first_name'], item['last_name'])
            result.append(person)
        return result
