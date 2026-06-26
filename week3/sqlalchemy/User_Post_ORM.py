from sqlalchemy import Column,Integer,String,ForeignKey,create_engine,Text
from sqlalchemy.orm import sessionmaker,declarative_base,relationship
DATABASE_URL = "postgresql+psycopg2://postgres:dushy123@localhost:5432/TestDB"
engine = create_engine(DATABASE_URL)
Base = declarative_base()
sessionlocal = sessionmaker(bind=engine)
class User(Base):
    __tablename__="users"
    id = Column(Integer,primary_key=True)
    name = Column(String)
    posts = relationship("Posts",back_populates="users")
class Posts(Base):
    __tablename__="posts"
    id = Column(Integer,primary_key=True)
    user_id = Column(Integer,ForeignKey("users.id"))
    post = Column(Text)
    users = relationship("User",back_populates="posts")
Posts.__table__.drop(engine,checkfirst=True)
User.__table__.drop(engine,checkfirst=True)
Base.metadata.create_all(engine)
session = sessionlocal()
alice = User(name="alice")
bob = User(name="bob")
charlie = User(name="charlie")
david = User(name="david")
eve = User(name="eve")
post1=Posts(post="blog about mountain")
post2=Posts(post="blog about mountain")
post3=Posts(post="blog about mountain")
post4=Posts(post="vlog on travel")
post5=Posts(post="vlog on travel")
post6=Posts(post="upload a photo")
post7=Posts(post="vlog on raining")
alice.posts.append(post1)
bob.posts.append(post2)
charlie.posts.append(post3)
alice.posts.append(post6)
bob.posts.append(post4)
charlie.posts.append(post5)
eve.posts.append(post7)
session.add_all([alice,bob,charlie,david,eve])
session.commit()
#inner-join
# result = session.query(User,Posts).join(Posts,(User.id==Posts.user_id)).all()
# for user,post in result:
#     print(user.name,post.post)
#outer-join
user = session.query(Posts).filter(Posts.user_id==5).first()
user.post = "vlog on trecking"
result = session.query(User,Posts).outerjoin(Posts,User.id==Posts.user_id).all()
delete_user = session.query(User).filter(User.name=="david").first()
session.delete(delete_user)
session.commit()
for user,post in result:
    if post:
        print(user.name,post.post)
    else:
        print(user.name,None)
result = session.query(Posts).all()
for row in result:
    print(row.post)
delete = session.query(User).all()
for row in delete:
    print(row.name)

