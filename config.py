from app import app
from flaskext.mysql import MySQL

mysql = MySQL()
app.config['MYSQL_DATABASE_USER'] = 'uroot'
app.config['MYSQL_DATABASE_PASSWORD'] = 'alsharif_2022'
app.config['MYSQL_DATABASE_DB'] = 'vital_signs'
app.config['MYSQL_DATABASE_HOST'] = 'mysql-server'
mysql.init_app(app)
