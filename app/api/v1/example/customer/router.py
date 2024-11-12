import logging
from typing import List

from fastapi import APIRouter, Body
from starlette import status

from app.api.base.schema import ResponseData
from app.api.base.swagger import swagger_response
from app.api.v1.example.customer.examples import (
    DATA_EXAMPLE_CREATE_USER
)
from app.api.v1.example.customer.schema import CustomerRq, CustomersRes
from app.api.v1.example.customer.service import UserService
from app.utils.functions import get_current_time

router = APIRouter()


@router.get(
    path="/test/",
    name="test",
    description="Test",
    responses=swagger_response(
        response_model=ResponseData[str],
        success_status_code=status.HTTP_200_OK
    ),
)
def test():
    logging.info('logging Hello World!!! OK')
    return {
        'message': f'Hello World!!! {get_current_time()}'
    }


@router.post(
    path="/",
    name="Customer",
    description="create new customer",
    responses=swagger_response(
        response_model=ResponseData[str],
        success_status_code=status.HTTP_200_OK
    ),
)
async def view_create_user(
        user: CustomerRq = Body(..., example=DATA_EXAMPLE_CREATE_USER),
):
    return await UserService().create_user(user)


@router.get(
    path="/",
    name="Customer",
    description="get customers",
    responses=swagger_response(
        response_model=ResponseData[List[CustomersRes]],
        success_status_code=status.HTTP_200_OK,
    ),
)
async def view_get_all_user(
):
    return await UserService().get_users()
