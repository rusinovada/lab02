def hello(_name):
    # Функция принимает на вход имя и возвращает сообщение
    message = 'Hello world from', _name
    return message


name = input('What is your name?')
print(hello(name))
