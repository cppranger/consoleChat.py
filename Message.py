from colorama import Fore, Style
from Person import Person
import date


class Message:
    id: int = 0
    messages: dict = {}
    _free_id: list = []

    def __init__(self, usr: Person, msg: str, comment=None) -> None:
        self.usr = usr
        self.msg = msg
        self.date = date.getDate()
        self.comment = comment
        self.id = Message.setId()
        Message.messages[self.id] = self

    def getDate(self) -> str:
        return "{}.{}.{}".format(self.date[0], self.date[1], self.date[2])

    def __str__(self) -> str:
        return "From {}, {}:\n{}{}".format(Fore.YELLOW + self.usr.fullName,
                                           Fore.BLUE + self.getDate(), Fore.CYAN + self.msg,
                                           Style.RESET_ALL + '\n-*-*-*-*-*--*-*-*-*-*-*-*-*-*-*-')

    def deleteMessage(self) -> None:
        Message.messages.pop(self.id)
        Message._free_id.append(self.id)

    @staticmethod
    def setId() -> int:
        if len(Message._free_id) != 0:
            return Message._free_id.pop(0)
        else:
            Message.id += 1
            return Message.id - 1
