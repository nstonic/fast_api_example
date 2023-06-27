from uuid import UUID

from sqlalchemy.orm import Session

import dto
import models


def create_item(data: dto.Example, db: Session):
    item = models.Example(text=data.text)
    try:
        db.add(item)
        db.commit()
        db.refresh(item)
    except Exception as ex:
        print(ex)
    return item


def get_item(uuid: UUID, db: Session):
    return db.query(models.Example).filter(models.Example.uuid == uuid).first()


def delete_item(uuid: UUID, db: Session):
    item = db.query(models.Example).filter(models.Example.uuid == uuid).delete()
    db.commit()
    return item
