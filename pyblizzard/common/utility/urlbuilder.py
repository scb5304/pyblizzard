from pyblizzard.common.constants import url


# Combines a region constant (subdomain) with the blizzard API path
def build_base_path_from_region(region):
    return 'https://{}.{}'.format(region, url.BLIZZARD_API)


# Concatenates the strings in the passed list with '/' separators. Does not end with a '/'.
def build_url_from_segments(segments):
    built_url = ''
    for segment in segments:
        built_url += segment + '/'
    return built_url[:-1]
