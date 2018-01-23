from pyblizzard.common.constants import url


# Combines a region constant (subdomain) with the blizzard API path
def build_base_path_from_region(region):
    return 'https://{}.{}'.format(region, url.BLIZZARD_API)
