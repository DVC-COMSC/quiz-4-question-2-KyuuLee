
# ******************************
# Make your Code
# ******************************


# Requirement
# No need to use list
# All input values are taken one by one separatively.
###

cnt = 0
while True:
    str = input()
    if (str.lower() == 'stop'):
        break
    if cnt == 0:
        minlen = maxlen = len(str)
        maxstr = minstr = str
    if minlen > len(str):
        minstr = str
        minlen = len(str)
    if maxlen < len(str):
        maxstr = str
        maxlen = len(str)
    cnt += 1

print(maxstr, minstr)
