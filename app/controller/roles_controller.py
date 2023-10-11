from http import HTTPStatus
from app import db
from app.models.roles_model import RoleModel
from app.schemas.roles_schema import RoleResponseSchema


class RoleController:
    def __init__(self):
        self.db = db
        self.model = RoleModel
        self.schema = RoleResponseSchema

    def fetch_all(self):
        # SELECT * FROM roles;
        record = self.model.all()
        response = self.schema(many=True)
        print(response.dump(record))
        return response.dump(record)

    def save(self, body):
        try:
            record_new = self.model.create(**body)
            self.db.session.add(record_new)
            self.db.session.commit()
            return {
                'message': f'Se creó {body["name"]} correctamente'
            }, HTTPStatus.OK
        except Exception as e:
            self.db.session.rollback()
            return {
                'message': 'Ocurrió un error',
                'error': str(e)
            }, HTTPStatus.INTERNAL_SERVER_ERROR
        finally:
            self.db.session.close()

    def find_by_id(self, id):
        try:
            record = self.model.where(id=id).first()
            response = self.schema(many=False)
            return response.dump(record), HTTPStatus.OK
        except Exception as e:
            return {
                'message': 'Ocurrió un error',
                'error': str(e)
            }, HTTPStatus.INTERNAL_SERVER_ERROR
