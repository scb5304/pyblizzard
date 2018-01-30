import jsonpickle


def get_delimited_enum_value_str(enum_objects, str):
    enum_values = []
    for enum_object in enum_objects:
        enum_values.append(enum_object.value)
    return str.join(enum_values)

def print_response_object(response_object):
    print(jsonpickle.encode(response_object, unpicklable=False), '\n')
