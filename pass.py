import aspose.words as aw

# load document
doc = aw.Document("backend.py")

# create document options
options = aw.saving.OoxmlSaveOptions(aw.SaveFormat.DOCX)

# set password
options.password = "password"

# save updated document
doc.save("BACKEND-SCRIPT.DOCX", options)