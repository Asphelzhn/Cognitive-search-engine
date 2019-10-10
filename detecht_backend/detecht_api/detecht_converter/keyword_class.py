class keyword_class:
    # Jakob & Carl
    def __init__(self,keyword,weight):
        self.keyword = keyword;
        self.weight = weight;


    def get_keyword_dict(self):
        return {'Keyword':self.keyword,'Weight':self.weight}