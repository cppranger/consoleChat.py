from Person import Person
from Message import Message


class Admin(Person):

    def __init__(self, firstName: str, secondName: str, birthday: tuple) -> None:
        super().__init__(firstName, secondName, birthday)
        self.email = Admin.setEmail(self)

    def setEmail(self) -> str:
        email = str(self.id)
        while len(email) < 6:
            email = '0' + email
        email = 'admin{}@company.com'.format(email)
        return email

    @staticmethod
    def modifyMessage(msg: Message, txt: str) -> None:
        msg.msg = txt
