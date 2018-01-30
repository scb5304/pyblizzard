from pyblizzard.common.utility.urlbuilder import UrlBuilder


class TestUrlBuilder:
    def test_simple_build(self):
        url_builder = UrlBuilder()
        url = url_builder.add('hello') \
            .add('world') \
            .build()
        assert url == 'hello/world'

    def test_use_trailing_slash(self):
        url_builder = UrlBuilder(use_trailing_slash=True)
        url = url_builder.add('hello') \
            .add('world') \
            .add('2') \
            .build()
        assert url == 'hello/world/2/'

    def test_use_initial_slash(self):
        url_builder = UrlBuilder(use_initial_slash=True)
        url = url_builder.add('hello') \
            .add('world') \
            .add('90') \
            .add('1') \
            .build()
        assert url == '/hello/world/90/1'

    def test_use_initial_and_trailing_slash(self):
        url_builder = UrlBuilder(use_initial_slash=True, use_trailing_slash=True)
        url = url_builder.add('hello') \
            .add('world') \
            .add('90') \
            .add('1') \
            .build()
        assert url == '/hello/world/90/1/'

