import uuid


def generate_uuid(chars=None, length=8, upper=False):
    """
    Generates a UUID string.

    Args:
        chars (str, optional): A string to be appended to the UUID string. Defaults to None.
        length (int, optional): The length of the UUID string. Defaults to 8.
        upper (bool, optional): Specify whether the UUID characters should be uppercase or lower case. Defaults to False.

    Return:
        string

    Usage:
        >>> generate_uuid(chars="BeneficiaryOrg", length=8, upper=True)
        >>> BeneficiaryOrg-DC4750F5
        >>> generate_uuid(chars="BeneficiaryOrg", length=8, upper=False)
        >>> BeneficiaryOrg-681ffbcb
    """
    uuid_chars = str(uuid.uuid4())[:length]

    if upper:
        uuid_chars = uuid_chars.upper()

    complete_string = ""

    if chars:
        complete_string = f"{chars}-{uuid_chars}"
    else:
        complete_string = uuid_chars

    return complete_string
