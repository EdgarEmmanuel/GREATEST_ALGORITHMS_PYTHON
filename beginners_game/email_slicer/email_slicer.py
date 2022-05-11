

class User:
    def __init__(self, email):
        self.email = email
        self.delimiterSymbol = None

    def determineEmailDomain(self):
        self.delimiterSymbol = self.email.index("@")
        return self.email[self.delimiterSymbol+1:]

    def determineEmailUserName(self):
        self.delimiterSymbol = self.email.index("@")
        return self.email[:self.delimiterSymbol]

    def printUserEmailInfo(self):
        username = self.determineEmailUserName()
        domain = self.determineEmailDomain()
        print(f"Your username is {username} and the domain is {domain}")


if __name__ == "__main__":
    User("risbah.singh@gmail.com").printUserEmailInfo()