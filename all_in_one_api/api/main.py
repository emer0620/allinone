import time
from fastapi import FastAPI, Request

from api.branch import router as branch_router
from api.department import router as department_router
from api.employee_data import router as employee_data_router
from api.user_account import router as user_account_router
from api.ps import router as ps_router
from api.spims import router as spims_router

app = FastAPI(title='All in One Application')

@app.middleware("http")
async def add_process_time_header(request: Request, call_next):
    start_time = time.time()
    response = await call_next(request)
    process_time = time.time() - start_time
    response.headers["X-Process-Time"] = str(process_time)
    return response

app.include_router(branch_router.branch_router)
app.include_router(department_router.department_router)
app.include_router(employee_data_router.employee_data_router)
app.include_router(user_account_router.user_account_router)
app.include_router(ps_router.ps_router)
app.include_router(spims_router.spims_router)
