import random
from flask import Flask , render_template
from flaskext.mysql import MySQL
import os
from dotenv import load_dotenv

load_dotenv()  # take environment variables from .env.


application = Flask(__name__)

mysql=MySQL()
application.config['MYSQL_DATABASE_HOST']=os.environ['RDS_HOSTNAME']
application.config['MYSQL_DATABASE_USER']=os.environ['RDS_USERNAME']
application.config['MYSQL_DATABASE_PASSWORD']=os.environ['RDS_PASSWORD']
application.config['MYSQL_DATABASE_DB']='FlasktoAWS'
mysql.init_app(application)

@application.route('/')
def index():
    random_number = random.randint(1,100)

    sql="SELECT * FROM `Prueba`;"
    conn=mysql.connect()
    cursor=conn.cursor()
    cursor.execute(sql)
    informacion=cursor.fetchall()
    conn.commit()

    return render_template('index.html', random_number=random_number, informacion=informacion)

if __name__ == '__main__':
#DEBUG is SET to TRUE. CHANGE FOR PROD
    application.run(debug=True)