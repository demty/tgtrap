class MainTg:
    states = [InitState, StatesGroup,...]
    init_state = InitState


class StatesGroup:
    states = [InitStateAnother, ...]
    def before_message_func(self):
        if message == 'to main':
            self.call_before('init.print_text')
            self.call_after()
            self.call('init.finished')  # transits state


class InitState:
    name = 'init'

    def on_message(self):
        self.event.spawn('finished')
        return [msgs]

    def on_inline(self):
        return [msgs]

    def on_state_exit(self):
        pass

    def on_state_enter(self):
        pass

    def on_error(self, error, kind):
        pass

    @event(name='print_text')
    def some_text_print(self):
        pass

    @event_hook(name='hook_name', listens=['init.finished'])
    def after_init(self):
        # if we want to set current state to class state
        self.capture_state()


"""
Be careful, race condition must be mentioned on startup
For example two states listens same event
User must be warned or restricted from executing such behaviour
Also there can be situation, when
"""
