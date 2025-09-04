# 🧑‍💻 Deploying a Django Project on PythonAnywhere

---

## **Lesson Overview**

You will learn to deploy a Django project to PythonAnywhere, making it publicly available online.
By the end, you will have a working deployment and understand how production servers differ from local development servers.

---

## **Prerequisites**

* A working Django project locally
* Basic command-line and Git knowledge
* Free PythonAnywhere account
* GitHub (or GitLab/Bitbucket) repository

---

## **Learning Objectives**

✅ Prepare Django project for production
✅ Upload project to PythonAnywhere
✅ Configure WSGI & Virtualenv
✅ Apply database migrations
✅ Test and debug live deployment

---

## **Lesson Outline**

---

### **1. Introduction to Deployment**

📖 **Concepts:**

* Deployment = putting your app on a live server
* Why we use WSGI servers in production
* Overview of PythonAnywhere interface (Dashboard, Consoles, Files, Web tab)

---

### **2. Prepare Django Project for Deployment**

🔧 **Steps:**

1. **Update `settings.py`**

   ```python
   DEBUG = False
   ALLOWED_HOSTS = ['yourusername.pythonanywhere.com']

   STATIC_ROOT = os.path.join(BASE_DIR, "staticfiles")
   ```

2. **Collect Static Files**

   ```bash
   python manage.py collectstatic
   ```

3. **Freeze Requirements**

   ```bash
   pip freeze > requirements.txt
   ```

4. **Commit Changes**

   ```bash
   git add .
   git commit -m "Prepare project for deployment"
   git push
   ```

✅ **Checkpoint:** Repo ready for deployment.

---

### **3. Upload Project to PythonAnywhere**

1. Log in → open a **Bash console**

2. Clone your project:

   ```bash
   git clone https://github.com/<username>/<repo>.git
   cd <repo>
   ```

3. Create & activate virtual environment:

   ```bash
   python3.10 -m venv venv
   source venv/bin/activate
   pip install -r requirements.txt
   ```

---

### **4. Configure the Web App**

1. **Web Tab → Add New Web App → Manual Config → Choose Python version**

2. **Edit WSGI File**

   ```python
   import os
   import sys

   path = '/home/<username>/<repo>'
   if path not in sys.path:
       sys.path.append(path)

   os.environ['DJANGO_SETTINGS_MODULE'] = '<projectname>.settings'

   from django.core.wsgi import get_wsgi_application
   application = get_wsgi_application()
   ```

3. **Set Virtualenv Path** in the Web tab
   `/home/<username>/<repo>/venv`

---

### **5. Database & Environment Variables**

1. Run migrations:

   ```bash
   python manage.py migrate
   ```

2. Create superuser:

   ```bash
   python manage.py createsuperuser
   ```

3. Add secret keys/environment variables in **Web tab → Environment Variables**

---

### **6. Reload & Test**

* Click **Reload** in Web tab

* Visit `https://<username>.pythonanywhere.com/`

* Test functionality (forms, links, admin panel)

💡 **Troubleshooting Tip:**
Use **Error Log** in Web tab if you see a 500 error.

---

### **7. Wrap-Up & Reflection (15 mins)**

* Write a short reflection:

  * Which step was easiest?
  * Which step was hardest?
  * What would you automate next time?

Stretch Goal: Research how to add a **custom domain** in PythonAnywhere.

---

## **Deliverables**

✅ Live Django app URL
✅ Screenshot of homepage & admin panel
✅ Short reflection on deployment process

---

## **Assessment / Checkpoints**

| Step           | Deliverable     | Success Criteria                 |
| -------------- | --------------- | -------------------------------- |
| Project Prep   | Updated repo    | DEBUG=False, ALLOWED\_HOSTS set  |
| Upload         | Files on server | Virtualenv works, deps installed |
| Web Config     | Working WSGI    | App reloads without error        |
| Database Setup | Migrations done | Admin accessible                 |
| Final Test     | Live URL        | No runtime errors                |

