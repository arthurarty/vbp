import uuid

from django.utils.http import int_to_base36

ID_LENGTH = 12


def generate_uuid():
    """
    Generates random unique id with length is of `ID_LENGTH`
    """
    return int_to_base36(uuid.uuid4().int)[:ID_LENGTH]
