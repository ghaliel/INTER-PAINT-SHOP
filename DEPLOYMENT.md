# INTER PAINT - Deployment Guide

## Quick Deployment Options

### Option 1: Railway (Recommended - Free & Easy)

1. **Sign up for Railway**
   - Go to [railway.app](https://railway.app)
   - Sign up with GitHub

2. **Deploy your project**
   - Click "New Project" → "Deploy from GitHub repo"
   - Select your repository
   - Railway will automatically detect Django and deploy

3. **Set Environment Variables**
   - Go to your project settings
   - Add these environment variables:
     ```
     SECRET_KEY=your-secret-key-here
     DEBUG=False
     ALLOWED_HOSTS=your-app-name.railway.app
     ```

4. **Your site will be live at**: `https://your-app-name.railway.app`

### Option 2: Render (Free Tier)

1. **Sign up for Render**
   - Go to [render.com](https://render.com)
   - Sign up with GitHub

2. **Create a new Web Service**
   - Connect your GitHub repository
   - Choose "Web Service"
   - Set build command: `pip install -r requirements.txt`
   - Set start command: `gunicorn paintshop.wsgi:application`

3. **Set Environment Variables**
   ```
   SECRET_KEY=your-secret-key-here
   DEBUG=False
   ALLOWED_HOSTS=your-app-name.onrender.com
   ```

### Option 3: PythonAnywhere (Free Tier)

1. **Sign up for PythonAnywhere**
   - Go to [pythonanywhere.com](https://pythonanywhere.com)
   - Create a free account

2. **Upload your code**
   - Use the Files tab to upload your project
   - Or use Git to clone your repository

3. **Set up a web app**
   - Go to Web tab
   - Create a new web app
   - Choose Django and Python 3.11

4. **Configure your app**
   - Set the source code directory
   - Set the WSGI configuration file

## Pre-deployment Checklist

Before deploying, make sure to:

1. **Collect static files**:
   ```bash
   python manage.py collectstatic
   ```

2. **Run migrations**:
   ```bash
   python manage.py migrate
   ```

3. **Create a superuser** (for admin access):
   ```bash
   python manage.py createsuperuser
   ```

4. **Test locally**:
   ```bash
   python manage.py runserver
   ```

## Environment Variables

Set these in your hosting platform:

- `SECRET_KEY`: A secure random string for Django
- `DEBUG`: Set to `False` in production
- `ALLOWED_HOSTS`: Your domain name(s)
- `DATABASE_URL`: Database connection string (if using external database)

## Security Notes

⚠️ **Important**: 
- Change the default SECRET_KEY in production
- Set DEBUG=False in production
- Use HTTPS in production
- Keep your database credentials secure

## Custom Domain

To use a custom domain:
1. Buy a domain (Namecheap, GoDaddy, etc.)
2. Point DNS to your hosting provider
3. Add your domain to ALLOWED_HOSTS
4. Configure SSL certificate

## Troubleshooting

### Common Issues:

1. **Static files not loading**
   - Run `python manage.py collectstatic`
   - Check STATIC_ROOT and STATIC_URL settings

2. **Database errors**
   - Ensure migrations are applied
   - Check database connection settings

3. **500 errors**
   - Check DEBUG=True temporarily to see error details
   - Check server logs

### Getting Help:
- Check Django deployment documentation
- Contact your hosting provider's support
- Check Django community forums

## Next Steps

After deployment:
1. Set up a custom domain
2. Configure email settings
3. Set up monitoring
4. Configure backups
5. Set up CI/CD for automatic deployments 