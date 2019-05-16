from contextlib import contextmanager
import traceback


@contextmanager
def supresser(*args):
    try:
        yield
    except args:
        pass


@contextmanager
def retyper(type_from, type_to):
    try:
        yield
    except type_from as e:
        raise type_to(*e.args).with_traceback(e.__traceback__)


@contextmanager
def dumper(stream):
    try:
        yield
    except Exception as e:
        print(repr(e).split('(')[0], ':', *e.args)
        traceback.print_tb(e.__traceback__)
