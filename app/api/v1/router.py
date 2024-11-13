from fastapi import APIRouter

from app.api.v1.user.router import router as router_user
from app.api.v1.user.router import router_auth

router = APIRouter()

router.include_router(router=router_auth, prefix="", tags=["[AUTHEN]"])
router.include_router(router=router_user, prefix="", tags=["[USERS]"])
