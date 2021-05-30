class Person:
    id: int = 0
    persons: dict = {}
    _free_id: list = []

    def __init__(self, firstName: str, secondName: str, birthday: tuple) -> None:
        self.firstName = firstName
        self.secondName = secondName
        self.birthday = birthday
        self.id = Person.setId()
        Person.persons[self.id] = self
        self.email = Person.setEmail(self)

    def setEmail(self) -> str:
        email = str(self.id)
        while len(email) < 6:
            email = '0' + email
        email = 'pers{}@company.com'.format(email)
        return email

    """
    so f tired of not understanding how this f __del__ works heh
    so it just dels person with deletePerson method + del w/o overloading del itself
    fock fock fock
    same s with deleteMessage btw
    """

    """
    def __del__(self):
        Person.persons.pop(self.id)
        Person._free_id.append(self.id)
        del self
    """

    def __str__(self) -> str:
        return "Person: {}: {} {}.\nemail: {}\nbirthday: {}".format(
            self.id, self.firstName, self.secondName,
            self.email, '{}.{}.{}'.format(self.birthday[0], self.birthday[1], self.birthday[2]))

    def __repr__(self) -> str:
        return "Person: {}: {} {}.".format(
            self.id, self.firstName, self.secondName,
            )

    def deletePerson(self) -> None:
        Person.persons.pop(self.id)
        Person._free_id.append(self.id)

    @property
    def fullName(self) -> str:
        return "{} {}".format(self.firstName, self.secondName)

    @fullName.setter
    def fullName(self, name: str) -> None:
        first, second = name.split(' ')
        self.firstName = first
        self.secondName = second

    @staticmethod
    def setId() -> int:
        if len(Person._free_id) != 0:
            return Person._free_id.pop(0)
        else:
            Person.id += 1
            return Person.id-1

    @staticmethod
    def getPersonsList() -> dict:
        return Person.persons

