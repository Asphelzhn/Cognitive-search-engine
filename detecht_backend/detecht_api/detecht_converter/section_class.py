class section_class:
    start = 0
    end = 0

    def __init__(self, start, end):
        self.start = start
        self.end = end


    def add_keyword(self, keyword, weight):
        print(keyword + " " + str(weight))