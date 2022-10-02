#import pymysql
from app import app
import mysql.connector
# from config import mysql
from flask import jsonify
from flask import Flask, request

@app.route('/add', methods=['POST'])
def create_save():
    try:
        _json = request.json
        _timestamp = _json['timestamp']
        _hr = _json['hr']
        _spo2 = _json['spo2']
        _resp = _json['resp']
        _tempr = _json['tempr']
        db = mysql.connector.connect(host='db_server', user='root', password='alsharif_2022', port=3306, database="vital_signs")
        cursor = db.cursor()
        if _timestamp and _hr and _spo2 and _tempr and _resp and request.method == 'POST':
            sqlQuery = "INSERT INTO vital_sign_table(timestamp, hr, spo2, resp, tempr) VALUES(%s, %s, %s, %s, %s)"
            bindData = (_timestamp, _hr, _spo2, _resp, _tempr)
            cursor.execute(sqlQuery, bindData)
            db.commit()
            respone = jsonify('Vital signs added successfully!')
            respone.status_code = 200
            cursor.close()
            db.close()
            return respone
        else:
            return showMessage()
    except Exception as e:
        print("add fail!!!")
        print(e)
        return showMessage("fetch-"+str(e))

     
@app.route('/fetch')
def fetch_vital_signs():
    try:
        db = mysql.connector.connect(host='db_server', user='root', password='alsharif_2022', port=3306, database="vital_signs")
        cursor = db.cursor()
        cursor.execute("SELECT timestamp, hr, spo2, resp, tempr FROM vital_sign_table LIMIT 1")
        empRows = cursor.fetchall()
        respone = jsonify(empRows)
        respone.status_code = 200
        cursor.close()
        db.close()
        return respone
    except Exception as e:
        print("fetch fail!!!")
        print(e)
        return showMessage("fetch-"+str(e))

@app.errorhandler(404)
def showMessage(error=None):
    message = {
        'status': 404,
        'message':'Record not found: '+request.url,
    }
    respone = jsonify(message)
    respone.status_code = 404
    return respone
        
if __name__ == "__main__":
    print("rest api")
    app.run(debug=True, host='0.0.0.0')
