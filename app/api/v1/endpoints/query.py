from typing import List

from fastapi import APIRouter, BackgroundTasks, Depends, HTTPException
from sqlalchemy.orm import Session
from app import schemas

from app.api import deps
from app.data.serp.bing import Scraper
from app.db import crud
from app.models.query import Query

router = APIRouter()


@router.get(
    "", response_model=List[schemas.Query], dependencies=[Depends(deps.api_key_auth)]
)
async def get_queries(
    db: Session = Depends(deps.get_db), skip: int = 0, limit: int = 100
) -> List[Query]:
    return crud.query.get_multi(db=db, skip=skip, limit=limit)


@router.get(
    "/{id}", response_model=schemas.Query, dependencies=[Depends(deps.api_key_auth)]
)
async def get_query(*, db: Session = Depends(deps.get_db), id: int):
    query = crud.query.get(db=db, id=id)
    if not query:
        raise HTTPException(status_code=404, detail=f"Query with id {id} not found")
    return query


def scrape_task(query: Query, db: Session):
    bing_scraper = Scraper(
        threads=query.threads, image_limit=query.image_limit, is_adult=query.is_adult
    )
    bing_scraper.scrape_images(query, db)


@router.post(
    "", response_model=schemas.Query, dependencies=[Depends(deps.api_key_auth)]
)
async def create_item(
    *,
    background_tasks: BackgroundTasks,
    db: Session = Depends(deps.get_db),
    query_in: schemas.QueryCreate,
):
    query = crud.query.create(db=db, obj_in=query_in)
    background_tasks.add_task(scrape_task, query, db)
    return query
