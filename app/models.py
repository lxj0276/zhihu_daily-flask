from . import db


class News(db.Model):
    id           = db.Column(db.Integer, primary_key=True)
    news_id      = db.Column(db.Integer)
    date         = db.Column(db.String(32))
    title        = db.Column(db.String(256))
    share_url    = db.Column(db.String(256))
    image_name   = db.Column(db.String(256))
    image_file   = db.Column(db.String(256))

    def __repr__(self):
        return '<Title %r>' % self.title
