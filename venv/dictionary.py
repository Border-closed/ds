#Напишите функцию принимающую на вход только ключевые параметры и возвращающую словарь,
# где ключ — значение переданного аргумента, а значение — имя аргумента.
#Если ключ не хешируем, используйте его строковое представление.

def create_dict(**text):
    result = {}
    for key, value in text.items():
        # Преобразование ключа в строку, если он не хешируем
        key_str = str(key) if hash(key) else key
        result[value] = key_str
    return result

# Пример использования функции
my_dict = create_dict(name="Dmitrii", age=34, city="Ekaterinburg")
print(my_dict)