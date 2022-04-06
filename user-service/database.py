from flask_sqlalchemy import SQLAlchemy, Model


class CrudOperations(Model):

    @classmethod
    def create(cls, **kwargs):
        instance = cls(**kwargs)
        return instance.save()

    def update(self, **kwargs):
        for key, val in kwargs.items():
            setattr(self, key, val)
        return self.save() or self

    def save(self):
        db.session.add(self)
        db.session.commit()
        return self

    def delete(self):
        db.session.delete(self)
        return db.session.commit()


db = SQLAlchemy()
