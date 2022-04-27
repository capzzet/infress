from django import template
register = template.Library()
menu = [{'title': "Главная", 'url_name': 'home'},
        {'title': "Резюме", 'url_name': 'resume'},
        {'title': "О нас", 'url_name': 'about'},
        {'title': "Блог", 'url_name': 'blog'},
        {'title': "Контакты", 'url_name': 'contacts'}, ]

@register.simple_tag()
def get_menu():
    return menu