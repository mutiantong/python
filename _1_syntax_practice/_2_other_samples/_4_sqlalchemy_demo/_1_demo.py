#!/usr/bin/python
# -*- coding:utf-8 -*-

from sqlalchemy import create_engine
from sqlalchemy import Column
from sqlalchemy.types import String, Integer, CHAR, BIGINT
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker


engine = create_engine('mysql://root:123456@192.168.8.162/cinder?charset=utf8', echo=True)
BaseModel = declarative_base()
Session = sessionmaker(bind=engine)

class User(BaseModel):
    __tablename__ = 'migrate_version'

    repository_id = Column(String(32), primary_key=True)
    repository_path = Column(String(32), server_default='', nullable=False)
    version = Column(Integer, nullable=False)


def main():
    session = Session()
    val = session.query(User).filter(User.repository_id == 'storage_manage').all()

    if len(val) == 0:
        new_value = User(repository_id='storage_manage', repository_path='/opt/stack/cinder/cinder/api/cloudsure/db', version=0)
        session.add(new_value)
        session.commit()
    session.close()

if __name__ == '__main__':
    main()