from Message import Message


class Forum:
    forum: str = ''

    def __new__(cls):
        if not hasattr(cls, 'instance'):
            cls.instance = super(Forum, cls).__new__(cls)
            Forum.forum = Forum.getMessages()
        return cls.instance

    def __str__(self):
        return self.forum

    @staticmethod
    def updateForum() -> None:
        Forum.forum = []
        Forum.forum = Forum.getMessages()

    @staticmethod
    def getMessages():
        msgList: str = '\nNew forum messages:\n'
        for msg in Message.messages:
            msgList += '\n'
            msgList += Message.messages[msg].__str__()
            msgList += '\n'
        msgList += 'Message list ends.\n'
        return msgList
