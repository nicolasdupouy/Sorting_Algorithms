import functools


def time_with_one_million_calls(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        import timeit
        start_time = timeit.default_timer()
        for t in range(1000000):
            func(*args, **kwargs)
        elapsed_time = timeit.default_timer() - start_time
        print(f'function [{func.__name__}] finished in {int(elapsed_time * 1000)} ms (launched 1 million times)')
    return wrapper
