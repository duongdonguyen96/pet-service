import logging
from typing import List

from fastapi import APIRouter, Body, Depends
from starlette import status

from app.api.base.oauth import get_current_user
from app.api.base.schema import ResponseData, AuthenticationRes, Authentication, UserInfo
from app.api.base.swagger import swagger_response
from app.api.v1.user.examples import (
    DATA_EXAMPLE_CREATE_USER
)
from app.api.v1.user.schema import UserRq, UserRes, ChangePasswordRq
from app.api.v1.user.service import UserService
from app.utils.functions import get_current_time

router = APIRouter()
router_auth = APIRouter()


@router.get(
    path="/me",
    name="get info of me",
    description="get info of me",
    responses=swagger_response(
        response_model=ResponseData[None],
        success_status_code=status.HTTP_200_OK
    ),
)
async def view_me(current_user: UserInfo = Depends(get_current_user)):
    user_info = await UserService(current_user).me()
    return ResponseData(**user_info)


@router_auth.post(
    path="/login",
    name="login",
    description="Login",
    responses=swagger_response(
        response_model=ResponseData[AuthenticationRes],
        success_status_code=status.HTTP_200_OK
    ),
)
async def view_login(
        user: Authentication = Body(...),
        current_user=None
):
    data = await UserService(current_user).login(user)
    return ResponseData[AuthenticationRes](**data)


@router.post(
    path="/user",
    name="Customer",
    description="create new user",
    responses=swagger_response(
        response_model=ResponseData[UserRes],
        success_status_code=status.HTTP_200_OK
    ),
)
async def view_create_user(
        user: UserRq = Body(..., example=DATA_EXAMPLE_CREATE_USER),
):
    return await UserService().create_user(user)


@router.get(
    path="/users",
    name="User",
    description="get users",
    responses=swagger_response(
        response_model=ResponseData[List[UserRes]],
        success_status_code=status.HTTP_200_OK,
    ),
)
async def view_get_all_user(current_user: UserInfo = Depends(get_current_user)):
    return await UserService(current_user).get_users()


@router.patch(
    path="/users/change-password",
    name="User",
    description="change-password",
    responses=swagger_response(
        response_model=ResponseData[str],
        success_status_code=status.HTTP_200_OK,
    ),
)
async def view_change_password(
        p: ChangePasswordRq,
        current_user: UserInfo = Depends(get_current_user)
):
    return await UserService(current_user).change_password(p)
