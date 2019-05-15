import sys
from functools import wraps


def takes(*a):
    def decorator(f):
        @wraps(f)
        def check(*args):
            for i in range(min(len(a), len(args))):
                    if isinstance(args[i], a[i]) == False:
                        raise TypeError
            return f(*args)
        return check
    return decorator
exec(sys.stdin.read())
