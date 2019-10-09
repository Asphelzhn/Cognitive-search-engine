
"""
Henrik & Oscar
"""


class ImpSent:
    sent = str("")
    rank = int
    order = int
    start_index = int
    end_index = int


def set_sent(self, sent_input):
    self.sent = sent_input


def set_rank(self, sent_rank):
    self.rank = sent_rank


def set_order(self, sent_order):
    self.order = sent_order


def set_start_index(self, sent_start):
    self.start_index = sent_start


def set_end_index(self, sent_end):
    self.end_index = sent_end


def get_sent(self):
    return self.sent


def get_rank(self):
    return self.rank


def get_order(self):
    return self.order


def get_start_index(self):
    return self.start_index


def get_end_index(self):
    return self.end_index

