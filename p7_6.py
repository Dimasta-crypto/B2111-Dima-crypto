def checker(function, ):
    def checker(*args, **kwargs):
        try:
            result = function(*args, **kwargs)
        except Exception as exc:
            print(f"We have a problem - {exc}")
        else:
            print(f"No problem - {result}")

    return checker

@checker
def calculate(expression):
    return eval(expression)


calculate("2+2")
