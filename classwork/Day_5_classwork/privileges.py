"""privileges_admin_module.py - Privileges and Admin, User imported separately (9-12)"""
from user_module import User


class Privileges:
    def __init__(self):
        self.privileges = ["can add post", "can delete post", "can ban user"]

    def show_privileges(self):
        print(self.privileges)


class Admin(User):
    def __init__(self, first_name, last_name):
        super().__init__(first_name, last_name)
        self.admin_privileges = Privileges()

    def show_privileges(self):
        self.admin_privileges.show_privileges()
