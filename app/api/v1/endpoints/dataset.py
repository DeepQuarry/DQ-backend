from typing import List
from app import schemas

from app.db import crud
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.api import deps
from app.models.dataset import Dataset

router = APIRouter()


@router.get(
    "", response_model=List[schemas.Dataset], dependencies=[Depends(deps.api_key_auth)]
)
async def get_datasets(
    db: Session = Depends(deps.get_db), skip: int = 0, limit: int = 100
) -> List[Dataset]:
    return crud.dataset.get_multi(db=db, skip=skip, limit=limit)


@router.get(
    "/{id}", response_model=schemas.Dataset, dependencies=[Depends(deps.api_key_auth)]
)
async def get_dataset(*, db: Session = Depends(deps.get_db), id: int):
    dataset = crud.dataset.get(db=db, id=id)
    if not dataset:
        raise HTTPException(status_code=404, detail=f"Dataset with id {id} not found")
    return dataset


# @router.delete("/{id}", response_model=schemas.Dataset)
# async def delete_item(*, db: Session = Depends(deps.get_db), id: int):
#     dataset = crud.dataset.get(db=db, id=id)
#     if not dataset:
#         raise HTTPException(status_code=404, detail=f"Dataset with id {id} not found")
#     dataset = crud.dataset.remove(db=db, id=id)
#     return dataset
