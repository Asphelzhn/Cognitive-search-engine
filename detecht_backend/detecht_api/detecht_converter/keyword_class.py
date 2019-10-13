class keyword_class:
    # Jakob & Carl
    def __init__(self,keyword,weight):
        self.keyword = keyword;
        self.weight = weight;

    def __str__(self):
        return "Keyword: " + str(self.keyword) + " Weight: " + str(self.weight)

    def get_keyword(self):
        return self.keyword

    def get_weight(self):
        return self.weight

    def get_keyword_dict(self):
        return {'Keyword':self.keyword,'Weight':self.weight}