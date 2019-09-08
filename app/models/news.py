class News:
    '''
    News class to define news sources objects
    '''

    def __init__(self,id,name,description,url,category,language,country):
        self.id = id
        self.name = name
        self.description = description
        self.url = "https://abcnews.go.com"
        self.category = category
        self.language = language
        self.category = category