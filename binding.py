from pony.orm import sql_debug
from database import db
from model import direction, human, klas, result, student, studying, subject, syllabus, teacher, topic

sql_debug(False)
db.bind(provider='sqlite', filename='bib.sqlite3', create_db=True)
db.generate_mapping(create_tables=True)
