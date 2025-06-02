from flask import Flask, request
import requests
app = Flask(__name__)

@app.route('/')
def index():
    return 'Hello'
    
@app.route('/api', methods=['POST'])
def api():
    if request.method == 'POST':
        headers = request.headers
        body = request.get_json()
        auth = headers.get('Auth')
        amm = body.get('amount')
        ref = body.get('reference')
        tel = body.get('phone')
        resp = {
            "success":1,
            "data":{
            "phone": tel,
            "reference": "your order id",
            "transactionId": ref,
            "amount": amm,
            "reason":"your reason or narrative"
        }
        }
        url = 'http://127.0.0.1:8000/webhook'
        requests.post(url, json = resp)
        return resp
    else:
        err = {
            "success":0,
            "errormsg":"An Error Occured. Make Payment Error: Insufficient Balance in your account"
            }
        return err
    
if __name__== '__main__':
    app.run(debug=True)