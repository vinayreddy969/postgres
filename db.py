import config
from sqlalchemy import Column, Integer, Text
from sqlalchemy.orm import declarative_base




# Define a model
Base = declarative_base()


class User(Base):
    __tablename__ = "my_table2"
    id = Column(Integer, primary_key=True)
    name = Column(Text)
    age = Column(Integer)


def insert_data():
    new_user = User(age="71", name="limbanna")
    config.session.add(new_user)
    config.session.commit()
    print("data inserted successfully")


# Fetch all records
if __name__ == "__main__":
    insert_data()
    config.session.close()

users = config.session.query(User).all()
for user in users:
    print(f"ID: {user.id}, Name: {user.name}, Age: {user.age}")
