from flask import Flask
from app.api.v1.views.politicalparty import politicalparty

app = Flask(__name__)
from app.api.v1.views.politicalparty import politicalparty
app.register_blueprint(politicalparty,url_prefix='/api/v1')

if __name__=='__main__':
    app.run(debug=True)
