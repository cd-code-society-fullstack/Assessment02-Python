def get_contents(string, keyword):
    # Find the first occurrence of keyword
    first_occurrence = string.find(keyword)
    
    # If the keyword is not found
    if first_occurrence == -1:
        return ""

    # Find the second occurrence of keyword
    second_occurrence = string.find(keyword, first_occurrence + len(keyword))

    # If there's only one occurrence
    if second_occurrence == -1:
        return "none"

    # Return the content between the first and second occurrence
    return string[first_occurrence + len(keyword) : second_occurrence]

