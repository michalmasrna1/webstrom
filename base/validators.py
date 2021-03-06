from django.core.validators import RegexValidator

phone_number_validator = RegexValidator(
    regex=r'^(\+\d{1,3}\s?\d{3}\s?\d{3}\s?\d{3}|\d{4}\s?\d{3}\s?\d{3})$',
    # ale prejde to tym aj bez medzier
    message='Zadaj telefónne číslo vo formáte +421 123 456 789 alebo 0912 345 678.',
)
