This is based on the kindle highlights python script found here 
[my-personal-zen/highlight_parser.py at master ·
duarteocarmo/my-personal-zen](https://github.com/duarteocarmo/my-personal-zen/blob/master/highlight_parser.py)
# 
I adapted it to generate markdown. Duarte's script generates txt files and I
wanted markdown. 

You can use this script exactly like Duarte's script. He has written a blog
about it.
 https://duarteocarmo.com/blog/managing-kindle-highlights-with-python-and-github.html
 

I  wanted to generate markdown files that I could index from DEVONthink, so I made the changes to Duarte’s script. 

Here it is - 

https://github.com/hirendra/kindle_highlights

My script generates markdown files in a folder that is indexed by DEVONthink.
This only works with connecting the kindle to the Mac. It looks for the My
Clippings.txt in the current directory. I have a symbolic link to
/Volumes/Kindle/documents/My Clippings.txt in my books read folder. 

```
11685 Hirendras-MacBook-Pro[01/13/21]:~/personal/booksread
-->ls -l
drwxr-xr-x     - hiren 23 Dec  2020 books
.rwxr-xr-x@ 3.4k hiren 21 Dec  2020 kindle_highlights.py
lrwxr-xr-x    42 hiren 14 Oct  2020 My Clippings.txt -> /Volumes/Kindle/documents/My Clippings.txt
```

When you run kindle_highlights.py, it generates the markdown files in the books folder. 
