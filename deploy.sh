dnf install -y git python3-pip
firewall-cmd --permanent --add-service=http
firewall-cmd --reload
python app.py
