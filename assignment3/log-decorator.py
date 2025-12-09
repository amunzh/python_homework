#TASK 1
import logging
logger = logging.getLogger(__name__ + "_parameter_log")
logger.setLevel(logging.INFO)
logger.addHandler(logging.FileHandler("./assignment3/decorator.log","a"))

def logger_decorator(func):
    def wrapper(*args, **kwargs):
        position = list(args) if args else 'none'
        keyword = dict(kwargs) if kwargs else 'none'
        ret_result = func(*args, **kwargs)
        logger.log(logging.INFO, f'function: {func.__name__}')
        logger.log(logging.INFO, f'positional parameters: {position}')
        logger.log(logging.INFO, f'keyword parameters: {keyword}')
        logger.log(logging.INFO, f'return: {ret_result}')
        return ret_result
    return wrapper

@logger_decorator
def hello_wrd():
    print('Hello World!')

@logger_decorator
def param_func(x):
    return True

@logger_decorator
def keyword_func(none,**kwargs):
    return logger_decorator


hello_wrd()
param_func([3,4,6,12,33])
keyword_func({'name': 'Amanda', 'age':66})