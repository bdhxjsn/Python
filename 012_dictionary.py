marks = {
    "lol" : 100,
    "null": 99,
    "lol_null": 199,
    69: "it applicable"
}

# print(marks, type(marks))
# print(marks[69])#for accessing the [dict] key's value

print(marks.items())#list dict_items in "TUPLE"
print(marks.keys())#list LHS from dict {keys}
print(marks.values())#list RHS from dict {values}
marks.update({"lol": 101, "YO": "what up biatch"})#update bcz {dict} is {Muttable}
#and can add new key/value pair too
print(marks)
print(marks.get("lol2"))#It gives {None} bcz of paranthesis threr is no "lol2"
# print(marks["lol2"])#It gives error bcz it's in  squred bracket. there no "lol2"
print(len(marks))