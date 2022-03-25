import webbrowser

for i in range(100):
    webbrowser.open("http://127.0.0.1:8000/news/delete/"+str(i))