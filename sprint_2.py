def decorate_function(decorated_function):
    def decorator(a, b):
        print(f'До выполнения {a}')
        decorated_function(a, b)
        print(f'После выполнения {b}')

    return decorator


@decorate_function
def test(a, b):
    print(f'Сама функция {a}, {b}')


test(1, 2)
