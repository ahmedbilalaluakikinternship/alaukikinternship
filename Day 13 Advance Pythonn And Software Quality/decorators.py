from functools import wraps
from datetime import datetime


def log_activity(func):

    @wraps(func)
    def wrapper(*args, **kwargs):

        print(f"\n[LOG] Starting: {func.__name__}")

        result = func(*args, **kwargs)

        print(f"[LOG] Completed: {func.__name__}")
        print("[LOG] Time:", datetime.now())

        return result

    return wrapper