class User:
    """App user"""
    def __init__(self, trusted=False):
        self.trusted = trusted
    
    def can_login(self):
        """only let trusted users in"""
        return self.trusted


def login(user):
    """Gives access to users w/ privileges"""
    # we implicitly check can login. We say if user can login...
    if user.can_login:
        print("All our secrets!")
    else:
        print("No secrets for you!")

def login_corrected(user):
    """Gives access to users w/ privileges"""
    # Now the way to turn that into an explicit check would be to say, if user can login is true. 
    if user.can_login(): # or use user.can_login() is True
        print("All our secrets!")
    else:
        print("No secrets for you!")

hacker = User(trusted=False)
friend = User(trusted=True)

login(hacker)
#* All our secrets!
login(friend)
#* All our secrets!

login_corrected(hacker)
#* No secrets for you!
login_corrected(friend)
#* All our secrets!