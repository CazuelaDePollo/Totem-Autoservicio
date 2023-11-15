from flask import Flask, render_template, request, redirect, url_for
from pymongo import MongoClient
from bson.objectid import ObjectId

app = Flask(__name__)
cliente = MongoClient("mongodb+srv://PlayerYee:Yanli1001*@baseplayeryee.rqwmun6.mongodb.net/test")

db = cliente['Autoservicio']

@app.route('/')
def index():
    producto = db.Productos
    datosProd = producto.find()

    return render_template('index.html', producto = datosProd)

@app.route('/completar-pago', methods=['POST'])
def completar_pago():
    total = float(request.form.get('total'))

    vouchers = db.Voucher
    vouchers.insert_one({'total': total})

    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)

