content = """wow
this 
is multiline"""

print(content)

#use repr to 'see' the carriage returns
print(repr(content))

#You can use repr to convert the heredoc/multiline string into a single line
content = repr(content)
print(content)