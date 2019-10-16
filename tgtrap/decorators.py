from typing import Callable, List


def event(name: str):
    def event_inner(f: Callable):
        def wrapper(*args, **kwargs):
            return f(*args, **kwargs)

        wrapper.is_event = True
        wrapper.name = name

        return wrapper

    return event_inner


def event_hook(name: str, listens: List[str]):
    def event_hook_inner(f: Callable):
        def wrapper(*args, **kwargs):
            return f(*args, **kwargs)

        wrapper.is_event_hook = True
        wrapper.name = name
        wrapper.listens = listens

        return wrapper

    return event_hook_inner
