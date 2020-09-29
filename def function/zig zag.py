import time, sys
indent = 0
indentIncreasing = True


while True:
    print(' ' * indent, end='')
    print('********')
    time.sleep(0.1)

    if indentIncreasing:
        indent = indent + 1
        if indent == 20:
            indentIncreasing = False

    else:
        indent = indent - 1
        if indent == 0:
            indentIncreasing = True

