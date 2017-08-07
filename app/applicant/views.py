import boto3

from flask import Blueprint, render_template, request, send_from_directory, Response
from app.applicant.controllers import *
from app import app


applicant_blueprint = Blueprint(
        'applicant',
        __name__,
        template_folder='templates'
    )


@applicant_blueprint.route('/')
def index():
    data = {}
    data['applicants'] = getApplicantsData()

    return render_template('applicant/index.html', data=data)


@applicant_blueprint.route('/uploads/<filename>')
def uploaded_file(filename):
    s3_client = boto3.client(service_name='s3', aws_access_key_id=app.config['AWS_ACCESS_KEY_ID'], aws_secret_access_key=app.config['AWS_SECRET_ACCESS_KEY'])

    file = s3_client.get_object(Bucket=app.config['S3_BUCKET'], Key=filename)
    return Response(
        file['Body'].read(),
        mimetype='application/pdf',
        headers={"Content-Disposition": "attachment;filename="+filename}
    )