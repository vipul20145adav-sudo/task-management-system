from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.core.jwt import create_access_token

from app.db.database import get_db
from app.schemas.user import UserCreate, UserResponse, UserLogin
from app.services.user_service import create_user, authenticate_user
from app.core.dependencies import get_current_user

router = APIRouter(
    prefix="/users",
    tags=["Users"]
)


@router.post("/signup", response_model=UserResponse)
def signup(user: UserCreate, db: Session = Depends(get_db)):
    return create_user(db, user)

@router.post("/login")
def login(user: UserLogin, db: Session = Depends(get_db)):

    authenticated_user = authenticate_user(db, user)

    access_token = create_access_token(
        data={
            "sub": authenticated_user.email,
            "role": authenticated_user.role
        }
    )

    return {
        "access_token": access_token,
        "token_type": "bearer"
    }

@router.get("/me")
def get_profile(current_user=Depends(get_current_user)):
    return current_user