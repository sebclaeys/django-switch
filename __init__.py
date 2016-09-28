__author__ = 'sclaeys'


from switches.models import Switch

def is_enabled(name, default=False):
    return Switch.values.get(name, default=default)

