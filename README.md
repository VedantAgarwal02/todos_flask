# 📌 Todo App (Flask + Modular MVC Architecture)

A clean, maintainable, and fully modular **Todo Management Application** built with **Flask (3.x)** and **SQLite**, following an MVC-style architecture with Blueprints, Models, and centralized Extensions.

This project demonstrates best practices for structuring medium-sized Flask applications, separating responsibilities clearly across modules.

---

## 🚀 Features

### 🧩 Core Functionality
- Add new tasks  
- View all tasks  
- Edit existing tasks  
- Delete tasks  
- Mark tasks as completed  

### ⚙️ Technical Highlights
- Modular structure using Flask Blueprints
- MVC-style organization:
  - **M**odels → `app/models.py`
  - **V**iews → `app/templates/...`
  - **C**ontrollers → `app/blueprints/...`
- SQLite database with SQLAlchemy ORM
- App factory pattern
- Clean separation of concerns

---

## 📁 Project Structure

```
todo_modular/
├── run.py
├── app/
│   ├── __init__.py
│   ├── config.py
│   ├── extensions.py
│   ├── models.py
│   ├── blueprints/
│   │   └── tasks/
│   │       ├── __init__.py
│   │       └── routes.py
│   └── templates/
│       ├── layout.html
│       └── tasks/
│           ├── list.html
│           └── add.html
├── static/
│   ├── css/style.css
│   └── js/app.js
└── todos.db (auto-created)
```

---

## 🛠️ Installation & Setup

### 1️⃣ Clone the repository  
```bash
git clone <your-repo-url> todo_modular
cd todo_modular
```

### 2️⃣ Create and activate a virtual environment  

**Windows**
```bash
python -m venv venv
venv\Scripts\activate
```

**Linux/Mac**
```bash
python3 -m venv venv
source venv/bin/activate
```

### 3️⃣ Install dependencies  
```bash
pip install -r requirements.txt
```

### 4️⃣ Run the application  
```bash
python run.py
```

App runs at: **http://127.0.0.1:5000**

---

## 📦 Deployment

To run with Gunicorn:
```bash
gunicorn -w 4 "run:app"
```

Ask for Docker support if needed.

---

## 📄 License
MIT License.
