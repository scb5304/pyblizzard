from pyblizzard import pyblizzard


def build_base_path_from_region(region):
    return 'https://{}.{}'.format(region, pyblizzard.BLIZZARD_API_ROOT)

def get_delimited_enum_value_str(enum_objects, str):
    enum_values = []
    for enum_object in enum_objects:
        enum_values.append(enum_object.value)
    return str.join(enum_values)