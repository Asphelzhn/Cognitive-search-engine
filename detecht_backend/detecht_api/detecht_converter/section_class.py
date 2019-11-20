from detecht_api.detecht_converter.keyword_class import keyword_class


class section_class:
    start = 0
    end = 0
    keywords = list()

    def __init__(self, start, end):
        self.start = start
        self.end = end

    def __str__(self):
        return "Start: " + str(self.start) + " End: " + str(self.end)

    def add_keyword(self, keyword, weight):
        self.keywords.append(keyword_class(keyword, weight))

    def get_start(self):
        return self.start

    def get_end(self):
        return self.end

    def get_section_dict(self):
        section_keywords = list()
        for section_keyword in self.keywords:
            section_keywords.append(section_keyword.get_keyword_dict())

        return {'start': self.start, 'end': self.end, 'section_keyword': section_keywords}
