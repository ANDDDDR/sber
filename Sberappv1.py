#!flask/bin/python
from flask import Flask, jsonify


app = Flask(__name__)

Examinations = [
    {        
	
        'subject': 'OS',
	'exam grade':'excellent'
    },
    {
        
        'subject': 'Computational Mathematics',
	'exam grade':'good'
    },
	{        
	
        'subject': 'electrical engineering',
	'exam grade':'good'
    },
    {
        
        'subject': 'computer and peripherals',
	'exam grade':'excellent'
    }
]

@app.route('/VIp21/Muravev_Andrey_Vladimirovich', methods=['GET'])
def get_Examinations():
    return jsonify({'Examinations': Examinations})

if __name__ == '__main__':
    app.run(debug=True)
