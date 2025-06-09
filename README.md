# 🚀 Task Management API - Backend Homework 1

A comprehensive Task Management API built with FastAPI, PostgreSQL, JWT authentication, and Docker support. This project implements all three levels of requirements: Basic, Medium, and Hard.

## ✨ Features

### 🥉 Basic Level - ✅ COMPLETED
- ✅ **CRUD Operations**: Complete Create, Read, Update, Delete functionality for tasks
- ✅ **Frontend Integration**: Modern web interface that connects to the backend API

### 🥈 Medium Level - ✅ COMPLETED
- ✅ **Dockerfile**: Production-ready containerization for FastAPI application
- ✅ **PostgreSQL Integration**: Full database connectivity with SQLAlchemy ORM
- ✅ **CI/CD Pipeline**: GitHub Actions workflow for automated testing and deployment

### 🥇 Hard Level - ✅ COMPLETED
- ✅ **JWT Authentication**: Secure user registration and login system
- ✅ **Docker Compose**: Multi-container setup with FastAPI + PostgreSQL
- ✅ **Secured Endpoints**: All task operations require authentication
  - ✅ `/auth/me` - Get current user information
  - ✅ `/tasks/create` - Create a new task
  - ✅ `/tasks/get_tasks` - Get all user's tasks
  - ✅ `/tasks/{task_id}` - Get, update, or delete specific task
  - ✅ `/tasks/{task_id}/complete` - Mark task as completed
  - ✅ `/tasks/{task_id}/incomplete` - Mark task as incomplete

## 🏗️ Architecture

```
📦 Task Management API
├── 🐳 Docker & Docker Compose
├── 🔐 JWT Authentication System
├── 🗄️ PostgreSQL Database
├── 🚀 FastAPI Backend
├── 🌐 Modern Web Frontend
├── 🔄 CI/CD with GitHub Actions
└── 📚 Comprehensive API Documentation
```

## 🛠️ Tech Stack

- **Backend**: FastAPI, SQLAlchemy, PostgreSQL
- **Authentication**: JWT with bcrypt password hashing
- **Database**: PostgreSQL 15 with health checks
- **Containerization**: Docker & Docker Compose
- **CI/CD**: GitHub Actions
- **Frontend**: Modern HTML5, CSS3, JavaScript (Vanilla)
- **Security**: CORS middleware, secure password hashing, token-based auth

## 📋 Prerequisites

### For Windows Users:

1. **Install Docker Desktop for Windows**:
   - Download from: https://docs.docker.com/desktop/install/windows-install/
   - Follow the installation wizard
   - Restart your computer when prompted
   - Enable WSL 2 if prompted

2. **Verify Docker Installation**:
   ```powershell
   docker --version
   docker-compose --version
   ```

3. **Install Git** (if not already installed):
   - Download from: https://git-scm.com/download/win

## 🚀 Quick Start

### 1. Clone the Repository
```bash
git clone <your-repository-url>
cd 09062025
```

### 2. Environment Setup
Copy the example environment file:
```bash
cp .env.example .env
```

### 3. Start the Application
```bash
docker-compose up --build
```

This command will:
- Build the FastAPI application container
- Start PostgreSQL database with health checks
- Set up networking between containers
- Initialize the database tables
- Start the API server on http://localhost:8000

### 4. Access the Application

- **API Documentation**: http://localhost:8000/docs
- **Alternative Docs**: http://localhost:8000/redoc
- **Frontend Application**: Open `frontend/index.html` in your browser
- **Health Check**: http://localhost:8000/health
- **API Root**: http://localhost:8000/

## 📖 API Usage

### Authentication Endpoints

#### Register a New User
```bash
curl -X POST "http://localhost:8000/auth/register" \
     -H "Content-Type: application/json" \
     -d '{
       "username": "testuser",
       "email": "test@example.com",
       "password": "securepassword123"
     }'
```

#### Login
```bash
curl -X POST "http://localhost:8000/auth/login" \
     -H "Content-Type: application/x-www-form-urlencoded" \
     -d "username=testuser&password=securepassword123"
```

#### Get Current User Info
```bash
curl -X GET "http://localhost:8000/auth/me" \
     -H "Authorization: Bearer YOUR_JWT_TOKEN"
```

### Task Management Endpoints

#### Create a Task
```bash
curl -X POST "http://localhost:8000/tasks/create" \
     -H "Content-Type: application/json" \
     -H "Authorization: Bearer YOUR_JWT_TOKEN" \
     -d '{
       "title": "Complete project documentation",
       "description": "Write comprehensive README and API docs",
       "deadline": "2024-12-31T23:59:59"
     }'
```

#### Get All Tasks
```bash
curl -X GET "http://localhost:8000/tasks/get_tasks" \
     -H "Authorization: Bearer YOUR_JWT_TOKEN"
```

#### Update a Task
```bash
curl -X PUT "http://localhost:8000/tasks/1" \
     -H "Content-Type: application/json" \
     -H "Authorization: Bearer YOUR_JWT_TOKEN" \
     -d '{
       "title": "Updated task title",
       "completed": true
     }'
```

