from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy import Column, String, Integer, Boolean, ForeignKey, Date

engine = create_engine('sqlite:///../instance/flaskr.sqlite')
Session = sessionmaker(bind=engine)
Base = declarative_base()

class Post(Base):
    __tablename__ = 'post'
    id = Column(Integer, primary_key=True)
    author_id = Column(Integer)
    created = Column(Date)
    title = Column(String)
    body = Column(String)

session = Session()
posts = session.query(Post).all()
print ('\nAll posts titles:')
for post in posts:
        print(f'{post.title}: {post.body}.')
