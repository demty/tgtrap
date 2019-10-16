from tgtrap.state import TgState
from tgtrap.trap import Trap


class HelloState(TgState):
    pass


class TgTrapExample(Trap):
    state = [HelloState]
    init_state = HelloState
