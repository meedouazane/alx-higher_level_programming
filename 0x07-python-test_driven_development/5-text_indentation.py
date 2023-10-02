def text_indentation(text):
    '''  prints a text with 2 new lines after each of these characters:
    ., ? and :
    text must be a string
    There should be no space at the beginning
    or at the end of each printed line
    '''
    if not isinstance(text, str):
        raise TypeError("text must be a string")
    if not text:
        return
    new_text = ""
    for i in range(len(text)):
        if (text[i] == '.' or text[i] == '?' or text[i] == ':'):
            new_text += text[i] + '\n'
            new_text += '\n'
            if (len(text) == i):
                new_text += '\n'
        else:
            new_text += text[i]

    lines = new_text.splitlines()
    result_text = '\n'.join([line.lstrip() for line in lines])
    print(result_text)
