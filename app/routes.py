from flask import current_app, render_template, request, send_from_directory, redirect, url_for
from .utils import pdf_to_jpg

def create_routes(app):
    @app.route('/', methods=['GET', 'POST'])
    def index():
        if request.method == 'POST':
            # Check if a file was uploaded
            if 'file' not in request.files:
                return redirect(request.url)
            file = request.files['file']
            # If the user does not select a file, the browser submits an
            # empty file without a filename.
            if file.filename == '':
                return redirect(request.url)
            if file:
                pdf_to_jpg(file)
                return redirect(url_for('uploaded_file', filename='output.jpg'))
        return render_template('index.html')

    @app.route('/uploads/<filename>')
    def uploaded_file(filename):
        return send_from_directory(current_app.config['UPLOAD_FOLDER'],
                                   filename)
