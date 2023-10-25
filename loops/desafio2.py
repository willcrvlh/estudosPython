def corresponding_parenthesis(text: str):
    left = text.count("(")
    rigth = text.count(")")
    diference = left- rigth

    if diference>0:
        return "(" * diference
    elif diference < 0:
        return ")" * (diference -1)
    
    return ""

def remove_more_than_two_repetitions(text: str):
    response = []
    response.append(text[0])
    response.append(text[1])

    for index, character in enumerate(text[2:],2):
        if text[index - 1] != character or text[index - 2] != character:
            response.append(character)

    return "".join(response)