text = "This string is written in this file using with statement ::"
with open("035_with_statement_file_.txt", "w") as file:
    file.write(text)

#To wipe out the content of any file use this method ::
# with open("035_with_statement_file_.txt", "w") as file:
#     file.write("")