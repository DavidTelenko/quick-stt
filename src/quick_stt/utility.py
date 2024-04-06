import time
import functools as ft


def flatten_dict(d: dict, parent_key: str = "", sep: str = "_") -> dict:
    items = []
    for k, v in d.items():
        new_key = f"{parent_key}{sep}{k}" if parent_key else k
        if isinstance(v, dict):
            items.extend(flatten_dict(v, new_key, sep=sep).items())
        else:
            items.append((new_key, v))
    return dict(items)


def time_this(to):
    def timed_redirector(fn):
        @ft.wraps(fn)
        def timed_wrapper(*args, **kwargs):
            start_time = time.time()
            result = fn(*args, **kwargs)
            to(time.time() - start_time)
            return result

        return timed_wrapper

    return timed_redirector


class Singleton(type):
    _instances = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super(Singleton, cls).__call__(*args, **kwargs)
        return cls._instances[cls]
