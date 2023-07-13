from typing import Union
from fastapi import FastAPI

app = FastAPI()


@app.get('/')
async def read_root():
    return {'Hello': 'World'}

@app.get('/items/{item_id}')
async def read_item(item_id: int, q: Union[str, None] = None):
    return {'item': item_id, 'q': q}

FakeDatabase = {
    1: {'task': 'Clean car'},
    2: {'task': 'Write blog'},
    3: {'task': 'Start stream'}
}

@app.post('/')
def AddItem(task: str):
    newid = len(FakeDatabase.keys()) + 1
    FakeDatabase[newid] = {'task': task}

    return FakeDatabase