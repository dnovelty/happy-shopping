def de_yield(func, *args):
    def wrapper(*args):
        res = func(*args)
        res = next(res)
        return res

    return wrapper
