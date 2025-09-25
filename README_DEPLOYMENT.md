# Vercel Deployment Instructions

## Prerequisites

1. Create a Vercel account
2. Set up a cloud database (Neon, Supabase, or AWS RDS)
3. Have your frontend repository ready

## Deployment Steps

### 1. Environment Variables

Set these in your Vercel dashboard for backend (hrms-v1-64ls.vercel.app):

```
SECRET_KEY=your-secret-key
DEBUG=False
VERCEL=1
FORCE_HTTPS=1
ALLOWED_HOSTS=hrms-v1-64ls.vercel.app
DB_NAME=your-db-name
DB_USER=your-db-user
DB_PASSWORD=your-db-password
DB_HOST=your-db-host
DB_PORT=5432
CORS_ALLOWED_ORIGINS=https://hrms-v1-x4vi.vercel.app
FRONTEND_URL=https://hrms-v1-x4vi.vercel.app
```

### 2. Frontend Configuration

Update your frontend (hrms-v1-x4vi.vercel.app) API base URL:

```javascript
const API_BASE_URL = "https://hrms-v1-64ls.vercel.app";
```

Set this in your frontend environment variables:

```
VITE_API_BASE_URL=https://hrms-v1-64ls.vercel.app
```

### 3. Database Setup

- Use a cloud PostgreSQL database
- Run migrations after deployment:
  ```bash
  python manage.py migrate
  python manage.py createsuperuser
  ```

### 4. Deploy

1. Push code to GitHub
2. Connect repository to Vercel
3. Deploy with automatic builds

## API Endpoints

Your Django API will be available at: https://hrms-v1-64ls.vercel.app/api/

## Post-Deployment

1. Test all API endpoints from frontend
2. Verify HTTPS enforcement
3. Check CORS configuration between:
   - Frontend: https://hrms-v1-x4vi.vercel.app
   - Backend: https://hrms-v1-64ls.vercel.app
4. Test file uploads (if any)

## Troubleshooting

- Check Vercel function logs for errors
- Ensure all environment variables are set
- Verify database connectivity
- Test CORS by checking browser console for any blocked requests
- Test with Vercel CLI locally first
