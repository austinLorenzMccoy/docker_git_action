# 🐳 Docker GitHub Actions Demo

![GitHub Workflow Status](https://img.shields.io/github/actions/workflow/status/austinLorenzMccoy/docker_git_action/cicd.yml?style=flat-square)
![Docker Pulls](https://img.shields.io/docker/pulls/austindoc/docker_git_action?style=flat-square)
![License](https://img.shields.io/badge/license-MIT-blue?style=flat-square)

A Flask-based web application demonstrating automated Docker containerization and deployment using GitHub Actions.

## 🚀 Features

- Automated Docker image builds via GitHub Actions
- Continuous Integration/Deployment (CI/CD) pipeline
- Flask web application with testing
- Automated Docker Hub publishing

## 🛠️ Tech Stack

- Python 3.9
- Flask
- Docker
- GitHub Actions
- pytest

## 🏗️ Project Structure

```
dockeraction/
├── Dockerfile              # Container configuration
├── app.py                 # Flask application
├── requirements.txt       # Python dependencies
├── test_app.py           # Test suite
├── .gitignore            # Git ignore rules
├── .github/
│   └── workflows/
│       └── cicd.yml      # CI/CD workflow
└── README.md             # Documentation
```

## 🚦 Prerequisites

- Docker Desktop
- Git
- GitHub account
- Docker Hub account

## 🏃‍♂️ Quick Start

1. **Clone the repository**
   ```bash
   git clone https://github.com/austinLorenzMccoy/docker_git_action.git
   cd docker_git_action
   ```

2. **Local Development**
   ```bash
   # Install dependencies
   pip install -r requirements.txt
   
   # Run tests
   pytest
   
   # Start Flask server
   python app.py
   ```

3. **Docker Operations**
   ```bash
   # Build image
   docker build -t austindoc/docker_git_action .
   
   # Run container
   docker run -p 5001:5001 austindoc/docker_git_action
   ```

## 🔄 CI/CD Pipeline

The GitHub Actions workflow automatically:
- Builds the Docker image
- Runs tests
- Publishes to Docker Hub (austindoc repository)

### Workflow Triggers
- Push to main branch
- Pull requests to main branch

## 📦 Docker Hub

Find the latest image at [hub.docker.com/r/austindoc/docker_git_action](https://hub.docker.com/r/austindoc/docker_git_action)

Pull the image:
```bash
docker pull austindoc/docker_git_action:latest
```

## 🔧 Configuration

### Environment Variables
Configure these in your GitHub repository secrets:
- `DOCKER_USERNAME`: Your Docker Hub username
- `DOCKER_PASSWORD`: Your Docker Hub access token

## 🤝 Contributing

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/amazing-feature`)
3. Commit changes (`git commit -m 'Add amazing feature'`)
4. Push to branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## 📝 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 📧 Contact

Austin McCoy - chibuezeaugustine23@gmail.com

Project Link: [github.com/austinLorenzMccoy/docker_git_action](https://github.com/austinLorenzMccoy/docker_git_action)
