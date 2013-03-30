from sqlalchemy import create_engine, Column, Integer, String, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, backref, sessionmaker

class Base(object):
    id = Column(Integer, primary_key=True)
    name = Column(String(250))

Base = declarative_base(cls=Base)


class Project(Base):
    __tablename__ = 'projects' 
    project_type_id = Column(Integer, ForeignKey('project_types.id'))

    project_type = relationship("ProjectType",
            backref=backref("projects", uselist=False))
    tasks = relationship('Task')
    config = relationship('Config')

    def __repr__(self):
        return "<Project('%s')>" % (self.name)

class ProjectType(Base):
    __tablename__ = 'project_types'

    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return "<ProjectType('%s')>" % (self.name)

class Config(Base):
    __tablename__ = 'project_config'
    value = Column(String(250))
    project_id = Column(Integer, ForeignKey('projects.id'))
    
    def __repr__(self):
        return "<Config('%s', '%s')>" % (self.name, self.value)


class Task(Base):
    __tablename__ = 'codebase_tasks'
    ticket = Column(Integer)
    priority = Column(String(50))
    project_id = Column(Integer, ForeignKey('projects.id'))

    def __repr__(self):
        return "<Task('%s', '%s')>" % (self.name, self.ticket)

engine = create_engine('sqlite:///db.sqlite', echo=True)
Base.metadata.create_all(engine)
Session = sessionmaker(bind=engine)

# Setup the initial db data
session = Session()
session.add_all([
    ProjectType('CodebaseHQ'),
    ProjectType('Custom')])
session.commit()


