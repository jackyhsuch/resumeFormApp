from app import db

class Applicant(db.Model):
    __tablename__ = 'applicants'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(256))
    email = db.Column(db.String(128))
    mobile_number = db.Column(db.Integer)
    resume_filename = db.Column(db.String(128))

    def __init__(self, name, email, mobile_number, resume_filename):
        self.name = name
        self.email = email
        self.mobile_number = mobile_number
        self.resume_filename = resume_filename

    def __repr__(self):
        return '<User %r>' % self.name

    @staticmethod
    def add_applicant(applicant):
        result = True
        try:
            db.session.add(applicant)
            db.session.commit()
        except:
            result = False

        return result


    @staticmethod
    def get_all():
        results = db.session.query(Applicant).all()

        return results





