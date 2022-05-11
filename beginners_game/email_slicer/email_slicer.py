

class User:
    def __init__(self, email):
        self.email = email

    def determineEmailDomain(self):
        pass

    def determineEmailUserName(self):
        pass

    def printUserEmailInfo(self):
        username = self.determineEmailUserName()
        domain = self.determineEmailDomain()
        print(f"Your username is {username} and the domain is {domain}")


if __name__ == "__main__":
    User("risbah@gmail.com").printUserEmailInfo()