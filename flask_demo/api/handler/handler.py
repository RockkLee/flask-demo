from flask_restx import Api
from flask_demo.helper.exception import CustomException


def register_exception_handlers(api: Api):
    @api.errorhandler(CustomException)
    def custom_exception_handler(error: CustomException):
        return {'message': error.message}, error.status_code
