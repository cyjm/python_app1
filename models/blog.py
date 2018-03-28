import uuid
import datetime
from models.post import Post
from database import Database

__author__ = 'cyjm'


class Blog(object):

    def __init__(self, author, title, content, id = None):
        self.author = author
        self.title = title
        self.content = content
        self.id = uuid.uuid4().hex if id is None else id

    def new_post(self):
        title = input('Enter post title: ')
        content = input('Enter post content: ')
        date = input("Enter post date in format DDMMYYYY(leave blank for today's date): ")
        if date == "":
            date = datetime.datetime.utcnow()
        else:
            date = datetime.datetime.strptime(date, "%d%m%Y")
        post = Post(blog_id=self.id,
                    title = title,
                    content = content,
                    author = self.author,
                    date = date)
        post.save_to_mongo()

    def get_posts(self):
        return Post.from_blog(self.id)

    def save_to_mongo(self):
        Database.insert("blogs", self.json())

    def json(self):
        return {
            'author': self.author,
            'title': self.title,
            'content': self.content,
            'id': self.id
        }

    @classmethod
    def from_mongo(cls,id):
        blog_data = Database.find_one('blogs', {'id': id})
        return cls(blog_data['author'],
                   blog_data['title'],
                   blog_data['content'],
                   blog_data['id'])
