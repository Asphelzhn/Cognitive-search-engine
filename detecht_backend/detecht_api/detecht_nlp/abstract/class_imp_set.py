
"""
Henrik & Oscar
"""


class ImpSent:

    def __init__(self):
        # a constructor file needs to contain something, but this is never used, tried without and got errors.
        self.sent = str
        self.rank = int
        self.order = int
        self.start_index = int
        self.end_index = int
        self.score = float
        self.page = int

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

    def set_end_index(self, sent_end):
        self.end_index = sent_end

    def set_score(self, sent_score):
        self.score = sent_score

    def set_page(self, sent_page):
        self.page = sent_page

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

    def get_score(self):
        return self.score

    def get_page(self):
        return self.page
