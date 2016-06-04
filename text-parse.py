# Enter your code here. Read input from STDIN. Print output to STDOUT
import sys

paragraph = raw_input('')
sentences = []
tempsen = ''
quote_dub = quote_sing = False

def check_suffix(array):
    total = len(array) - 1
    suffix_two = array[total-1] + array[total]
    suffix_three = array[total-2] + array[total-1] + array[total]
    if array[total-1] == ' ':
        return False
    if (suffix_two == 'Dr') or (suffix_two == 'Mr') or (suffix_two == 'Sr'):
        return False
    if suffix_three == 'Mrs':
        return False
    return True

for c in paragraph:
    if (c == '\"') and quote_dub == False:
        quote_dub = True
    elif c == '\"':
        quote_dub = False
        
    if (c == "\'") and quote_sing == False:
        num_sing = len(tempsen)
        if tempsen[num_sing-1] == ' ':
            quote_sing = True
    elif c == "\'":
        quote_sing = False
    
    if c == '.' or c == '?' or c == '!':
        if (quote_dub == False) and (quote_sing == False) and check_suffix(tempsen):
            tempsen = tempsen + c
            sentences.append(tempsen)
            tempsen = ''
        else:
            tempsen = tempsen + c
    else:
        tempsen = tempsen + c
for i in sentences:
    i = i.strip()
    print i
