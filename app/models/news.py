class Sources:
    '''
    News class to define news sources objects
    '''

    def __init__(self,id,name,author,description,url,category,language,country):
        self.id = id
        self.name = name
        self.author = author
        self.description = description
        self.url = url
        self.category = category
        self.language = language
        self.country = country


# class Articles: