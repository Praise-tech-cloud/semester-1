# Worksheet 1.5: Person class

from datetime import date

class Person:
    """
    A Person, with a name and a date of birth.
    """
    def __init__(self, name, birth):
        """
        Creates a Rectangle, given values for width and height.
        """
        # Add code here to check type and value of provided width & height,
        # raising appropriate exceptions if necessary (see README.md)
        self.name = name
        self.birth = birth

        if name <= " ":
            raise ValueError("Name cant be empty")
        
        if not isinstance(name, str): 
            raise TypeError("Name must be a string")
        
        if not isinstance(birth, date):
            raise TypeError("The birth must be a date")

    # Write a constructor here to create and initialize name and
    # birth fields (see README.md for further details)

    # Implement methods initials() and is_birthday() here
    # (see README.md for further details)
    def initials(self):
        return "".join(word[0].upper() for word in self.name.split())

    def is_birthday(self):
        today == date.today()
        return today.month == self.birth.month and today.day == self.birth.day