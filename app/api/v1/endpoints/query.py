from typing import Any, List

from app.db import crud
from app.serp.bing import Scraper
from app.api import deps
from fastapi import APIRouter, BackgroundTasks, Depends, HTTPException
from app.models.query import Query
import schemas
from sqlalchemy.orm import Session


router = APIRouter()

@router.get("", response_model=List[schemas.Query])
async def get_queries(
    db: Session = Depends(deps.get_db),
    skip: int = 0,
    limit: int = 100
    ) -> List[Query]:
    return crud.query.get_multi(db=db, skip=skip, limit=limit)

@router.get("/{id}", response_model=schemas.Query)
async def get_query(*, db: Session = Depends(deps.get_db), id: int):
    query = crud.query.get(db=db, id=id)
    if not query:
        raise HTTPException(status_code=404, detail=f"Query with id {id} not found")
    return query

def scrape_task(query: Query, db: Session):
    bing_scraper = Scraper(image_limit=10, threads=5)
    bing_scraper.scrape_images(query, db)

@router.post("", response_model=schemas.Query)
async def create_item(*, background_tasks: BackgroundTasks, db: Session = Depends(deps.get_db), query_in: schemas.QueryCreate):
    query = crud.query.create(db=db, obj_in=query_in)
    background_tasks.add_task(scrape_task, query, db)
    return query

