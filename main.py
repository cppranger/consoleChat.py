"""
I want to implement a real console chat (or a forum).
So this is just an OOP prototype, idk really if i can do it, but i'll try ofc... :)
"""


from Admin import Admin
from User import User
from Message import Message
from Forum import Forum


if __name__ == '__main__':
    admin1 = Admin('Jeff', 'Richards', (5, 6, 1979))
    usr1 = User('James', 'Polish', (16, 2, 1986))
    usr2 = User('Polly', 'Williams', (14, 12, 2005))
    msg1 = Message(admin1, "Hello everyone!\nI'm happy to introduce you THE 1ST MESSAGE on this forum!")
    msg2 = Message(usr1, "Jeez mate! I've been waiting for so long! XD")
    msg3 = Message(usr1, "Jeff, where tf r u? :)")
    msg4 = Message(usr2, "Hello, guys! ~^_^~")
    forum = Forum()

    print(forum)

    Admin.modifyMessage(msg3, "Jeff, where r u?")
    msg5 = Message(admin1, "James, plz do not swear, it's prohibited here...")
    msg6 = Message(usr1, "Jeff f off, BTW there's a gurl?")
    usr1.modifyMessage(msg4, "it doesn't work, huh")

    forum.updateForum()
    print(forum)
