import random
from flask import Flask , render_template

application = Flask(__name__)

@application.route('/')
def index():
    random_number = random.randint(1,100)
    return render_template('index.html', random_number=random_number)

if __name__ == '__main__':
#DEBUG is SET to TRUE. CHANGE FOR PROD
    application.run(debug=True)