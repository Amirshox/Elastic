from app import create_app


def test_get_cars():
    flask_app = create_app()

    # Create a test client using the Flask application configured for testing
    with flask_app.test_client() as test_client:
        response = test_client.get('/api/v1/cars/')
        assert response.status_code == 200
