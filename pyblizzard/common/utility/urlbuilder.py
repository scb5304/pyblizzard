from pyblizzard.common.constants import url


def build_base_path_from_region(region):
    return 'https://{}.{}'.format(region, url.BLIZZARD_API)


def build_url_from_segments(segments):
    built_url = ''
    for segment in segments:
        built_url += segment + '/'
    return built_url
