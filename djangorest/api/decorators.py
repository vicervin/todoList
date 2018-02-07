

def logger(f, *args):
    def new_f(*args):
        print("Entering", f.__name__)
        f(*args)
        print("Entry being created", str(args ))
        print("Exited", f.__name__)

    return new_f