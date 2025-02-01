# 📚 FAQ Management System

A dynamic and multilingual FAQ management system designed to handle frequently asked questions in multiple languages. Built with Django and designed for scalability.

---

## 🚀 Installation

Get started with the FAQ Management System in just a few easy steps:

1. **Clone the repository:**
   ```bash
   git clone https://github.com/your-repo/faq-management-system.git
   cd faq-management-system
2. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
3. **Run migrations:**
   ```bash
   python manage.py migrate
4. **Start the server:**
   ```bash
   python manage.py runserver
5. **Access the system:**
   Open your browser and navigate to http://127.0.0.1:8000.

# 🌐 API Usage
The system provides a RESTful API to fetch FAQs in multiple languages. Below are the available endpoints:

## Fetch FAQs
**English:**
GET /api/faqs/

**Hindi:**
GET /api/faqs/?lang=hi

**Bengali:**
GET /api/faqs/?lang=bn

## 🧪 Running Tests
Ensure the system is working as expected by running the test suite:
pytest

## 🐳 Deployment
Deploy the FAQ Management System effortlessly using Docker:

Build and run the containers:

docker-compose up --build
Access the deployed system:
Open your browser and navigate to http://localhost:8000.

## 📂 Project Structure
faq-management-system/
```bash
├── api/               # API endpoints and logic
├── core/              # Core application settings and configurations
├── faqs/              # FAQ models and views
├── tests/             # Unit and integration tests
├── manage.py          # Django management script
├── requirements.txt   # Project dependencies
└── Dockerfile         # Docker configuration

