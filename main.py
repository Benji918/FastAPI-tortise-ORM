from fastapi import FastAPI, Request, status
from database import init_db
import uvicorn
from crud import router
from fastapi.exceptions import RequestValidationError
from fastapi.responses import JSONResponse

app = FastAPI()
app.include_router(router)
init_db(app)

@app.get("/")
def read_root():
    return {"Hello": "World"}

@app.exception_handler(RequestValidationError)
async def custom_validation_handler(request: Request, exc: RequestValidationError):
    errors = []
    for error in exc.errors():
        error_copy = dict(error)
        if "ctx" in error_copy and isinstance(error_copy["ctx"], dict):
            error_copy["ctx"] = {
                k: str(v) if isinstance(v, Exception) else v
                for k, v in error_copy["ctx"].items()
            }
        errors.append(error_copy)

    return JSONResponse(
        status_code=status.HTTP_422_UNPROCESSABLE_ENTITY,
        content={"detail": errors, "message": "An error occurred while processing the request."},
    )

if __name__ == "__main__":
    uvicorn.run("main:app", host="127.0.0.1", port=8000, reload=True)
