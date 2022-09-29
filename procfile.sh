export HEROKU=true
python manage.py migrate
python manage.py loaddata initial_wishlist_data.json