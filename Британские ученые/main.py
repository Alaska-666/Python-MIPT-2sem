import re
import random
import string


def prepare_to_british_scientists(text, letters_to_shuffle_nm):
    x = ''
    key = letters_to_shuffle_nm
    result = re.findall(r"[\w']"
                        r"+|[\s,./?<>}\]{[!@'#№$;%^&:*()\"+=_\-\\|`~1234567890]", text)
    for i in range(len(result)):
        if ((i != len(result) - 1) or (result[i] != '\n')) and re.match(r"[\w]", result[i]):
            if len(result[i]) - 2 >= key:
                res = list(str(result[i][1:key + 1]))
                random.shuffle(res)
                res = res + list(str(result[i][key + 1:len(result[i]) - 1]))
            else:
                res = list(str(result[i][1:len(result[i]) - 1]))
                random.shuffle(res)
            ans = str(result[i][0] + ''.join(res))
            if len(result[i]) != 1:
                x = x + ans + result[i][-1]
            else:
                x = x + ans
        elif (i == len(result) - 1) and (result[i] == '\n'):
            continue
        else:
            x = x + result[i]
    if (x == text) and (key > 1):
        x = ''
        for i in range(len(result)):
            if ((i != len(result) - 1) or (result[i] != '\n')) and re.match(r"[\w]", result[i]):
                if ((len(result[i]) != 4) or (key <= 1)) and  len(result[i]) - 2 < key:
                    res = list(str(result[i][1:len(result[i]) - 1]))
                    random.shuffle(res)
                elif (len(result[i]) == 4) and (key > 1):
                    res = list(str(result[i][1:len(result[i]) - 1]))
                    res.reverse()
                else:
                    res = list(str(result[i][1:key + 1]))
                    random.shuffle(res)
                    res = res + list(str(result[i][key + 1:len(result[i]) - 1]))
                ans = str(result[i][0] + ''.join(res))
                if len(result[i]) != 1:
                    x = x + ans + result[i][-1]
                else:
                    x = x + ans
            elif (i == len(result) - 1) and (result[i] == '\n'):
                continue
            else:
                x = x + result[i]
    return x
    
