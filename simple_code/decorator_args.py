class User:
    def __init__(self,name):
        self.name = name
        self.is_logged_in = False



def is_authenticated_decorator(func):
    def wrapper(*args):
        if args[0].is_logged_in:
            func(args[0])
        else:
            print(f'User {args[0].name} is not authenticated')

    return wrapper

@is_authenticated_decorator
def do_something(user : User):
    print(f'This user {user.name} has passed authentication')


new_user = User('John')
new_user.is_logged_in = True

do_something(new_user)