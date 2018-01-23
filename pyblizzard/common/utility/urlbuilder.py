class UrlBuilder:
    _segments = None
    _use_initial_slash = False
    _use_trailing_slash = False

    def __init__(self, **kwargs):
        self._segments = []
        if 'use_initial_slash' in kwargs:
            self._use_initial_slash = kwargs['use_initial_slash']
        if 'use_trailing_slash' in kwargs:
            self._use_trailing_slash = kwargs['use_trailing_slash']

    def add(self, segment):
        self._segments.append(segment)
        return self

    def build(self):
        url = '/'.join(self._segments)
        if self._use_initial_slash:
            url = '/' + url
        if self._use_trailing_slash:
            url = url + '/'
        return url
