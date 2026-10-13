from contextlib import asynccontextmanager

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.models.base import Base
from app.db.session import engine

from app.api.routers.task import router as task_router


@asynccontextmanager
async def lifespan(_:FastAPI):
    Base.metadata.create_all(bind=engine)
    yield

app = FastAPI(lifespan=lifespan)
app.include_router(router=task_router)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],
    allow_methods=['*'],
    allow_headers=["*"],
)

# Categories

# class CategoryORM(Base):
#     __tablename__ = "categories"

#     name: Mapped[str]


# class CategorySchema(BaseModel):
#     id: str
#     name: str


# class CategoryCreateSchema(BaseModel):
#     name: str


# class CategoryUpdateSchema(BaseModel):
#     name: str | None = None



# def category_orm_to_model(category_orm: CategoryORM) -> CategorySchema:
#     return CategorySchema(id=category_orm.id, name=category_orm.name)


# @app.get("/categories")
# def read_categories(db: Session = Depends(get_db)) -> list[CategorySchema]:
#     categories = db.scalars(select(CategoryORM)).all()
#     return [category_orm_to_model(category) for category in categories]



# @app.post("/categories", status_code=status.HTTP_201_CREATED)
# def create_category(payload:CategoryCreateSchema, db: Session = Depends(get_db)) -> CategorySchema:
#     new_category = CategoryORM(name=payload.name)
#     db.add(new_category)
#     db.commit()

#     return category_orm_to_model(new_category)
    



# @app.patch("/categories/{category_id}")
# def update_category(category_id: str, payload: CategoryUpdateSchema, db: Session = Depends(get_db)):
#     category_for_update = db.get(CategoryORM, category_id)
    
#     if category_for_update is None:
#         raise HTTPException(
#             status_code=status.HTTP_404_NOT_FOUND,
#             detail="Category not found"
#         )

#     if payload.name is not None:
#         category_for_update.name = payload.name

#     db.commit()

#     return category_orm_to_model(category_for_update)


# @app.delete("/categories/{category_id}", status_code=status.HTTP_204_NO_CONTENT)
# def delete_category(category_id: str, db: Session = Depends(get_db)):
#     category_for_delete = db.get(CategoryORM, category_id)
#     if category_for_delete is None:
#         raise HTTPException(
#             status_code=status.HTTP_404_NOT_FOUND,
#             detail="Category not found"
#         )

#     db.delete(category_for_delete)
#     db.commit()



