from fastapi import APIRouter

from app.api.v1.chatbot import router as router_chatbot
from app.api.v1.example import router as router_example

router = APIRouter()

router.include_router(router=router_example.router_module, prefix="/example", tags=["[Example]"])
router.include_router(router=router_chatbot.router, prefix="/chatbot", tags=["[Chatbot]"])
