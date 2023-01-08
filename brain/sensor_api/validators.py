from django.core.exceptions import ValidationError


def validate_command_base_string(value):
    if not "{args}" in value:
        raise ValidationError("Arguments placeholder is missing. Add '{args}'.")
