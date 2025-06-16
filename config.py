import os

basedir = os.path.abspath(os.path.dirname(__file__))

class Config(object):
    SECRET_KEY = os.environ.get('SECRET_KEY') or '3b7d!@Ud4c1tyCMS#2025'

    # Storage account info
    BLOB_ACCOUNT = os.environ.get('BLOB_ACCOUNT') or 'udacitystorage1705'
    BLOB_STORAGE_KEY = os.environ.get('BLOB_STORAGE_KEY') or 'nHtE8pLYdx0eXy+D8khs16b7ZkXS8ejaAeeQjpC88S+KjHJZzMhNV5BQ4tspEqNXhPbUaqj3slyT+ASt7USRxw=='
    BLOB_CONTAINER = os.environ.get('BLOB_CONTAINER') or 'article-images'

    # SQL Server info
    SQL_SERVER = os.environ.get('SQL_SERVER') or 'udacityserver.database.windows.net'
    SQL_DATABASE = os.environ.get('SQL_DATABASE') or 'udacitydb'
    SQL_USER_NAME = os.environ.get('SQL_USER_NAME') or 'azureuser'
    SQL_PASSWORD = os.environ.get('SQL_PASSWORD') or 'Udacityuser123'
    # Connection string for SQLAlchemy
    SQLALCHEMY_DATABASE_URI = (
        'mssql+pyodbc://'
        + SQL_USER_NAME + '@' + SQL_SERVER + ':'
        + SQL_PASSWORD + '@' + SQL_SERVER
        + ':1433/' + SQL_DATABASE
        + '?driver=ODBC+Driver+17+for+SQL+Server'
    )
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    ### Info for MS Authentication ###
    CLIENT_SECRET = os.environ.get('CLIENT_SECRET') or 'Mdd8Q~wC.4WEFQJ0KH_cy_lcpWzny7YXIYgv4a6O'
    # In production, recommend using KeyVault or environment variables for CLIENT_SECRET

    AUTHORITY = os.environ.get('AUTHORITY') or "https://login.microsoftonline.com/common"  # For multi-tenant apps

    CLIENT_ID = os.environ.get('CLIENT_ID') or "0b8b0405-169d-49d1-9aa4-c92778f8154e"

    REDIRECT_PATH = "/getAToken"  # Must match your Azure app registration

    SCOPE = ["User.Read"]  # Only need to read user profile for this app

    SESSION_TYPE = "filesystem"  # Token cache stored in server-side session
