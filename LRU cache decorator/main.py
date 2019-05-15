from functools import wraps
from collections import OrderedDict


def cache(N):
    def decorator(f):
        @wraps(f)
        def memorize(*args, **kwargs):
            memorize.cache = getattr(memorize, 'cache', OrderedDict())
            key = (tuple(args), hash(tuple(sorted(kwargs.items()))))
            if key not in memorize.cache:
                new_value = f(*args, **kwargs)
                memorize.cache[key] = new_value
                if len(memorize.cache) > N:
                    memorize.cache.popitem(last=False)
                else:
                    return memorize.cache[key]
            return memorize.cache[key]
        return memorize
    return decorator
