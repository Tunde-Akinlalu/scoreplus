# ISGA Gymnastics Scoring System

A Flask-based web application for managing gymnastics competition scoring for the Independent Schools Gymnastics Association (ISGA).

## Features

- **User Authentication**: Login, registration, role-based access (admin, scorer, viewer)
- **Event Management**: Create events with multiple categories (5 Piece, 4 Piece)
- **School & Athlete Registration**: Register schools and athletes per category
- **Score Input Interface**: Real-time score entry with auto-calculation of totals
- **Team Totals & Group Scores**: Automatic calculation of top-4 apparatus totals, team positions, and group scores
- **Dynamic Row Creation**: Add athlete rows on the fly
- **Export to Excel**: Branded Excel export with ISGA purple/cyan styling
- **Export to PDF**: Professional PDF reports with full formatting
- **ISGA Branding**: Purple (#6B2D7B) and cyan (#00BCD4) theme matching isgagymnastics.org

## Setup in PyCharm

### 1. Prerequisites
- Python 3.9+
- MySQL Server (or MariaDB)
- PyCharm IDE

### 2. Create MySQL Database
```sql
CREATE DATABASE isga_gymnastics CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;
```

### 3. Open in PyCharm
1. Open PyCharm → File → Open → select the `flask_app` folder
2. Configure Python Interpreter (Settings → Project → Python Interpreter)
3. Create a virtual environment

### 4. Install Dependencies
```bash
pip install -r requirements.txt
```

### 5. Configure Environment
```bash
cp .env.example .env
# Edit .env with your MySQL credentials
```

### 6. Run the Application
```bash
python app.py
```
Or in PyCharm: Right-click `app.py` → Run

### 7. Access the Application
- Open http://localhost:5000
- Default admin login: `admin` / `admin123`

## Project Structure
```
flask_app/
├── app.py              # Main Flask application & routes
├── config.py           # Configuration (DB, secret key)
├── models.py           # SQLAlchemy database models
├── forms.py            # Flask-WTF form definitions
├── requirements.txt    # Python dependencies
├── .env.example        # Environment variable template
├── README.md           # This file
└── templates/
    ├── base.html              # Base template with ISGA branding
    ├── index.html             # Home page with event listing
    ├── login.html             # Login form
    ├── register.html          # Registration form
    ├── create_event.html      # Event creation form
    ├── view_event.html        # Event detail with categories
    ├── add_category.html      # Add category to event
    ├── schools.html           # School management
    ├── add_school_to_category.html  # Add school to category
    ├── view_category.html     # Full results table (like your CSV)
    └── score_input.html       # Score entry interface
```

## Scoring Logic

- **Individual Total** = Set Vault + Vol Vault + Set Floor + Vol Floor
- **Team Totals**: Top 4 scores per apparatus across team members
- **Group Score**: Sum of apparatus averages (team total / 4 per apparatus)
- **Positions**: Ranked by total score (descending) across all teams in category
