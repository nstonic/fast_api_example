import uuid as uu
from fastapi import APIRouter, Path, HTTPException
from starlette.status import HTTP_200_OK, HTTP_404_NOT_FOUND

router = APIRouter()

items = []


@router.post('/new')
async def create(text: str) -> dict:
    item = {'uuid': str(uu.uuid4()),
            'text': text}
    items.append(item)
    return item


@router.get('/all')
async def get_all() -> list[dict]:
    return items


@router.get('/{uuid}')
async def get_item(uuid: str = Path(..., title="UUID of item")) -> dict:
    item, *_ = list(filter(
        lambda x: x['uuid'] == uuid,
        items
    ))
    return item


@router.get('/{count}')
async def get_item(count: int = Path(..., title="Requested count of items")) -> list[dict]:
    count = min(count, len(items) - 1)
    return items[:count]


@router.delete('/{uuid}', status_code=HTTP_200_OK)
async def get_item(uuid: str = Path(..., title="UUID of item for deleting")) -> dict:
    for item in items:
        if item['uuid'] == uuid:
            items.remove(item)
            return {'message': 'Item deleted successfully'}
    raise HTTPException(
        status_code=HTTP_404_NOT_FOUND,
        detail=f"Item with {uuid=} doesn't exist",
    )
