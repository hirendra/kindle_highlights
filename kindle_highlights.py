#!/usr/local/bin/python3
# A script to parse kindle higlights into markdown
# files for my personal github repo. Because other
# software was making me pay for it.
# Use it, and abuse it.
# https://duarteocarmo.com/blog/managing-kindle-highlights-with-python-and-github.html
import re
import pathlib


class Book:
    book_list = set()

    def __init__(self, title, author):
        self.author = author
        self.title = title
        self.highlights = []
        Book.book_list.add(self.title)

    def add_highlight(self, loc,highlight):
        if highlight:
            self.highlights.append((loc,highlight))

    def __str__(self):
        return f"<Book Object>Title:{self.title}\tAuthor:{self.author}\tHighlights:{len(self.highlights)}"

    def write_book(self, format="markdown"):
        if self.title == None or len(self.highlights) == 0:
            print(f"Not writting because name is None.")
            return False
        clean_title = "".join(
            [c for c in self.title if c.isalpha() or c.isdigit() or c == " "]
        ).rstrip()
        with open(f"books/{clean_title}.md", "w+") as file:
            file.write(f"# {clean_title}")
            file.write("\n")
            for t in self.highlights:
                h = t[1]
                loc = t[0]
                clean_text = h.replace("\n", " ")
                file.write(f"#### {loc}\n- {clean_text}")
                file.write("\n")

            file.close()


class Highlight:
    total_highlights = 0

    def __init__(self, raw_string):
        (self.title, self.author, self.loc,self.content,) =\
            Highlight.parse_single_highlight(
            raw_string
            )

    def __str__(self):
        return f"<Highlight Object> Title:{self.title}\t\
            Author:{self.author}\tLoc:{self.loc}\t\
            Content:{self.content}"

    @staticmethod
    def parse_single_highlight(highlight_string):
        splitted_string = highlight_string.split("\n")
        print(splitted_string)
        if len(splitted_string) > 2:
            author_line = splitted_string[1]
            loc = splitted_string[2]
            loc = re.sub(r"- Your Highlight","Highlight",loc)
            content = splitted_string[-2]
    #        content = "\n".join(splitted_string[2:])
            regex = r"\((.*?)\)"
            match = re.search("\((.*)\)", author_line)

            if match:
                author = match.group(1)
                title = author_line[: match.start()]
                return title, author, loc, content

        return None, None, None,None


current_directory = pathlib.Path.cwd()
parsed_books = list(set(file.stem for file in current_directory.glob("**/*.md")))
highlight_separator = "=========="
highlight_json = dict()
library = []


with open("My Clippings.txt", "r") as file:
    data = file.read()

highlights = data.split(highlight_separator)

for raw_string in highlights:
    h = Highlight(raw_string)
    if h.title not in Book.book_list:
        b = Book(h.title, h.author)
        b.add_highlight(h.loc,h.content)
        library.append(b)
    else:
        for b in library:
            if b.title == h.title:
                b.add_highlight(h.loc,h.content)

for book in library:
    if book.title:
        print(book.title)
        if book.title.strip() not in parsed_books:
            book.write_book(format="markdown")
        else:
            print(f"{book.title} is already written.")
