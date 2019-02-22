"""import os
import tempfile

import pytest
from app import politico


@pytest.fixture
def client():
    db_fd, politico.app.config['DATABASE'] = tempfile.mkstemp()
    politico.app.config['TESTING'] = True
    client =  politico.app.test_client()

    with  politico.app.app_context():
         politico.app.init_db()

    yield client

    os.close(db_fd)
    os.unlink( politico.app.config['DATABASE'])
"""