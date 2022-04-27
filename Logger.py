from datetime import datetime

def get_logs(path):
    def decor(old_function):
        def new_function(*args, **kwargs):
            date_time = datetime.now()
            old_function_name = old_function.__name__
            result = old_function(*args, **kwargs)
            with open(path, 'w', encoding= 'utf-8') as file:
                file.write(f'Дата/время: {date_time}\n'
                           f'Имя функции: {old_function_name}\n'
                           f'Аргументы: {args, kwargs}\n'
                           f'Результат: {result}\n')
            return result
        return new_function
    return decor



