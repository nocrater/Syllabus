from database import db, PrimaryKey, Required, Optional


class Direction(db.Entity):
    id = PrimaryKey(int, auto=True)
    klas = Optional('Klas', cascade_delete=True)
    name = Required(str)