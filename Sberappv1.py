#!flask/bin/python
from flask import Flask, render_template


app = Flask(__name__,static_folder="static")


@app.route('/VIp21/Muravev_Andrey_Vladimirovich', methods=['GET'])
def get_Examinations():
    return render_template("index.html")

if __name__ == '__main__':
    app.run(debug=True)
