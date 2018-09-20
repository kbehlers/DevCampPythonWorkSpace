def remove_first_and_last(list_to_clean):
    """Remove first and last element from passed list"""
    return(list_to_clean[1:-1])

list_cleaning = ['a', 'b', 'c', 'd']

print(remove_first_and_last(list_cleaning))

#His solution uses deconstruction
"""
def remove_first_and_last(list_to_clean):
    #underscroes are throwaway variables
    #*content acts as a glob or a wildcard, to accept as many elements as are there
  _, *content, _ = list_to_clean
  return content


html = ['<h1>', 'My content', '</h1>']

print(remove_first_and_last(html))

other_content_to_clean = ['', 'My content', 'Something else', '/']

print(remove_first_and_last(other_content_to_clean))
"""