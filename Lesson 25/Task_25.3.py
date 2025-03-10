from datetime import datetime

class TimestampMixin:
    def __init__(self):
        self._creation_time = datetime.now()
        self._modification_time = self._creation_time

    def get_creation_time(self):
        return self._creation_time

    def get_modification_time(self):
        return self._modification_time

    def update_modification_time(self):
        self._modification_time = datetime.now()

class File(TimestampMixin):
    def __init__(self, name):
        super().__init__()
        self.name = name

    def rename(self, new_name):
        self.name = new_name
        self.update_modification_time()

class User(TimestampMixin):
    def __init__(self, username):
        super().__init__()
        self.username = username

    def change_username(self, new_username):
        self.username = new_username
        self.update_modification_time()

def main():
    file = File("test.txt")
    user = User("john_doe")

    print("File Creation Time:", file.get_creation_time())
    print("File Modification Time:", file.get_modification_time())
    print("User Creation Time:", user.get_creation_time())
    print("User Modification Time:", user.get_modification_time())

    user.change_username("jane_doe")

    print("File Modification Time:", file.get_modification_time())
    print("User Modification Time:", user.get_modification_time())

if __name__ == "__main__":
    main()