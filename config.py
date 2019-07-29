import os


class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'the-most-secret-key-of-secret-keys'
