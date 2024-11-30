from django.core.validators import RegexValidator


'''
This regex assumes that you have a clean string,
you should clean the string for spaces and other characters
ДА, я это просто скопировал с инета.
'''

isalphavalidator = RegexValidator(r'^[A-Za-zа-яА-Я]*$',
                             message='Имя должнос одержать только буквы!',
                             code='Invalid name')