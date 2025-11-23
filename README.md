📌 Ansible Web Application Deployment Project
🎯 Overview
This project deploys a Flask web application with a MySQL database backend using Ansible, Docker, and Ansible Vault.
The deployment includes:
-- Database server installation & configuration
-- Web application Docker image build
-- Deployment of the Flask app container
-- Secure storage of credentials using Ansible Vault
🗂 Directory Structure
ansible-project/
│── ansible.cfg
│── inventory.ini
│── playbook.yml
│── group_vars/
│ └── vault.yml (encrypted)
│── roles/
│ ├── db/
│ └── web/
🔐 Ansible Vault All sensitive variables (DB username, password, host, etc.) are stored in: group_vars/vault.yml Encrypted with: ansible-vault encrypt group_vars/vault.yml
▶️ Running the Deployment
1️⃣ Edit inventory.ini: Set your target VM IP.
2️⃣ Run the playbook: ansible-playbook playbook.yml --ask-vault-pass
3️⃣ Access the web app: http://:5000/
The app will return a JSON response containing the current time fetched from the database.
🧪 Testing Database Connectivity
On the web container: docker exec -it flask_app_container python3 - <<EOF import mysql.connector conn = mysql.connector.connect(host="your-host", user="your-user", password="your-pass", database="app") cursor = conn.cursor() cursor.execute("SELECT NOW();") print(cursor.fetchone()) EOF
🔐 Vault Password for Teacher: I will add password and my full documentation in the word file that I have added to teams.
