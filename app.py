from flask import Flask, render_template
import json

app = Flask(__name__)

# Загрузка Библии
with open("bible/bible.json", "r", encoding="utf-8") as f:
    bible = json.load(f)
books = bible["Books"]

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/bible")
def bible_books():
    return render_template("bible_books.html", books=books)

@app.route("/bible/<int:book_id>")
def bible_chapters(book_id):
    book = next((b for b in books if b["BookId"] == book_id), None)
    if not book:
        return "Книга не найдена", 404
    return render_template("bible_chapters.html", book=book)

@app.route("/bible/<int:book_id>/<int:chapter_id>")
def bible_chapter(book_id, chapter_id):
    book = next((b for b in books if b["BookId"] == book_id), None)
    if not book:
        return "Книга не найдена", 404
    chapter = next((c for c in book["Chapters"] if c["ChapterId"] == chapter_id), None)
    if not chapter:
        return "Глава не найдена", 404
    return render_template("bible_chapter.html", book=book, chapter=chapter)

if __name__ == "__main__":
    app.run(debug=True)
