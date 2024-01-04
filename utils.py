class Credential:
    amount = 0

    def __init__(self, Username, Password) -> str:
        self.Username = Username
        self.Password = Password
    # user func
    def value_of_Username(self) -> str:
        return self.Username
    # pass func
    def value_of_Password(self) -> str:
        return self.Password

    
 # for storing passwords       
class StoredCredential(Credential):
    def __init__(self, Username, Password, website) -> str:
        super().__init__(Username, Password)
        self.website = website

    def value_of_website(self) -> str:
        return self.website






