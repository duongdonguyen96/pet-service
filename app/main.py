import uvicorn
from dotenv import load_dotenv
from fastapi import FastAPI, Request, status
from fastapi.encoders import jsonable_encoder
from fastapi.exceptions import HTTPException
from fastapi.openapi import utils
from fastapi.responses import ORJSONResponse
from starlette.middleware.cors import CORSMiddleware
from starlette.responses import JSONResponse

# load file config
load_dotenv('.env')  # noqa

from app.api.base.except_custom import ExceptionHandle
from app.api.v1 import router as v1_router
from app.settings.config import APPLICATION
from app.settings.middleware import middleware_setting

app = FastAPI(
    title=APPLICATION["project_name"],
    debug=APPLICATION["debug"],
    version=APPLICATION["version"],
    docs_url="/docs",
    default_response_class=ORJSONResponse,
    openapi_url="/openapi.json" if APPLICATION["debug"] else None
)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(router=v1_router.router, prefix="/api/v1")


@app.middleware("http")
async def time_header(request: Request, call_next):
    return await middleware_setting(request=request, call_next=call_next)


# handler exception
@app.exception_handler(ExceptionHandle)
async def except_custom(_: Request, exc: ExceptionHandle) -> JSONResponse:
    return JSONResponse(
        content=jsonable_encoder(
            {"data": exc.data, "errors": exc.get_message_detail()}
        ),
        status_code=exc.status_code,
    )


@app.exception_handler(HTTPException)
async def http_except_custom(_: Request, exc: HTTPException) -> JSONResponse:
    errors = [
        {
            "loc": None,
            "msg": None,
            "detail": f"{exc.detail}",
        }
    ]

    return JSONResponse(
        content=jsonable_encoder({"data": None, "errors": errors}),
        status_code=status.HTTP_400_BAD_REQUEST,
    )


utils.HTTP_422_UNPROCESSABLE_ENTITY = status.HTTP_400_BAD_REQUEST

if __name__ == "__main__":
    uvicorn.run('app.main:app', host="127.0.0.1", port=8001, reload=True)
