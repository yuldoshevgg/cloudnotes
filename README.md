# CloudNotes ☁️📝

CloudNotes is a cloud-based note management system that allows users to securely create, edit, and manage personal notes through a web interface.

The application is built using the **Django framework** and deployed using **Docker containers** on a cloud server. The project demonstrates modern backend development and DevOps practices including containerization, cloud deployment, HTTPS configuration, and automated CI/CD pipelines.

---

# 🌐 Live Demo

The application is deployed on a cloud server and accessible via HTTPS.

**Website:**  
https://yuldoshevgg.work

---

# 🚀 Features

- User registration and authentication
- Create, edit, and delete personal notes
- Secure data storage using PostgreSQL
- Containerized deployment using Docker
- Reverse proxy configuration using Nginx
- Automated deployment with GitHub Actions
- HTTPS support using Let's Encrypt
- Cloud deployment on a virtual machine
- Health check endpoint for monitoring

---

# 🏗 System Architecture

The system follows a client–server architecture where user requests are processed by the backend server and stored in the database.

```
User Browser
      │
      │ HTTPS
      ▼
Cloudflare
      │
      ▼
Nginx (Reverse Proxy + Static Files)
      │
      ▼
Django Application (Gunicorn)
      │
      ▼
PostgreSQL Database
```

Each service runs inside its own **Docker container**, ensuring consistent environments across development and production.

---

# 🧰 Technology Stack

| Component | Technology |
|-----------|------------|
| Programming Language | Python |
| Backend Framework | Django |
| Database | PostgreSQL |
| Web Server | Nginx |
| Containerization | Docker |
| Container Orchestration | Docker Compose |
| CI/CD | GitHub Actions |
| Cloud Infrastructure | Oracle Cloud VM |
| SSL | Let's Encrypt |

---

# 📂 Project Structure

```
cloudnotes/
│
├── config/              # Django project configuration
├── notes/               # Notes application
├── nginx/               # Nginx configuration
├── Dockerfile           # Docker image configuration
├── docker-compose.yml   # Container orchestration
├── requirements.txt     # Python dependencies
└── manage.py
```

---

# 💻 Local Development Setup

## 1. Clone the repository

```bash
git clone https://github.com/yuldoshevgg/cloudnotes.git
cd cloudnotes
```

---

## 2. Create environment variables

Create a `.env` file in the project root directory.

Example configuration:

```
SECRET_KEY=your-secret-key
DEBUG=True

POSTGRES_DB=cloudnotes
POSTGRES_USER=cloudnotes
POSTGRES_PASSWORD=cloudnotespassword
```

---

## 3. Build Docker containers

```
docker-compose build
```

---

## 4. Start containers

```
docker-compose up
```

The application will be available at:

```
http://localhost:8000
```

---

# ☁️ Production Deployment

The application is deployed on a **cloud virtual machine** using Docker containers and is publicly accessible at:

**https://yuldoshevgg.work**

Deployment includes:

- Docker container environment
- Nginx reverse proxy
- PostgreSQL database
- HTTPS using Let's Encrypt
- Domain configuration
- Cloud server deployment

Start the production environment with:

```
docker-compose up -d
```

---

# ⚙️ Continuous Deployment

This project uses **GitHub Actions** for automated CI/CD.

When changes are pushed to the **main branch**, the pipeline automatically:

1. Builds the Docker image
2. Pushes the image to DockerHub
3. Connects to the cloud server via SSH
4. Updates containers using Docker Compose

Deployment workflow:

```
Push Code
   ↓
GitHub Actions
   ↓
Docker Image Build
   ↓
Push to DockerHub
   ↓
Deploy to Cloud Server
```

This ensures that the latest version of the application is automatically deployed.

---

# 🔐 Environment Variables

Example `.env` configuration for production:

```
SECRET_KEY=production-secret-key
DEBUG=False

POSTGRES_DB=cloudnotes
POSTGRES_USER=cloudnotes
POSTGRES_PASSWORD=securepassword

DB_HOST=db
DB_PORT=5432
```

---

# ❤️ Health Check Endpoint

The application includes a health check endpoint used by Docker and monitoring tools.

Endpoint:

```
/health/
```

Example response:

```json
{
  "status": "ok"
}
```

---

# 🔒 Security

Security measures implemented in the system include:

- Environment variables for sensitive configuration
- HTTPS encryption using SSL certificates
- Docker container isolation
- Secure database configuration
- Reverse proxy protection using Nginx

---

# 📈 Future Improvements

Potential improvements for future versions include:

- Note sharing between users
- Real-time collaborative editing
- REST API for mobile applications
- Advanced search functionality
- File attachments
- Monitoring and logging systems

# 📄 License

This project was developed for educational purposes.