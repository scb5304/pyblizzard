from pyblizzard import pyblizzard


def build_base_path_from_region(region):
    return 'https://{}.{}'.format(region, pyblizzard.BLIZZARD_API_ROOT)