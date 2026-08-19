import os


class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY', 'isga-secret-key-change-in-production')

    # Get the URL from environment (Render) or .env (Local)
    db_url = os.environ.get('DATABASE_URL')

    # If no URL is found (e.g., empty .env), use a safe fallback
    if db_url:
        # Ensure SSL is enabled if connecting to Aiven
        if 'aivencloud.com' in db_url and 'ssl=true' not in db_url:
            # Append ssl=true if missing
            if '?' in db_url:
                db_url += '&ssl=true'
            else:
                db_url += '?ssl=true'
        SQLALCHEMY_DATABASE_URI = db_url
    else:
        # Fallback for local development (localhost)
        SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root:password@localhost:3306/isga_gymnastics'

    SQLALCHEMY_TRACK_MODIFICATIONS = False
    WTF_CSRF_ENABLED = True