from fastapi import FastAPI
from routes.user import user_router
from routes.course import course_router
from routes.enrollment import enrollment_router

app = FastAPI(
    title='Edutrack Lite API',
    description='App to enroll for your preferred tech courses'
)

app.include_router(user_router, prefix="/users", tags=["Users"])
app.include_router(course_router, prefix="/courses", tags=["Courses"])
app.include_router(enrollment_router, prefix="/enrollments", tags=["Enrollments"])


@app.get("/")
def home():
    return {"message": "Hello from the Educaion App API"}


# books = {}

# book_data = {
#     "id": 1,
#     "title": "Harry Porter",
#     "author": "James",
#     "year": 2023,
#     "pages": 50,
#     "language": "English"

# } 

# books[book_data["id"]] = book_data


# @app.get('/books') #nouns for naming
# def get_books():
#     return books

# @app.post('/books')
# def create_books(title, author, year, pages, language):  
#     book_id = len(books) + 1  
#     book = {
#         "id": book_id,
#         "title": title,
#         "author": author,
#         "year": int(year),
#         "pages": int(pages),
#         "language": language
  
#     }
#     books[book_id] = book
#     return books #Is like we return what was created.#you can see nature of data on Swagger

# @app.get('/books/{book_id}')
# def get_book_by_id(book_id):  
#     if int(book_id) not in books:
#         return {"message": "book not found"}
#     return {"message": "Success", "data": books[int(book_id) ]}
# # 



# 
# @app.get("/post_home")
# def post_home():
#     return {"Message": "Hello Server"}