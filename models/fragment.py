from ..extensions import db

class Fragment(db.Model):
    __tablename__ = "fragment"
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    fragmento = db.Column(db.String(150))
    titulo = db.Column(db.String(50))
    dt = db.Column(db.Date)
    #fim = db.Column(db.Date)

    def __repr__(self):
        return "<Fragment(fragmento={}, titulo={}, dt={})>".format(self.fragmento, self.titulo, self.dt)