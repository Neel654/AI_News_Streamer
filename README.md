# 📰 AI News Streamer - AI-Powered News Aggregation & Summarization Platform

A Python-based web application that fetches, processes, and summarizes news articles using AI-powered workflows, delivering content through a clean stream-style web interface built with a Python backend and JavaScript frontend.

[![Python](https://img.shields.io/badge/Python-Backend-blue?style=for-the-badge&logo=python)](https://www.python.org/) [![Flask](https://img.shields.io/badge/Framework-Flask-black?style=for-the-badge&logo=flask)]() [![JavaScript](https://img.shields.io/badge/Frontend-JavaScript-yellow?style=for-the-badge&logo=javascript)](https://developer.mozilla.org/en-US/docs/Web/JavaScript) [![AI](https://img.shields.io/badge/AI-News%20Summarization-green?style=for-the-badge)]()

---

## 🎯 Project Overview

AI News Streamer is a full-stack web application designed to improve news consumption by combining:
- News aggregation workflows
- AI-powered summarization
- Backend processing pipelines
- Stream-style frontend presentation

The application fetches and processes news content on the backend while presenting summarized articles through a lightweight browser-based interface.

The repository follows a traditional web application structure with:
- Python backend services
- Frontend JavaScript/CSS/HTML assets
- AI/news processing workflows
- Modular project organization

---

## ✨ Key Capabilities

- ✅ **News aggregation workflows** for fetching latest articles
- ✅ **AI-powered summarization** for streamlined content consumption
- ✅ **Python backend architecture** for request and processing logic
- ✅ **Interactive frontend interface** using JavaScript, HTML, and CSS
- ✅ **Stream-style article presentation** optimized for readability
- ✅ **Modular backend/frontend separation** for scalability and maintainability

---

## 🏗️ Architecture

```text
┌─────────────────────────┐
│      Browser Client     │
│   HTML / CSS / JS UI    │
└────────────┬────────────┘
             │ HTTP Requests
             ▼
┌─────────────────────────┐
│      Python Backend     │
│      Application API    │
└────────────┬────────────┘
             │
             ▼
┌─────────────────────────┐
│ News Fetching &         │
│ Processing Layer        │
├─────────────────────────┤
│ • Article Retrieval     │
│ • AI Summarization      │
│ • Data Processing       │
└─────────────────────────┘
```

The architecture separates frontend presentation from backend processing workflows, making the system easier to maintain and extend.

---

## 🛠️ Technology Stack

| Layer | Technology |
|---|---|
| **Backend** | Python |
| **Framework** | Flask-style web architecture |
| **Frontend** | JavaScript, HTML, CSS |
| **AI Workflow** | News summarization pipeline |
| **Application Style** | Full-stack web application |
| **Dependencies** | Defined in `requirements.txt` |

---

## 📁 Project Structure

```text
AI_News_Streamer/
├── app/                 # Backend Python application logic
├── static/              # Frontend assets (JS, CSS, HTML)
├── requirements.txt     # Python dependencies
├── .gitignore           # Git ignore rules
└── README.md            # Project documentation
```

### Core Project Areas

- **`app/`** — Backend routes, processing logic, and AI/news workflows
- **`static/`** — Frontend assets and browser-side UI logic
- **`requirements.txt`** — Dependency management for backend services

---

## 🚀 Getting Started

### Prerequisites

- Python 3.10+
- pip package manager

### Installation & Setup

1. **Clone the repository**
```bash
git clone https://github.com/Neel654/AI_News_Streamer.git
cd AI_News_Streamer
```

2. **Create a virtual environment**
```bash
python -m venv .venv
```

3. **Activate the environment**

#### Windows
```bash
.venv\Scripts\activate
```

#### macOS/Linux
```bash
source .venv/bin/activate
```

4. **Install dependencies**
```bash
pip install -r requirements.txt
```

5. **Run the application**
```bash
python -m app
```

### Alternative Flask Startup

```bash
flask run
```

After startup, open the local development URL in your browser to access the news streaming interface.

---

## 🔄 Application Workflow

### News Processing Lifecycle

1. The backend fetches or receives news article data
2. Articles are processed and prepared for summarization
3. AI-powered workflows generate condensed summaries
4. Processed articles are served through the backend
5. The frontend renders content in a stream-style UI

---

## 📌 Project Highlights

### Full-Stack Engineering
- Backend/frontend separation
- Python web application architecture
- Static asset management
- Browser-based content rendering

### AI & Data Workflow
- News aggregation concepts
- AI summarization integration
- Content processing pipelines
- Streamlined information delivery

### Software Engineering Focus
- Modular repository structure
- Maintainable application organization
- Scalable backend workflow design
- Frontend UI integration

---

## 💡 Why This Project Stands Out

This project combines:
- Web application engineering
- Backend processing workflows
- Frontend UI implementation
- AI-assisted content summarization

Unlike a static news webpage, AI News Streamer demonstrates practical experience building a multi-layer application that processes and transforms content dynamically.

---

## 🧠 Learning Outcomes

This project demonstrates practical experience with:
- Python backend development
- Full-stack web application architecture
- Frontend integration using JavaScript/HTML/CSS
- AI-assisted content workflows
- Request handling and application routing
- Modular project organization

---

## 🚀 Future Improvements

Potential future enhancements:
- Real-time news streaming
- User authentication and personalization
- LLM-powered summarization upgrades
- Topic/category filtering
- Sentiment analysis integration
- Infinite scrolling UI
- Deployment with Docker and cloud hosting

---

## 📄 Resume-Ready Description

- Built a Python-based AI news streaming platform integrating backend news processing workflows, AI-powered summarization, and a JavaScript frontend to deliver summarized articles through a stream-style web interface.

---

## 👤 Author

**Neel Prajapati**  
Computer Science Student @ Toronto Metropolitan University

---

⭐ Feel free to explore the repository, contribute improvements, or fork the project!
