def cached(maxsize):
    
    def decorator_function(func):
        cache = {}

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
