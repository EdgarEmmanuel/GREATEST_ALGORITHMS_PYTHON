

class User:
    def __init__(self, email):
        self.email = email
        self.delimiterSymbol = self.email.index("@")

    def determineEmailDomain(self):
        return self.email[self.delimiterSymbol+1:]

    def determineEmailUserName(self):
        return self.email[:self.delimiterSymbol]

    def printUserEmailInfo(self):
        username = self.determineEmailUserName()
        domain = self.determineEmailDomain()
        print(f"Your Email Is : {self.email}")
        print(f"Your username is << {username} >> and the domain is << {domain} >>")


if __name__ == "__main__":
    User("risbah.singh@gmail.com").printUserEmailInfo()