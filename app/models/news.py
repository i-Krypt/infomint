class News:
    '''
    news class to define news objects
    '''

   
    def __init__(self,id,name,author,description,url,urlToImage,publishedAt):
        self.id =id
        self.name = name
        self.author = author
        self.description = description
        self.url = url
        self.urlToImage = urlToImage
        self.publishedAt = publishedAt
        