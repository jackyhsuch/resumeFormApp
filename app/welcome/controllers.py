import os
import datetime
import boto3

from app import app
from app.models.applicants import Applicant
from werkzeug.utils import secure_filename
from PIL import Image
from io import BytesIO

def parseApplicationRequest(request):
    name = request.form['name']
    email = request.form['email']
    mobile_number = request.form['mobile_number']
    resume_file = request.files['resume_filename']
    photo = request.files['photo']

    # if photo:
    #     resume_filename = str(int(datetime.datetime.utcnow().timestamp())) + '.pdf'

    #     im = Image.open(photo)
    #     outfile = os.path.join(app.config['UPLOAD_FOLDER'], resume_filename)
    #     im.save(outfile, "PDF", resolution=100.0)


    if 'resume_filename' in request.files and\
        resume_file.filename != '' and\
        allowed_file(resume_file.filename):

        resume_filename = str(int(datetime.datetime.utcnow().timestamp())) + '.pdf'
        s3_client = boto3.client(service_name='s3', aws_access_key_id=app.config['AWS_ACCESS_KEY_ID'], aws_secret_access_key=app.config['AWS_SECRET_ACCESS_KEY'])

        if not resume_file.filename.endswith('.pdf'):
            im = Image.open(resume_file)
            file = BytesIO()
            im.save(file, "PDF", resolution=100.0)

            s3_client.put_object(Body=file.getvalue(), Bucket=app.config['S3_BUCKET'], Key=resume_filename)

        else:

            s3_client.put_object(Body=resume_file, Bucket=app.config['S3_BUCKET'], Key=resume_filename)

    applicant = Applicant(
            name = name,
            email = email,
            mobile_number = mobile_number,
            resume_filename = resume_filename
        )

    result = Applicant.add_applicant(applicant)

    return


def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in app.config['ALLOWED_EXTENSIONS']


        