def cached(maxsize):
    def decorator_function(func):
        cache = {}
        if maxsize <= 0:
            return 0

        def wrapper(*args, **kwargs):
            hash_value = hash(tuple(kwargs.items()))
            key = (args, hash_value)
            res = 0
            if key not in cache:
                res = func(*args, **kwargs)
                if len(cache.keys()) < maxsize:
                    cache[key] = res
                else:
                    return res

            return cache[key]

        return wrapper

    return decorator_function


if __name__ == '__main__':
    print("There is a '@cached' decorator")