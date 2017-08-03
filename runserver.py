from app import app
from app.welcome.views import welcome_blueprint
from app.applicant.views import applicant_blueprint

app.register_blueprint(welcome_blueprint, url_prefix='')
app.register_blueprint(applicant_blueprint, url_prefix='/applicant')
app.run(host="0.0.0.0",port=app.config['PORT'],debug=app.config['DEBUG'])


@app.errorhandler(404)
def internal_error(exception):
    app.logger.exception(exception)
    return render_template('404.html'), 404


@app.errorhandler(500)
def internal_error(exception):
    app.logger.exception(exception)
    
    return render_template('500.html'), 500
