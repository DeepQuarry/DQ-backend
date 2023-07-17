from app.db.crud.base import CRUDBase
from app.models.dataset import Dataset
from app.models.image import Image
from app.models.user import User
from app.schemas.dataset import DatasetCreate, DatasetUpdate
from app.schemas.image import ImageCreate, ImageUpdate
from app.schemas.user import UserCreate, UserUpdate

dataset = CRUDBase[Dataset, DatasetCreate, DatasetUpdate]
image = CRUDBase[Image, ImageCreate, ImageUpdate]
user = CRUDBase[User, UserCreate, UserUpdate]
