from functools import wraps
import time


def profiler(f):
    @wraps(f)
    def wrapper(*args, **kwargs):
        wrapper.last_time_taken = getattr(wrapper, 'last_time_taken', 0)
        wrapper.calls = getattr(wrapper, 'calls', 0)
        wrapper.ptr = getattr(wrapper, 'ptr', False)
        if wrapper.ptr is False:
            wrapper.calls = 0
            wrapper.ptr = (args, kwargs)
        start = time.clock()
        func = f(*args, **kwargs)
        end = time.clock()
        wrapper.calls += 1
        if (args, kwargs) == wrapper.ptr:
            wrapper.ptr = False
        wrapper.last_time_taken = end - start
        return func
    return wrapper
