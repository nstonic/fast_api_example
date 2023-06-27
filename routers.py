from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

import dto
import service
from db import get_db

router = APIRouter()


@router.post('/new')
async def create(text: dto.Example, db: Session = Depends(get_db)):
    return service.create_item(text, db)
