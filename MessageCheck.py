'''
    illegalWords(String msg)
    prepMsg(String msg)
'''
def illegalWords(msg):
    ''' illegalWords(String msg)
        Authors: Kevin Gonzalez
        Version: 1.0
        Date: 12/02/2018
        Args:   msg: Message to be parsed for illegal words

        return: boolean illegalMsg
            True if illegal word is detected.
        Notes:
            illegalWords.txt must be in the same directory as this file.
            This file contains illegal words
    '''

    illegalWords = open("illegalWords.txt", "r")
    illegalMsg = False
    i = 0

    for word in illegalWords:
        for char in range(0, len(msg)):
            if (msg[char] == word[i]):
                if (i == len(word) - 2): #Minus 2 for indexing and exclude '\n'
                    illegalMsg = True
                    return illegalMsg
                else:
                    i = i + 1
            else:
                i = 0
                
    illegalWords.close()
    return illegalMsg

def prepMsg(msg):
    ''' prepMsg(String msg)
        Authors: Kevin Gonzalez
        Version: 1.0
        Date: 12/02/2018
        Args:   msg: Message to be parsed for illegal words

        return: String msg
            Capitalized string with a message seperator if one is not found
        Notes:
            illegalWords.txt must be in the same directory as this file.
            This file contains illegal words
    '''

    if (msg[0] != ' ' or msg[len(msg) - 1] != ' '):
        msg = msg.upper() + ' '

    return msg

