from pyblizzard.common.utility.urlbuilder import UrlBuilder


class TestUrlBuilder:
    def test_simple_build(self):
        url_builder = UrlBuilder()
        url = url_builder.add('hello') \
            .add('world') \
            .build()
        assert url == 'hello/world'
