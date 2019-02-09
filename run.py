import os
from app import politico
from flask import Flask
from app.api.v1.views.politicalparty import politicalparty

app = politico(os.getenv('FLASK_CONFIG') or 'development')
from app.api.v1.views.politicalparty import politicalparty
app.register_blueprint(politicalparty,url_prefix='/api/v1')

if __name__=='__main__':
    app.run()