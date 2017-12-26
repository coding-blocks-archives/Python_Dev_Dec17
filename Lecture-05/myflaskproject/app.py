from flask import Flask, request, render_template, redirect, url_for
from datetime import date
import csv

app = Flask(__name__)


@app.route('/')
def home():
	return render_template("index.html")


@app.route('/tasks/<int:id>')
def tasks(id):
	return "Task id: {}".format(id)


@app.route('/bio')
def get_bio():
	name = request.args.get("name")
	age = request.args.get("age")
	d = date.today()
	data = [[1,2,3],
			[4,5,6],
			[7,8,9]]
	return render_template("bio.html", name=name, age=age, date=d, 
							data=data)


@app.route('/upload', methods=['GET', 'POST'])
def uploader():
	if request.method == 'GET':
		return render_template("upload.html")

	elif request.method == 'POST':
		name = request.form.get("name")
		year = request.form.get("year")
		cgpa = request.form.get("cgpa")

		with open("records.csv", "a") as f:
			writer = csv.writer(f)
			writer.writerow([name, year, cgpa])

		image = request.files.get("image")
		image.save("static/images/{}".format(image.filename))

		return redirect(url_for("home"))



if __name__ == "__main__":
	app.run(port=8000, debug=True, use_reloader=True)