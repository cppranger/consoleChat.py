from Person import Person
from Message import Message


class User(Person):

    def __init__(self, firstName: str, secondName: str, birthday: tuple) -> None:
        super().__init__(firstName, secondName, birthday)
        self.email = User.setEmail(self)

    def setEmail(self) -> str:
        email = str(self.id)
        while len(email) < 6:
            email = '0' + email
        email = 'admin{}@company.com'.format(email)
        return email

    def modifyMessage(self, msg: Message, txt: str) -> None:
        if self == msg.usr:
            msg.msg = txt
        else:
            print("Access denied! You can modify only your messages!")