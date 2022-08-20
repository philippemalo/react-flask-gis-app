import graphene
from graphene import relay
from graphene_sqlalchemy import SQLAlchemyObjectType, SQLAlchemyConnectionField
from .models import Shape as ShapeModel


class Shape(SQLAlchemyObjectType):
    class Meta:
        model = ShapeModel
        interfaces = (relay.Node, )


class Query(graphene.ObjectType):
    node = relay.Node.Field()
    # Allows sorting over multiple columns, by default over the primary key
    all_shapes = SQLAlchemyConnectionField(Shape.connection)

schema = graphene.Schema(query=Query)