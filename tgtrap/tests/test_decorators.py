from tgtrap.decorators import event
from tgtrap.state import TgState


class Test(TgState):
    name = "test"

    @event(name="test")
    def test_f(self):
        pass


t = Test()
pass
