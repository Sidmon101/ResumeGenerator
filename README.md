# 📝 Django Resume Builder

A web-based application built with Django that allows users to create, preview, and download professional resumes in PDF format using customizable templates.

---

## 🚀 Features

- Submit personal and professional details via a user-friendly form
- Choose from multiple resume templates
- View generated resumes in-browser
- Download resumes as PDF files with custom filenames
- Admin panel to view all user submissions

---

## 🛠️ Tech Stack

- **Backend**: Django, Python  
- **Frontend**: HTML, CSS, JavaScript  
- **PDF Generation**: WeasyPrint  
- **Database**: SQLite (default, can be swapped with PostgreSQL/MySQL)  
- **Version Control**: Git & GitHub  

---

## 📦 Installation

1. **Clone the repository**  
   ```bash
   git clone https://github.com/your-username/your-repo-name.git
   cd your-repo-name
   ```

2. **Create a virtual environment**  
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies**  
   ```bash
   pip install -r requirements.txt
   ```

4. **Run migrations**  
   ```bash
   python manage.py migrate
   ```

5. **Start the development server**  
   ```bash
   python manage.py runserver
   ```

---

## 📄 Usage

- Navigate to `http://127.0.0.1:8000/`
- Fill out the resume form and submit
- View your resume or download it as a PDF
- Visit `/user_list/` to see all generated resumes

---

## 📁 Folder Structure

```
mysite/
│
├── pdf/                # App containing views, templates, models
  ── templates/pdf/      # HTML templates for forms and resumes
├── manage.py
└── requirements.txt
```

---

