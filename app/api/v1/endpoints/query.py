from typing import Any, List
from db import crud
from app.api import deps
from fastapi import APIRouter, Depends, HTTPException
from app.models.query import Query
import schemas
from sqlalchemy.orm import Session


router = APIRouter()

@router.get("", response_model=List[schemas.Query])
def get_querys(
    db: Session = Depends(deps.get_db),
    skip: int = 0,
    limit: int = 10
    ) -> List[Query]:
    return crud.query.get_multi(db=db, skip=skip, limit=limit)

@router.get("/{id}", response_model=schemas.Query)
def get_query(*, db: Session = Depends(deps.get_db), id: int):
    query = crud.query.get(db=db, id=id)
    if not query:
        raise HTTPException(status_code=404, detail=f"Query with id {id} not found")
    return query

@router.delete("/{id}", response_model=schemas.Query)
def delete_item(*, db: Session = Depends(deps.get_db), id: int):
    query = crud.query.get(db=db, id=id)
    if not query:
        raise HTTPException(status_code=404, detail=f"Query with id {id} not found")
    query = crud.query.remove(db=db, id=id)
    return query

