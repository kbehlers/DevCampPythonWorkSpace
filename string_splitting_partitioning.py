


heading = "Python: An Introduction: A subheading"

return_tuple = heading.partition(": ")
print(return_tuple[0])

#if desired, the tuple can be deconstructed into 3 variables on assignment
beginning, delimiter, ending = heading.partition(": ")
print(beginning)

#SPLITTING is much more powerful
tags = "python, coding, programming, development"
tags_list = tags.split(",")
for tag in tags_list:
    #use strip to remove the whitespace that got included
    print(tag.strip())
