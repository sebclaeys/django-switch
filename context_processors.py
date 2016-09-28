import switches.models as model

def switches_loader(request):
    return {'switch': model.Switch.values.get_all()}

