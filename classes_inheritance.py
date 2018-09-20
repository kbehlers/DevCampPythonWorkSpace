class User:
    def __init__(self, email, first_name, last_name):
        self.email = email
        self.first_name = first_name
        self.last_name = last_name

    def greeting(self):
        return f'Hi {self.first_name} {self.last_name}'

class AdminUser(User):
    def __init__(self,email, first_name, last_name, middle_name):
        self.middle_name = middle_name
        #define attribute middle name, but then just inherit the definitions of the parent for email, first_name, last_name
        super().__init__(email,first_name,last_name)
    def active_users(self):
        return self.middle_name


tiffany = AdminUser('tiffany@devcamp.com', 'Tiffany', 'Hudgens', 'Jane')

kristine = User('kristine@devcamp.com', 'Kristine', 'Hudgens')

print(tiffany.active_users())
print(tiffany.greeting())
