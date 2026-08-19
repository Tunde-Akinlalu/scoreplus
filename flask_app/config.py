import os


class Config:
    # 1. Get SECRET_KEY
    SECRET_KEY = os.environ.get('SECRET_KEY', 'isga-secret-key-change-in-production')

    # 2. Get DATABASE_URL
    db_url = os.environ.get('DATABASE_URL')

    # 3. Safety Check: Ensure we have a string, not None or a dict
    if db_url:
        # If it's a string, ensure it has ssl=true for Aiven
        if isinstance(db_url, str):
            # CRITICAL FIX: Do NOT append '?ssl=true' here.
            # This causes the 'str' object has no attribute 'get' error.
            # Just use the URL as-is, or remove the SSL flag entirely if not needed.
            SQLALCHEMY_DATABASE_URI = db_url
        else:
            SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root:password@localhost:3306/isga_gymnastics'
    else:
        SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root:password@localhost:3306/isga_gymnastics'

    SQLALCHEMY_TRACK_MODIFICATIONS = False
    WTF_CSRF_ENABLED = True

    # 4. CRITICAL FIX: Configure SSL options as a DICTIONARY
    # This overrides any URL query parameters that might be misinterpreted.
    # It tells PyMySQL to use SSL correctly.
    SQLALCHEMY_ENGINE_OPTIONS = {
        'connect_args': {
            # 'ssl_disabled': 0 means SSL is required/enabled
            # You can also add 'ssl': {'ca': ...} if Aiven provides a CA file
            'ssl_disabled': 0
        }
    }