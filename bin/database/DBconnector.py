


class LoginData():
    """basic login class containing all the login info for the bot"""
    token = ""
    def __init__(self, token):
        self.token = token
        


def login():
    """pulls from the database the bot's token and otherdata"""
    return LoginData()
