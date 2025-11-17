firewall-cmd --permanent --add-service=http
firewall-cmd --reload
dnf install -y git python3-pip screen
pip install gunicorn
chmod 777 /run/screen
screen -S app
gunicorn -w 3 -b 0.0.0.0:80 app:app
