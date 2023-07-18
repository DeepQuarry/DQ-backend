from typing import Any, List
from db import crud
from app.api import deps
from fastapi import APIRouter, Depends, HTTPException
from app.models.dataset import Dataset
import schemas
from sqlalchemy.orm import Session


router = APIRouter()

@router.get("", response_model=List[schemas.Dataset])
def get_datasets(
    db: Session = Depends(deps.get_db),
    skip: int = 0,
    limit: int = 10
    ) -> List[Dataset]:
    return crud.dataset.get_multi(db=db, skip=skip, limit=limit)

@router.get("/{id}", response_model=schemas.Dataset)
def get_dataset(*, db: Session = Depends(deps.get_db), id: int):
    dataset = crud.dataset.get(db=db, id=id)
    if not dataset:
        raise HTTPException(status_code=404, detail=f"Dataset with id {id} not found")
    return dataset

@router.delete("/{id}", response_model=schemas.Dataset)
def delete_item(*, db: Session = Depends(deps.get_db), id: int):
    dataset = crud.dataset.get(db=db, id=id)
    if not dataset:
        raise HTTPException(status_code=404, detail=f"Dataset with id {id} not found")
    dataset = crud.dataset.remove(db=db, id=id)
    return dataset
