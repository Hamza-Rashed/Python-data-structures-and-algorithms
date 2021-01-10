from data_structures_and_algorithms.data_structures.linked_list.linked_list import LinkedList

def repeated(string):

    df = LinkedList()
    text = ''
    for i in range(len(string)):
        if df.includes(text):
            return text
        elif string[i] == ',' or string[i] == ' ' or string[i] == '-' or string[i] == '.' :
            if text != '': 
                df.insert(text)
                text = ''
            continue
        else:
            text += string[i].lower()
    return 'no repeated'
