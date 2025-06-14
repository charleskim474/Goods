from flask import Flask, request, render_template, jsonify
import requests
import sqlite3

def db():
    conn = sqlite3.connect('goods.db')
    cur = conn.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS goods(id INTEGER PRIMARY KEY, item TEXT, qty TEXT, price TEXT)")
    conn.commit()
    conn.close()
    return
    
def save(row):
    conn = sqlite3.connect('goods.db')
    cur = conn.cursor()
    cur.execute("INSERT INTO goods(item, qty, price) VALUES (?, ?, ?)", row)
    conn.commit()
    cur.execute("SELECT * FROM goods")
    res = cur.fetchall()
    for d in res:
        print(d)
    conn.close()


app = Flask(__name__)

@app.route('/')
def index():
    return render_template('subula.html')
    
@app.route('/api', methods=['POST'])
def api():
    try:
        db()
    except Exception as e:
        print(e)
    if request.method == 'POST':
        req = request.get_json()
        try:
            for d in req:
                item = d['item']
                qty = d['qty']
                price = d['price']
                row = (item, qty, price)
                save(row)
        except Exception as e:
            print(e)
        return jsonify({'message':'Received Succesfully'})
    
if __name__== '__main__':
    app.run(debug=True)