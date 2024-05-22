from django import template    # Импорт модуля

register = template.Library()


@register.filter
def exponentiation(value, degree):
    """Переменная value - параметр int.
    Переменная degree - параметр int.
    Функция return - возвращает int.
    """
    return value**degree
