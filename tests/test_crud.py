from school import create_app
def test_index(app, client):
    """
    SHOULD load index page with valid HTTP status
    """
    res = client.get('/')
    assert res.status_code == 200