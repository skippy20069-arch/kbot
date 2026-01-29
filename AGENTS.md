# AGENTS.md

This file provides guidance to WARP (warp.dev) when working with code in this repository.

## Project Overview
This is a Flask-based business website for Wrapology, a custom signs, prints, and vehicle wraps company. The site showcases their services, portfolio work, and provides quote request functionality.

**Technology Stack:**
- Flask 3.0.0 web framework (Python)
- Jinja2 templating (extends/blocks pattern)
- Static CSS (no framework)
- Deployed to Render (configured via render.yaml) or Heroku (Procfile)

## Development Commands

### Local Development
```powershell
# Navigate to project directory
cd C:\Users\vanes\Desktop\website

# Run development server (default port 5000)
python app.py
```

### Production Deployment
The app is configured for both Render and Heroku:
- **Render**: Uses `render.yaml` config with gunicorn
- **Heroku**: Uses `Procfile` with gunicorn
- Production server: `gunicorn app:app`

### Environment Variables
- `SECRET_KEY`: Flask session secret (auto-generated on Render, set manually elsewhere)
- `PORT`: Server port (defaults to 5000)

## Architecture

### Application Structure
```
app.py                  # Main Flask application with all routes
templates/              # Jinja2 templates
├── base.html          # Base template with nav, footer, flash messages
├── home.html          # Homepage with hero, services, featured work
├── work.html          # Portfolio/gallery page
├── shop.html          # Shop page
├── quote.html         # Custom quote request form
└── contact.html       # Contact information page
static/
├── css/
│   └── style.css      # All styling (purple theme: #6629A7)
└── images/            # Product photos and brand assets
```

### Routing Pattern
All routes are defined in `app.py`:
- `/` - Home page
- `/work` - Portfolio showcase
- `/shop` - Shop page
- `/quote` - Quote request form (GET/POST)
- `/contact` - Contact information

The `/quote` route is the only one that handles POST requests. It performs basic form validation and uses Flask's flash messaging system for user feedback.

### Template Inheritance
All templates extend `base.html` which provides:
- Navigation bar with logo and menu links
- Flash message display system
- Footer with contact info and social links
- Consistent page structure via `{% block content %}`

### Styling Approach
Single CSS file (`static/css/style.css`) organized by sections:
- Brand colors: Dark background (#131212), Purple accent (#6629A7), White text (#F8F8F8)
- Uses Poppins font from Google Fonts
- Responsive design patterns
- No CSS framework or preprocessor

### Static Assets
Images in `static/images/` include:
- `logo.png` - Company logo
- `Transform background.jpg` - Hero section background
- Portfolio photos (retail signage, vehicle graphics, window graphics)
- Work examples for gallery pages

## Business Context
**Company:** Wrapology (Northern Ireland)
**Services:** Custom signs, vehicle graphics, print products, window/wall graphics, CNC fabrication, design services

**Contact Information:**
- Email: Wrapology5@gmail.com
- Phone: 07596460121
- Address: 54 Main Street, Killylea, Armagh, BT60 4LS
- Social: Facebook and Instagram

## Important Notes
- The quote form currently only displays flash messages; no actual email sending or database storage is implemented (see comment in app.py:31-32)
- SECRET_KEY defaults to 'dev-secret-key-change-in-production' if not set via environment variable
- Debug mode is set to False in production (app.py:44)
- No automated tests currently exist in the codebase
