# import mysql.connector
# try:
#     db = mysql.connector.connect(host = 'mysql-server', user = 'root', password = 'alsharif_2022', port = 3306, database="vital_signs")
#     cursor = db.cursor()
#     cursor.execute("SELECT timestamp, hr, spo2, resp, tempr FROM vital_sign_table LIMIT 1")
#     empRows = cursor.fetchall()
#     # respone = jsonify(empRows)
#     # respone.status_code = 200
#     print(empRows)
#     cursor.close()
#     db.close()
#
#     # print(respone)
# except Exception as e:
#     print("fetch fail!!!")
#     print(e)