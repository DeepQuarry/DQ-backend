from app.db.crud.base import CRUDBase
from app.models.dataset import Dataset
from app.models.image import Image
from app.models.query import Query
from app.models.user import User
from app.schemas.dataset import DatasetCreate, DatasetUpdate
from app.schemas.query import QueryCreate, QueryUpdate
from app.schemas.user import UserCreate, UserUpdate

dataset = CRUDBase[Dataset, DatasetCreate, DatasetUpdate](Dataset)
user = CRUDBase[User, UserCreate, UserUpdate](User)
query = CRUDBase[Query, QueryCreate, QueryUpdate](Query)
