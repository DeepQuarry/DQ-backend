# improt schemas here for ease of use
from app.schemas.dataset import Dataset, DatasetBase, DatasetCreate, DatasetUpdate
from app.schemas.image import Image, ImageBase, ImageCreate, ImageUpdate
from app.schemas.tag import Tag, TagBase, TagCreate, TagUpdate
from app.schemas.user import User, UserBase, UserCreate, UserUpdate

DatasetBase.update_forward_refs(TagBase=TagBase)
Tag.update_forward_refs(DatasetBase=DatasetBase)
