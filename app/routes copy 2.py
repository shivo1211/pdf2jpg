from flask import current_app, render_template, request, send_from_directory, redirect, url_for
from app import create_app
from .utils import pdf_to_jpg

app = create_app()

@app.route('/', methods=['GET', 'POST'])
def index():
    # Your route handling code
