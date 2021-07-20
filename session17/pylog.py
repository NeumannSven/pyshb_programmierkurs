

def logger(fn):
    def wrapper(*args, **kwargs):

        r = fn(*args, **kwargs)

        print(f"{fn.__name__} {args} {kwargs}-> {r}")
        return r
    return wrapper

def html(tag):
    def tagfunc(fn):
        def wrapper(*args, **kwargs):
            r = fn(*args, **kwargs)
            return f"<{tag}>{r}</{tag}>"
        return wrapper
    return tagfunc