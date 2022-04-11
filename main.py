from fastapi import FastAPI

from app.routers import auth, items, users

app = FastAPI(
    description='Simple API for warehouse with users, items, role system '
                'and JWT-token based authentication.',
)

app.include_router(users.router)
app.include_router(auth.router)
app.include_router(items.router)

