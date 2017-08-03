import os

from app import app
from app.models.applicants import Applicant
from werkzeug.utils import secure_filename

def getApplicantsData():
    datas = Applicant.get_all()

    return datas


        