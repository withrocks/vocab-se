#!/usr/bin/env python
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import sessionmaker
"""
import os
try:
    os.remove("./data.sqlite")  # TODO!
except FileNotFoundError:
    pass
"""

Base = declarative_base()
engine = create_engine("sqlite:///data.sqlite")
Session = sessionmaker(bind=engine)
session = Session()

class Job(Base):
    # Contains information about the jobs, e.g. for continuing where we stopped last
    __tablename__ = 'job'

    id = Column(String, primary_key=True)
    processed = Column(Integer)

class Kelly(Base):
    # Represents the frequency data, from kelly.xml
    # Not all values in the source are parsed. Can be further parsed by looking at "source"
    # and updating the version
    __tablename__ = 'kelly'

    id = Column(Integer, primary_key=True)
    # The version of the entry, used if we need to parse more from the source than originally intended
    written_form = Column(String)
    written_form_lower = Column(String, index=True)
    wpm = Column(String)  # TODO: float
    version = Column(Integer)

    def __repr__(self):
        return "<Kelly({0} {1})>".format(self.written_form, self.wpm)


def create_database():
    Base.metadata.create_all(engine)


def _update_job_info(job_id, processed):
    pass

def parse_kelly():
    def parse_kelly_entry(form_representation):
        kelly = Kelly()
        for child in form_representation:
            if child.attrib["att"] == "wpm":
                kelly.wpm = child.attrib["val"]
            elif child.attrib["att"] == "writtenForm":
                kelly.written_form = child.attrib["val"]
        kelly.version = 1
        return kelly

    kelly_meta = session.query(Job).filter_by(id='kelly').first()
    if not kelly_meta:
        kelly_meta = Job(id="kelly")
        session.add()
    print(kelly_meta)

    return


    entry = 0
    max_entries = 5000
    batch = 200
    for i in range(max_entries):
        pass
    from lxml import etree
    for event, element in etree.iterparse("./kelly.xml", tag="FormRepresentation"):
        entry += 1
        if entry == max_entries:
            break
        continue
        kelly = parse_kelly_entry(element)
        session.add(kelly)
        if entry % batch == 0:
            # TODO: I/O bound, so would benefit from simple threading
            session.commit()
        element.clear()
    session.commit()


if __name__ == "__main__":
    import time
    start_at = time.time()
    create_database()
    parse_kelly()
    print(time.time() - start_at)

