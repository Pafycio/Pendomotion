__author__ = 'Pawel'


class State():
    def __init__(self, surf, prev=None):
        self.prev_state = prev
        self.surf = surf

    def on_update(self):
        pass

    def on_render(self):
        pass

    def on_event(self, event):
        pass

    def get_prev(self):
        return self.prev_state
