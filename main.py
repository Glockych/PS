from http.client import HTTPException

from fastapi import FastAPI, HTTPException
import uvicorn

app = FastAPI()

books = [
    {
        'id': 1,
        'title': 'Книга про Питон',
        'author': 'Горин',
    },
    {
        'id': 2,
        'title': 'Книга про Реакт',
        'author': 'Байден',
    }
]

@app.get('/books')
def read_books():
    return books

@app.get('/books/{book_id}')
def get_book(book_id: int):
    for book in books:
        if book['id'] == book_id:
            return book
    raise HTTPException(status_code=404, detail='Книга не найдена')

if __name__ == '__main__':
    uvicorn.run('main:app', reload=True)
