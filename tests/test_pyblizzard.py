from pyblizzard.common.enum.locale import Locale
from pyblizzard.common.enum.region import Region
from pyblizzard.pyblizzard import PyBlizzard


class TestPyBlizzard:
    def test_api_instances_not_defined_before_instantiated(self):
        assert not PyBlizzard.diablo
        assert not PyBlizzard.starcraft2
        assert not PyBlizzard.wow

    def test_instantiation_creates_api_instances(self):
        py_blizzard = PyBlizzard('api123', Region.US, Locale.US)
        assert py_blizzard.diablo
        assert py_blizzard.starcraft2
        assert py_blizzard.wow

    def test_set_timeout_applies_to_api_instances(self):
        py_blizzard = PyBlizzard('api123', Region.US, Locale.US)
        py_blizzard.set_timeout(109)
        assert py_blizzard._timeout == 109
        assert py_blizzard.diablo._timeout == 109
        assert py_blizzard.starcraft2._timeout == 109
        assert py_blizzard.wow._timeout == 109
