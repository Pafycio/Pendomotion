__author__ = 'Pawel'


class State():
    def __init__(self, surf, prev=None):
        """

        :param surf:
        :param prev:
        :return:
        """
        self.prev_state = prev
        self.surf = surf

    def on_update(self):
        """

        :return:
        """
        pass

    def on_render(self):
        """

        :return:
        """
        pass

    def on_event(self, event):
        """

        :param event:
        :return:
        """
        pass

    def get_prev(self):
        """

        :return:
        """
        return self.prev_state
