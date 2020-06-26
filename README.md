# Mini-Projet
Ce projet consiste à mettre en place une base de données des patients et d'attribuer à chacun un parrain ou une marraine pour un meilleur suivi.

pip install -r requirements.txt
python manage.py migrate
python manage.py createsuperuser
python manage.py makemigrations Retention
python manage.py migrate
python manage.py runserver