#### Delete a Task
```bash
curl -X DELETE "http://localhost:8000/tasks/1" \
     -H "Authorization: Bearer YOUR_JWT_TOKEN"
```

## 🌐 Frontend Usage

1. Open `frontend/index.html` in your web browser
2. Register a new account or login with existing credentials
3. Create, view, update, and delete tasks through the intuitive interface
4. Mark tasks as complete/incomplete
5. View task details including creation time and deadlines

## 🔧 Development

### Running in Development Mode
```bash
# Start only the database
docker-compose up db

# Install Python dependencies
pip install -r requirements.txt

# Run the FastAPI server locally
uvicorn src.main:app --reload --host 0.0.0.0 --port 8000
```

### Database Management
```bash
# Access PostgreSQL directly
docker-compose exec db psql -U postgres -d postgres

# View database logs
docker-compose logs db

# Reset database
docker-compose down -v
docker-compose up --build
```

### Viewing Logs
```bash
# View all logs
docker-compose logs

# View specific service logs
docker-compose logs app
docker-compose logs db

# Follow logs in real-time
docker-compose logs -f app
```

## 🧪 Testing

The project includes a CI/CD pipeline that runs tests automatically. To run tests locally:

```bash
# Install test dependencies
pip install pytest pytest-asyncio httpx

# Run tests (when implemented)
pytest tests/ -v
```

## 🔒 Security Features

- **JWT Authentication**: Secure token-based authentication
- **Password Hashing**: bcrypt for secure password storage
- **CORS Protection**: Configurable cross-origin resource sharing
- **Input Validation**: Pydantic models for request/response validation
- **SQL Injection Protection**: SQLAlchemy ORM prevents SQL injection
- **Non-root Container**: Docker container runs as non-privileged user

## 📁 Project Structure

```
09062025/
├── 📄 README.md                 # This file
├── 📄 requirements.txt          # Python dependencies
├── 📄 Dockerfile               # Container configuration
├── 📄 docker-compose.yml       # Multi-container setup
├── 📄 .env.example             # Environment variables template
├── 📁 .github/
│   └── 📁 workflows/
│       └── 📄 ci-cd.yml        # GitHub Actions CI/CD
├── 📁 src/
│   ├── 📄 main.py              # FastAPI application entry point
│   ├── 📄 config.py            # Configuration management
│   ├── 📄 database.py          # Database models and connection
│   ├── 📄 auth.py              # Authentication utilities
│   ├── 📄 auth_api.py          # Authentication endpoints
│   └── 📁 tasks/
│       ├── 📄 __init__.py
│       ├── 📄 models.py        # Pydantic models
│       ├── 📄 crud.py          # Database operations
│       └── 📄 api.py           # Task endpoints
└── 📁 frontend/
    └── 📄 index.html           # Web frontend
```

## 🌍 Environment Variables

Key environment variables (see `.env.example` for complete list):

- `DATABASE_URL`: PostgreSQL connection string
- `SECRET_KEY`: JWT signing secret (change in production!)
- `ACCESS_TOKEN_EXPIRE_MINUTES`: JWT token expiration time
- `ALLOWED_ORIGINS`: CORS allowed origins

## 🚀 Deployment

The project includes a GitHub Actions CI/CD pipeline that:

1. **Tests**: Runs automated tests on every push/PR
2. **Builds**: Creates Docker images
3. **Pushes**: Uploads images to GitHub Container Registry
4. **Deploys**: Ready for deployment to any container platform

### Production Deployment Checklist

- [ ] Change `SECRET_KEY` to a secure random value
- [ ] Set `DEBUG=False` in production
- [ ] Configure proper CORS origins
- [ ] Set up SSL/TLS certificates
- [ ] Configure database backups
- [ ] Set up monitoring and logging
- [ ] Review security settings

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch: `git checkout -b feature/amazing-feature`
3. Commit your changes: `git commit -m 'Add amazing feature'`
4. Push to the branch: `git push origin feature/amazing-feature`
5. Open a Pull Request

## 📝 License

This project is created for educational purposes as part of a backend development homework assignment.

## 🆘 Troubleshooting

### Common Issues

**Docker not starting:**
- Ensure Docker Desktop is running
- Check if ports 8000 and 5432 are available
- Try `docker-compose down` then `docker-compose up --build`

**Database connection errors:**
- Wait for PostgreSQL health check to pass
- Check database logs: `docker-compose logs db`
- Verify environment variables in `.env`

**Frontend not connecting to API:**
- Ensure API is running on http://localhost:8000
- Check browser console for CORS errors
- Verify API endpoints are accessible

**Authentication issues:**
- Check if JWT token is valid and not expired
- Verify username/password combination
- Clear browser localStorage if needed

### Getting Help

If you encounter issues:

1. Check the logs: `docker-compose logs`
2. Verify all services are running: `docker-compose ps`
3. Test API endpoints with the interactive docs: http://localhost:8000/docs
4. Check the health endpoint: http://localhost:8000/health

---

**🎉 Congratulations! You now have a fully functional Task Management API with authentication, database persistence, and a modern web interface!**
