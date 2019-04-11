class Contact:
    def __init__(self, lName, fName): # explicit constructor for class
        self.lastName = lName
        self.firstName = fName


worker1 = Contact("Smith", "James")
print(worker1.lastName, worker1.firstName) # object.public_property

#newLast = input('Enter the last name: ')

#setattr(worker1, 'lastName', newLast)  # set attribute with new value

print(worker1.lastName, worker1.firstName)

print(getattr(worker1, 'lastName'))  # get existing attribute


class Contact:
    name = ''
    email = ''
    phone = ''


class Person(Contact):
    first_name = ''
    last_name = ''
    name = ''


class Company(Contact):
    industry = ''


class Employee(Person):
    employer = None
    job_title = ''
    office_email = ''
    office_phone = ''
    extension = ''


class Friend(Person):
    relationship = ''


class FamilyMember(Person):
    relationship = ''
    birthday = ''


p = Friend()
p.first_name = 'Laerte'
p.last_name = 'Pereira'
print(p.first_name, p.last_name)
