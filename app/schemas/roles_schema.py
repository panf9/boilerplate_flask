from flask_restx import fields
from marshmallow_sqlalchemy import SQLAlchemyAutoSchema
from app.models.roles_model import RoleModel


class RoleRequestSchema:
    def __init__(self, namespace):
        self.ns = namespace

    def create(self):
        return self.ns.model('Role Create', {
            'name': fields.String(required=True, max_lenght=8)
        }
        )


class RoleResponseSchema(SQLAlchemyAutoSchema):
    class Meta:
        model: RoleModel
