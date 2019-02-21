import os
from app import politico

app = politico(os.getenv('APP_SETTINGS') or 'development')

if __name__=='__main__':
    app.run()
