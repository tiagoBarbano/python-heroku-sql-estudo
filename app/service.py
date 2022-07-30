from fastapi import APIRouter, Body, HTTPException, status, Depends
from app.schema import UserSchema
from app.repository import add_user, get_all_users, get_user_by_id, update_user, delete_user
from app.database import get_db
from sqlalchemy.ext.asyncio import AsyncSession
from app.cache import get_all, Order

from app.model import UserModel

router = APIRouter()


@router.get("/hello-world")
async def root():
    return {"message": "Hello World"}

@router.post("/", response_description="user data added into the database")
async def add_user(user: UserSchema = Body(...), db: AsyncSession = Depends(get_db)):
    new_user = UserModel(nome=user.nome, idade=user.idade, email=user.email)
    db.add(new_user)
    return new_user

@router.get("/", response_description="users retrieved")
async def get_users(db: AsyncSession = Depends(get_db)):
    try:
        users = await get_all()
        
        #user = await get_all_users(db)

        if users == []:
            raise HTTPException(status_code=status.HTTP_204_NO_CONTENT)

        return users
    except HTTPException as ex:
        if(hasattr(ex, 'status_code')):
            raise HTTPException(status_code=ex.status_code)
        
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR)


@router.get("/{id}", response_description="user data retrieved")
async def get_user_data(id: int, db: AsyncSession = Depends(get_db)):
    user = await get_user_by_id(db, id)
    if user:
        return user
    
    raise HTTPException(status_code=status.HTTP_204_NO_CONTENT) 

@router.put("/{id}")
async def update_user_data(id: str, req: UserSchema = Body(...), db: AsyncSession = Depends(get_db)):
    updated_user = await update_user(db, id, req)
    
    if updated_user:
        return updated_user

    raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Problema na atualizacao")

    
@router.delete("/{id}", response_description="user data deleted from the database")
async def delete_user_data(id: str,  db: AsyncSession = Depends(get_db)):
    delete_user = await delete_user(db, id)
    
    if delete_user:
        return delete_user
    
    raise HTTPException(status_code=status.HTTP_204_NO_CONTENT)    