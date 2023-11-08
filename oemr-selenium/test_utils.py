def read_properties():
    properties = {}
    with open('secret.config', 'r') as file:
        for line in file:
            if '=' in line:
                key, value = line.strip().split('=', 1)
                key = key.strip()  # Strip spaces from key
                value = value.strip()  # Strip spaces from value
                properties[key] = value
    return properties

def get_user():
    return read_properties().get('username', None)

def get_pass():
    return read_properties().get('password', None)
