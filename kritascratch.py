print ("Hello World")

app = Krita.instance() # get the application
documentsOpen = app.documents() # get the open documents
documentCount = len( app.documents() ) # get how many documents opened
print(documentCount)
