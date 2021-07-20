from sklearn.cluster import KMeans
import cv2
from collections import Counter
from flask import Flask, render_template, request, flash, redirect, send_from_directory, url_for
from PIL import Image
import os
from werkzeug.utils import secure_filename
import matplotlib.pyplot as plt
from pathlib import Path


app = Flask(__name__)
app.config['SECRET_KEY'] = "Ichfahrenach-Lummerland"

UPLOAD_FOLDER = "uploads"
PLOTS_FOLDER = "static/plots"
ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg', 'gif'}

app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

def RGB2HEX(color):
    return "#{:02x}{:02x}{:02x}".format(int(color[0]), int(color[1]), int(color[2]))


@app.route('/', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        # check if the post request has the file part
        if 'file' not in request.files:
            flash('No file part')
            return render_template('index.html')
        file = request.files['file']
        # If the user does not select a file, the browser submits an
        # empty file without a filename.
        if file.filename == '':
            flash('No selected file')
            return render_template('index.html')
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            file.save(Path(UPLOAD_FOLDER)/filename)
            return redirect(url_for('uploaded_file', filename=filename))

    return render_template('index.html')


@app.route('/uploads/<filename>')
def uploaded_file(filename):

    image = cv2.imread(f"{UPLOAD_FOLDER}/{filename}")
    image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

    modified_image = cv2.resize(image, (600, 400), interpolation=cv2.INTER_AREA)
    modified_image = modified_image.reshape(modified_image.shape[0]*modified_image.shape[1], 3)
    
    clf = KMeans(n_clusters=10)
    labels = clf.fit_predict(modified_image)
    
    counts = Counter(labels)
    counts = dict(sorted(counts.items()))
    
    center_colors = clf.cluster_centers_
    ordered_colors = [center_colors[i] for i in counts.keys()]
    rgb_colors = [ordered_colors[i] for i in counts.keys()]
    hex_colors = [RGB2HEX(ordered_colors[i]) for i in counts.keys()]

    plt.figure(figsize=(8, 6))
    plt.pie(counts.values(), labels=hex_colors, colors=hex_colors)
    plt.savefig(Path(PLOTS_FOLDER)/filename)  # save as jpg

    return render_template('colors.html', filename=filename)


if __name__ == '__main__':
    app.run(debug=True)