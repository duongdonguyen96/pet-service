from fastapi import APIRouter

from app.api.v1.example.customer import router as router_customer

router_module = APIRouter()

router_module.include_router(
    router=router_customer.router, prefix="/customers",
)
