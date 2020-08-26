# This script is always mounted into the container for django
# It has to be executed when django was upgraded
# It should always be executed inside, you can also execute it from the host with
# docker-compose exec fse_django bash script.sh

python manage.py makemigrations fachschaftsempfaenger
python manage.py migrate fachschaftsempfaenger
python manage.py makemigrations
python manage.py migrate
