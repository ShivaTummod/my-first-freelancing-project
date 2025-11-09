# 🏢 Smart Building Management System

A comprehensive Django-powered facility management platform for monitoring and managing building operations.

[![Deploy GitHub Pages](https://github.com/ShivaTummod/my-first-freelancing-project/actions/workflows/pages.yml/badge.svg)](https://github.com/ShivaTummod/my-first-freelancing-project/actions/workflows/pages.yml)
[![Django CI](https://github.com/ShivaTummod/my-first-freelancing-project/actions/workflows/django-ci.yml/badge.svg)](https://github.com/ShivaTummod/my-first-freelancing-project/actions/workflows/django-ci.yml)

## 📋 Overview

The Smart Building Management System is a web application built with Django that helps facility managers monitor, control, and optimize building operations. The system provides a centralized dashboard for managing multiple facilities, tracking maintenance, and accessing real-time building data.

## ✨ Features

- **🔐 User Authentication**: Secure login and registration system
- **📊 Interactive Dashboard**: Comprehensive overview of facility operations
- **🏗️ Facility Management**: Track and manage multiple facilities
- **📱 Responsive Design**: Works seamlessly on desktop and mobile devices
- **🔒 Admin Panel**: Django's powerful admin interface for system management
- **📷 Media Management**: Upload and manage facility images and documents

## 🚀 Quick Start

### Prerequisites

- Python 3.9 or higher
- pip (Python package manager)
- Git
- Virtual environment (recommended)

### Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/ShivaTummod/my-first-freelancing-project.git
   cd my-first-freelancing-project
   ```

2. **Create and activate virtual environment**
   ```bash
   # On macOS/Linux
   python -m venv venv
   source venv/bin/activate
   
   # On Windows
   python -m venv venv
   venv\Scripts\activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r smartbuilding/requirements.txt
   ```

4. **Navigate to the Django project**
   ```bash
   cd smartbuilding
   ```

5. **Set up environment variables** (optional)
   ```bash
   cp ../.env.example .env
   # Edit .env with your configuration
   ```

6. **Run database migrations**
   ```bash
   python manage.py migrate
   ```

7. **Create a superuser** (optional, for admin access)
   ```bash
   python manage.py createsuperuser
   ```

8. **Collect static files**
   ```bash
   python manage.py collectstatic --noinput
   ```

9. **Run the development server**
   ```bash
   python manage.py runserver
   ```

10. **Access the application**
    - Main site: http://127.0.0.1:8000/
    - Admin panel: http://127.0.0.1:8000/admin/

## 📁 Project Structure

```
my-first-freelancing-project/
├── .github/
│   └── workflows/          # GitHub Actions workflows
│       ├── django-ci.yml   # CI/CD for Django tests
│       ├── deploy.yml      # Deployment workflow
│       └── pages.yml       # GitHub Pages deployment
├── smartbuilding/          # Django project root
│   ├── bot/                # Main application
│   │   ├── templates/      # HTML templates
│   │   ├── models.py       # Database models
│   │   ├── views.py        # View functions
│   │   └── ...
│   ├── smartbuilding/      # Project settings
│   │   ├── settings.py     # Django settings
│   │   ├── urls.py         # URL routing
│   │   └── ...
│   ├── media/              # User-uploaded files
│   ├── static_root/        # Collected static files
│   ├── manage.py           # Django management script
│   └── requirements.txt    # Python dependencies
├── index.html              # GitHub Pages landing page
├── DEPLOYMENT.md           # Deployment guide
└── README.md               # This file
```

## 🌐 Deployment

### Important Note

⚠️ **This Django application cannot run on GitHub Pages.** GitHub Pages only serves static HTML/CSS/JS files and cannot execute Python/Django applications.

The `index.html` file in the root serves as a **documentation landing page** for GitHub Pages, not the actual application.

### Deployment Options

For production deployment, choose one of these platforms:

#### 1. Heroku (Recommended for beginners)
```bash
# Install Heroku CLI and login
heroku login

# Create new app
heroku create your-app-name

# Add PostgreSQL database
heroku addons:create heroku-postgresql:mini

# Deploy
git push heroku main
```

#### 2. Railway
- Connect your GitHub repository
- Railway will auto-detect Django
- Configure environment variables
- Deploy with one click

#### 3. Render
- Connect your GitHub repository  
- Create a new Web Service
- Configure build and start commands
- Deploy automatically on push

#### 4. AWS EC2, DigitalOcean, or Custom Server
See [DEPLOYMENT.md](DEPLOYMENT.md) for detailed instructions.

## 🧪 Testing

Run the test suite:

```bash
cd smartbuilding
python manage.py test
```

Run tests with coverage:

```bash
coverage run --source='.' manage.py test
coverage report
```

## 🔒 Security

### Production Checklist

Before deploying to production:

- [ ] Set `DEBUG = False` in settings.py
- [ ] Change `SECRET_KEY` to a secure random value
- [ ] Configure `ALLOWED_HOSTS` with your domain
- [ ] Use environment variables for sensitive data
- [ ] Set up HTTPS/SSL certificate
- [ ] Configure proper database (PostgreSQL recommended)
- [ ] Set up static file serving (Whitenoise or CDN)
- [ ] Enable security middleware
- [ ] Review Django's deployment checklist

Run Django's security check:

```bash
python manage.py check --deploy
```

## 📚 Documentation

- [Django Documentation](https://docs.djangoproject.com/)
- [Deployment Guide](DEPLOYMENT.md)
- [Django Deployment Checklist](https://docs.djangoproject.com/en/stable/howto/deployment/checklist/)

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## 📝 License

This project is available for use under standard software practices.

## 🐛 Issues

Found a bug or have a suggestion? Please [open an issue](https://github.com/ShivaTummod/my-first-freelancing-project/issues).

## 👥 Authors

- ShivaTummod - Initial work

## 🙏 Acknowledgments

- Built with Django
- Deployed with GitHub Actions
- Documentation hosted on GitHub Pages
