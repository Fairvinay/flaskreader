class Config:
    CORS_RESOURCES = {
        '/remove_password': {'origins': 'https://storenotify.in,http://localhost:port,http://127.0.0.1:5000/'}
    }