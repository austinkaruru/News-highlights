class Articles:

    def __init__(self, author, title, description, url, urlToImage):
        self.author = author
        self.title = title
        self.description = description
        self.url = url
        self.urlToImage = 'https://img.etimg.com/thumb/msid-65766706' + urlToImage
