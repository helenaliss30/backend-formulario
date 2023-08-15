class Register:
    def __init__(
        self,
        email,
        password,   
    ):
        self.email=email
        self.password=password
        
    def toDBCollection(self):
        return {
            "email": self.email,
            "password": self.password,
        }
