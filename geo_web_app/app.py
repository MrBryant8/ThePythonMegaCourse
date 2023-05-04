import datetime
import pandas
from flask import render_template, Flask, request, send_file
from geopy.geocoders import Nominatim

app = Flask(__name__)


@app.route('/')
def index():
    return render_template("index.html")


@app.route('/success-table', methods=['POST'])
def success_table():
    global filename
    if request.method == 'POST':
        file = request.files['file']

        # if\ 'Address' or 'address' in df.columns:
        try:
            df = pandas.read_csv(file)
            gc = Nominatim(user_agent="http")
            df["coordinates"] = df["Address"].apply(gc.geocode)
            df["Latitude"] = df["coordinates"].apply(lambda x: x.latitude if x is not None else None)
            df["Longitude"] = df["coordinates"].apply(lambda x: x.longitude if x is not None else None)
            df = df.drop('coordinates', 1)
            filename = datetime.datetime.now().strftime(r"uploads/%Y-%m-%d-%H-%M-%S-%f" + ".csv")
            df.to_csv(filename, index=None)
            return render_template("index.html", text=df.to_html(), bttn='download.html')
        # else:
        except Exception as e:
            return render_template("index.html", text=str(e))


@app.route('/download-file')
def download():
    return send_file(filename, attachment_filename="yourfile.csv", as_attachment=True)


if __name__ == '__main__':
    app.debug = True
    app.run()
