"""user_admin_module.py - User, Privileges, and Admin in one module (9-11)"""


class User:
    def __init__(self, first_name, last_name, state_of_origin="Enugu",
                 program_name="Hackathon 3.0"):
        self.first_name = first_name
        self.last_name = last_name
        self.marital_status = "single"
        self.state_of_origin = state_of_origin
        self.program_name = program_name
        self.login_attempts = 0

    def describe_user(self):
        print(f"\n{self.last_name} {self.first_name} is {self.marital_status}, "
              f"and is from {self.state_of_origin} and is actively participating "
              f"in the {self.program_name} software development program.")

    def greet_user(self):
        print(f"\nGood day {self.last_name} {self.first_name}")

    def increment_login_attempts(self):
        self.login_attempts += 1

    def reset_login_attempts(self):
        self.login_attempts = 0


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
