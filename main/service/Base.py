from main import db_session
from main import db

class Base(object):
    __model__ = None

    def __init__(self,session = None):
        self.session = session or db_session

    def save(self, model):
        self.session.add(model)
        self.session.commit()
        return model

    def count(self, **kargs):
        return self.session.query(self.__model__).filter_by(**kargs).count()

    def all(self, offset=None, limit=None, order_by=None, desc=False):
        query = self.session.query(self.__model__)
        if order_by is not None:
            if desc:
                query = query.order_by(db.desc(order_by))
            else:
                query = query.order_by(order_by)
        if offset is not None:
            query = query.offset((offset-1)*limit)
        if limit is not None:
            query = query.limit(limit)
        return query.all()

    def find(self, **kargs):
        query = self.session.query(self.__model__).filter_by(**kargs)
        return query

    def first(self, **kargs):
        return self.session.query(self.__model__).filter_by(**kargs).first()

    def get(self, id):
        self.session.expire_all()
        return self.session.query(self.__model__).get(id)

    def create(self, **kargs):
        return self.save(self.__model__(**kargs))

    def session_commit(self):
        self.session.commit()

    def update(self, model, **kwargs):
        for k, v in kwargs.items():
            setattr(model, k, v)
        self.save(model)
        return model

    def delete(self,model):
        self.session.delete(model)
        self.session_commit()

    def __del__(self):
        self.session.close()
