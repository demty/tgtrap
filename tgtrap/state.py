class TgState:
    name = None

    def __init__(self):
        if not self.name:
            raise NotImplemented("State name should be set")
        self._events = {}
        self._get_class_events()

    def _get_class_events(self):
        for attribute in dir(self):
            attr_obj = getattr(self, attribute)
            if callable(attr_obj):
                is_event = getattr(attr_obj, "is_event", False)
                if is_event:
                    self._events[attr_obj.name] = attr_obj
