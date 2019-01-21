from datetime import date, datetime


def json_serial(obj):
    if isinstance(obj, (date, datetime)):
        return obj.isoformat()
    raise TypeError('Type %s not serializable' % type(obj))
