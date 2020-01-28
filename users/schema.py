import graphene
from .types import UserType
from .models import User


class Query(object):

    rooms = graphene.List("rooms.schema.RoomType")
    user = graphene.Field(UserType, id=graphene.Int(required=True))

    def resolve_user(self, info, id):
        try:
            return User.objects.get(id=id)
        except:
            return None
