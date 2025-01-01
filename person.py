class Person:
    first_name = ""
    last_name = ""

    def __init__(self, first_name=None, last_name=None):
        self.first_name = first_name
        self.last_name = last_name

    def get_name(self):
        return f"{self.first_name} {self.last_name}"