from fastapi import FastAPI
from routes.hello import router as hello_router
from routes.health import router as health_router

app = FastAPI()

# attach hello routes
app.include_router(hello_router)

# attach health status route
app.include_router(health_router)



