from app import api
from flask_restx import Resource
from flask import request
from http import HTTPStatus
from app.controller.roles_controller import RoleController
from app.schemas.roles_schema import RoleRequestSchema

role_ns = api.namespace(
    name='Roles',
    description='rutas de módulos roles',
    path='/roles'  # Esta es la ruta raiz
)

schema_request = RoleRequestSchema(role_ns)

# CRUD


@role_ns.route('')
class Roles(Resource):
    def get(self):
        '''Listar todos los modelos'''
        controller = RoleController()
        return controller.fetch_all()

    @role_ns.expect(schema_request.create(), validate=True)
    def post(self):
        '''Crear un nuevo rol'''
        controller = RoleController()
        return controller.save(request.json)


@role_ns.route('/<int:id>')
class find_by_id(Resource):
    def get(self, id):
        '''Obtener un rol por su id'''
        controller = RoleController()
        return controller.find_by_id(id)

    def put(self, id):
        '''Actualizar algún campo del rol enviando todos los datos'''
        return f'Modificando el elemento con ID: {id}', HTTPStatus.OK

    def patch(self, id):
        '''Actualizar ulgun dato del rol enviando únicamentos los datos necesarios'''
        return f'Modificando con datos parciales el elemento con ID: {id}', HTTPStatus.OK

    def delete(self, id):
        '''Eliminar un rol por su id'''
        return f'Eliminado el elemento con ID: {id}', HTTPStatus.OK

# # Listado GET
# @app.route('/roles', methods=['GET'])
# def list_roles():
#     return 'Lista de roles'

# # Creación POST
# @app.route('/roles', methods=['POST'])
# def create_roles():
#     return 'creación de rol', HTTPStatus.CREATED

# # Actualización
# @app.route('/role/<int:id>', methods=['PUT', 'PATCH'])
# def update_roles(id):
#     return f'Modificando el {id}', HTTPStatus.OK

# # Eliminar
# @app.route('/role/<int:id>', methods=['DELETE'])
# def delete_roles(id):
#     return f'Eliminado {id}', HTTPStatus.OK
