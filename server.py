from flask import Flask, jsonify,abort,redirect,url_for
app = Flask(__name__)

laptops = [
    {
        'id': 1,
        'model': u'HP',
        'price': u'25000', 
        'available': False
    },
    {
        'id': 2,
        'model': u'Lenova',
        'price': u'25600', 
        'available': False
    }
    {
        'id': 3,
        'model': u'Dell',
        'price': u'32000', 
        'available': True
    }
    {
        'id': 4,
        'model': u'Samsung',
        'price': u'25200', 
        'available': True
    }
]

@app.route('/laptops', methods=['GET','POST'])
def get_laptops():
    return jsonify({'laptops': laptops})

@app.route('/laptops/<int:laptops_id>', methods=['GET','POST'])
def get_laptop_status(laptops_id):
    laptops = [laptop for laptop in laptops if laptop['id'] == laptops_id]
    if len(laptops) == 0:
        abort(404)
    return jsonify({'laptops': laptops[0]})

if __name__ == '__main__':
    app.run(debug=True,host="0.0.0.0",port=8787)
