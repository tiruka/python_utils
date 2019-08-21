from datetime import datetime
import functools
import logging

logger = logging.getLogger(__name__)

def elapsed_time(func):
    """
    #####################
    @elapsedtime
    def somefunc():
        print('foobar')
    #####################
    You can get the elapsed time of somefunc() to execute.
    """
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        func_name = func.__qualname__
        start = datetime.now()
        logger.info(f'func_name:{func_name} started')
        result = func(*args, **kwargs)
        t = datetime.now() - start
        logger.info(f'func_name:{func_name} ended: elapsed_time {t}')
        return result
    return wrapper

def args_decorator(func):
    """
    With this decorator function, you can use arguments in the function decorated by this.
    You need to modify or add codes about how to use additional args.
    The below decorated funciton 'elapsed_time_with_args' is an example.
    The funciton 'elapsed_time_with_args' have addition arguments of dargs and dkwargs (d means decorator),
    although those arguments are not used below.
    Attention is that you must use decorator like @elapsed_time_with_args().
    #####################
    @elapsed_time_with_args()
    def somefunc():
        print('foobar')
    #####################
    """
    def param(*args, **kwargs):
        def _wrapper(f):
            return func(f, *args, **kwargs)
        return _wrapper
    return param

@args_decorator
def elapsed_time_with_args(func, *dargs, **dkwargs):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        func_name = func.__qualname__
        start = datetime.now()
        logger.info(f'func_name:{func_name} started')
        result = func(*args, **kwargs)
        t = datetime.now() - start
        logger.info(f'func_name:{func_name} ended: elapsed_time {t}')
        return result
    return wrapper
