# Airbnb API

REST & GraphQL API of the Airbnb Clone using Django REST Framework and Graphene GraphQL

### API Actions

- [X] List Rooms (with Pagination)
- [ ] Filter Rooms
- [ ] Search By Coords
- [ ] Login (JWT)
- [ ] Create Account
- [ ] See Room
- [ ] Add Room to Favourites
- [ ] See Favs
- [ ] See my Profile
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

