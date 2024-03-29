import uuid


def generate_random_email() -> str:
    return str(uuid.uuid4()) + '@mailto.plus'
