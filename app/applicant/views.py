from flask import Blueprint, render_template, request, send_from_directory
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
    return send_from_directory(directory='uploads', filename=filename, as_attachment=True)