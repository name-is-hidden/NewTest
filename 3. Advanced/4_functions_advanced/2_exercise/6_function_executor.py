def func_executor(*args):
    result = list()

    for operation, parameters in args:
        function_result = operation(*parameters)
        result.append(f"{operation.__name__} - {function_result}")

    return "\n".join(result)
