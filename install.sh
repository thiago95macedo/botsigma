# python manage.py startapp iqoption (Criar APP)
# python manage.py makemigrations iqoption (Criar tabelas dos models no banco de dados)
# python manage.py showmigrations
# python manage.py migrate --fake botsigma zero


sudo apt install python3-venv

sudo apt install gcc g++ make
curl -fsSL https://deb.nodesource.com/setup_18.x | sudo -E bash -
sudo apt-get install nodejs

sudo apt install postgresql postgresql-contrib
sudo -u postgres psql -e --command "CREATE USER sigma WITH SUPERUSER PASSWORD 'sigma1q2w3e4r'"
sudo -u postgres createdb botsigma

python3 -m venv .venv
source .venv/bin/activate

pip install --upgrade pip
pip install --upgrade setuptools
pip install -r requeriments.txt
pip install -U https://github.com/thiago95macedo/iqoptionapi/archive/refs/heads/master.zip

django-admin startproject botsigma .
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver 127.0.0.1:1995

