# Airbnb API

REST & GraphQL API of the Airbnb Clone using Django REST Framework and Graphene GraphQL

### API Actions

#### Rooms

- [x] List Rooms (with Pagination)
- [x] See Room

#### Users

- [x] See User
- [x] Login (JWT)
- [x] Create Account
- [x] See My Profile
- [] Add Room to Favourites
- [ ] Edit Profile

### initial 

pipenv --three
pipenv shell
pipenv install
python manage.py migrate
python manage.py createsuperuser
python manage.py mega_seed
python manage.py runserver

pipenv install graphene-django

