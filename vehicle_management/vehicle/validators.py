from django.core.validators import RegexValidator

vehicle_number_validator = RegexValidator(
    regex=r'^[A-Z]{2}[0-9]{2}[A-Z]{2}[0-9]{4}$',
    message='Enter a valid Indian vehicle number (e.g. MH02AB1234).'
)