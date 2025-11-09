# Django Deployment Guide

This guide explains how to deploy your Django application using GitHub Actions.

## GitHub Actions Workflows

This project includes two GitHub Actions workflows:

### 1. Django CI (`django-ci.yml`)
Runs automatically on every push and pull request to main/master/develop branches.

**What it does:**
- Tests the application with multiple Python versions (3.9, 3.10, 3.11)
- Installs dependencies
- Runs database migrations
- Runs Django tests
- Checks for security issues

### 2. Deploy (`deploy.yml`)
Deploys the application when code is pushed to main/master branch or manually triggered.

**What it does:**
- Runs tests before deployment
- Collects static files
- Provides templates for various deployment platforms

## Deployment Options

### Option 1: Heroku

1. Create a Heroku account and app
2. Add the following secrets to your GitHub repository:
   - `HEROKU_API_KEY`: Your Heroku API key
   - `HEROKU_APP_NAME`: Your Heroku app name
   - `HEROKU_EMAIL`: Your Heroku account email

3. Uncomment the Heroku deployment section in `.github/workflows/deploy.yml`

4. Create a `Procfile` in the root directory:
   ```
   web: cd smartbuilding && gunicorn smartbuilding.wsgi
   ```

5. Add `gunicorn` to your requirements.txt

### Option 2: AWS EC2

1. Set up an EC2 instance with your Django application
2. Add the following secrets to your GitHub repository:
   - `EC2_SSH_KEY`: Your private SSH key
   - `EC2_HOST`: Your EC2 instance IP or hostname
   - `EC2_USERNAME`: SSH username (usually `ubuntu` or `ec2-user`)

3. Uncomment the AWS deployment section in `.github/workflows/deploy.yml`

### Option 3: DigitalOcean App Platform

1. Create a DigitalOcean account and app
2. Add the following secret to your GitHub repository:
   - `DIGITALOCEAN_ACCESS_TOKEN`: Your DigitalOcean API token

3. Uncomment the DigitalOcean deployment section in `.github/workflows/deploy.yml`

### Option 4: Custom Server (SSH)

1. Set up your server with Python, pip, and your Django application
2. Add the following secrets to your GitHub repository:
   - `HOST`: Your server IP or hostname
   - `USERNAME`: SSH username
   - `SSH_PRIVATE_KEY`: Your private SSH key

3. Uncomment the custom server deployment section in `.github/workflows/deploy.yml`
4. Update the script section with your server's specific paths and commands

## Adding GitHub Secrets

To add secrets to your GitHub repository:

1. Go to your repository on GitHub
2. Click on "Settings" → "Secrets and variables" → "Actions"
3. Click "New repository secret"
4. Add the required secrets based on your deployment option

## Environment Variables for Production

Before deploying, update your `settings.py` for production:

1. Set `DEBUG = False` in production
2. Configure `ALLOWED_HOSTS` with your domain
3. Use environment variables for sensitive data:
   ```python
   import os
   
   SECRET_KEY = os.environ.get('DJANGO_SECRET_KEY', 'fallback-secret-key')
   DEBUG = os.environ.get('DEBUG', 'False') == 'True'
   ALLOWED_HOSTS = os.environ.get('ALLOWED_HOSTS', '').split(',')
   ```

4. Configure database for production (PostgreSQL is recommended)

## Testing Locally

Before deploying, test your application locally:

```bash
cd smartbuilding
python manage.py test
python manage.py check --deploy
python manage.py collectstatic --noinput
```

## Manual Deployment Trigger

You can manually trigger deployment from GitHub:

1. Go to "Actions" tab in your repository
2. Select "Deploy Django Application" workflow
3. Click "Run workflow"
4. Select the branch and click "Run workflow"

## Monitoring Deployments

- Check the "Actions" tab in your GitHub repository to see workflow runs
- Click on any workflow run to see detailed logs
- Failed deployments will send notifications (configure in repository settings)

## Troubleshooting

- **Tests failing**: Check the CI workflow logs for error details
- **Static files not loading**: Ensure `collectstatic` runs successfully
- **Database errors**: Make sure migrations run on the deployment server
- **Secret key errors**: Verify all required secrets are added to GitHub

## Additional Resources

- [Django Deployment Checklist](https://docs.djangoproject.com/en/stable/howto/deployment/checklist/)
- [GitHub Actions Documentation](https://docs.github.com/en/actions)
- [Heroku Django Deployment](https://devcenter.heroku.com/articles/django-app-configuration)
