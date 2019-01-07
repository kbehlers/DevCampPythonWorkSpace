#TODO add required Django imports
from datetime import date

class Person(Model):
    name = CharField(max_length=100) #Django Charfield null-true still defaults to empty string, thus redundant
    birthdate = DateField()
    phone_number = CharField(max_length=25)
    email_address = EmailField()
    CONTACT_TYPE_CHOICES = (
        ("EMAIL", "Email"),
        ("PHONE", "Phone"),
    )
    contact_type = CharField(max_length=10,choices=CONTACT_TYPE_CHOICES,default="EMAIL")
    
    @property
    def age(self):
        today = date.today()
        max_age = today.year - self.birthdate.year
        #Tuple comparison yields bool. Comparision starts at 0 position and moves on if needed
        today_is_before_birthday = (today.month, today.day) < (self.birthdate.month, self.birthdate.day)
        
        if today_is_before_birthday:
            true_age = max_age - 1
        else:
            true_age = max_age
        return true_age
    @age.setter
    def age(self, value):
        raise AttributeError("Change birthdate attribute to modify age attribute")

    @property
    def first_name(self):
        return self.name.split(' ')[0]
    @first_name.setter
    def first_name(self, value):
        raise AttributeError("Change the name attribute to modify the first_name")
