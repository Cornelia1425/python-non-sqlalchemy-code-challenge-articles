class Article:
    all =[]
    def __init__(self, author, magazine, title):
        self.author = author #we don't want to pass the setter method, we want to call the setter method. if we use self._author, we just take whatever value we give to it, and it will go into getter for later people get.
        self._magazine = magazine

        # if not isinstance(title, str):
        #     raise Exception("title must be a string")
        # elif len(title) not in range(5,51):
        #     raise Exception("title must be 5-50 character!")
        # self._title = title
        self.title = title
        Article.all.append(self)

    @property
    def title(self):
        return self._title
    @title.setter
    def title(self, value):
        if hasattr(self, 'title'):
            print ("title already exists cannot be changed")
        elif (not isinstance(value, str)) or (len(value) not in range(5,51)):
            print ("title must be a 5-50 character string")             # raise Exception("title must be 5-50 character!")
        else:
            self._title=value
        
    @property 
    def author(self):
        return self._author #not self.author or it will call itself    
    @author.setter

    def author(self, value):
        if not isinstance(value, Author):
            print ("input value not an Author class")
        self._author = value

    @property
    def magazine(self):
        return self._magazine
    
    @magazine.setter
    def magazine(self, value):
        if not isinstance(value, Magazine):
            print ("input value not an Magazine class")
        self._magazine = value


        
class Author:
    def __init__(self, name):
        # self.name = name
        if hasattr(self, 'name'):
            print ("name already exists cannot be changed")
        elif type(name)!=str or len(name) == 0:
            print ("author name must be a string and more than 0 character!")
        # elif len(name) == 0:
            # print ("author name must be more than 0 character!")
        else:
            self._name=name

        #if i don't return inside the if and elif, i continue to run the code, so i need else, here. if I have return in both if and elif, i don't need to add else.
        
     

    @property
    def name(self):
        return self._name

    # @name.setter
    # def name(self, value):
    #     if type(value)!=str:
    #         raise Exception
    #     elif len(value) == 0:
    #         raise Exception
    #     self._name = value

    def articles(self):
        return [article for article in Article.all if isinstance(article, Article) and article.author == self]
 

    def magazines(self):

        return list(set(article.magazine for article in Article.all if isinstance(article.magazine, Magazine) and article.author == self))
      
    

    def add_article(self, magazine, title):
        article = Article(self, magazine, title)
        self.articles().append(article)
        return article

    def topic_areas(self):
        if self.articles() == []:
            return None
        else:
            return list(set(article.magazine.category for article in Article.all if article.author ==self))



class Magazine:
    def __init__(self, name, category):
        self._name = name  
        self._category = category

    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self, value):
        if type(value)!= str:
            print ("magazine name must be a string")
            return
        elif len(value) not in range(2,17):
            print ("magazine name must be 2-16 character!")
            return
        self._name = value 
        #not self._name(value)

    @property
    def category(self):
        return self._category
    
    @category.setter
    def category(self,value):
        if not isinstance(value, str):
            print ("must be a string")
        elif len(value) != 0:
            self._category = value


    def articles(self):
        return [article for article in Article.all if isinstance(article, Article) and article.magazine == self] 
        # a list comprehension

    def contributors(self):
        return list(set(article.author for article in Article.all if isinstance(article.author, Author) and article.magazine == self))
        #returns None of the author has no articles

    def article_titles(self):
        if self.articles()==[]:
            return None
        else:
            return [article.title for article in Article.all if article.magazine ==self]

    def contributing_authors(self):
        all_magazine_authors = list(article.author for article in Article.all if isinstance(article.author, Author) and article.magazine == self)
        count_dict={}
        duplicate_authors = []
        for e in all_magazine_authors:
            if e in count_dict:
                count_dict[e]+=1
            else:
                count_dict[e]=1
        for e, count in count_dict.items():
            if count >=2:
                duplicate_authors.append(e)
       

        if duplicate_authors == []:
            return None
        else: 
            return duplicate_authors