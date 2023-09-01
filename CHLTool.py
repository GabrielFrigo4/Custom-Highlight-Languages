def GetInputs(msg):
    input_data = input(msg)
    if input_data == '':
        return input_data
    while True:
        user_input = input()

        if user_input == '':
            break
        else:
            input_data += f'\n{user_input}'
    return input_data


def KeyWordOnly(_data):
    if _data == '':
        print('\'data\' is empty')
        return
    _line_dada = _data.split('\n')
    _ret_data = ''
    for _local_data in _line_dada:
        _loc_str = _local_data.split()[0]
        _ret_data += f'{_loc_str}\n'
    return _ret_data


def KeyWordStyle(_data):
    if _data == '':
        print('\'data\' is empty')
        return
    _line_dada = _data.split('\n')
    _ret_data = ''
    for _local_data in _line_dada:
        _loc_str = _local_data.split()[0]
        _ret_data += f'<keyword>{_loc_str}</keyword>\n'
    return _ret_data


def Upper(_data):
    if _data == '':
        print('\'data\' is empty')
        return
    _data = _data.upper()
    return _data


def Lower(_data):
    if _data == '':
        print('\'data\' is empty')
        return
    _data = _data.lower()
    return _data


def SpaceToLine(_data):
    if _data == '':
        print('\'data\' is empty')
        return
    _data = _data.replace(" ", "\n")
    return _data


def LineToSpace(_data):
    if _data == '':
        print('\'data\' is empty')
        return
    _data = _data.replace("\n", " ")
    return _data


def SpaceToBar(_data):
    if _data == '':
        print('\'data\' is empty')
        return
    _data = _data.replace(" ", "|")
    return _data


def BarToSpace(_data):
    if _data == '':
        print('\'data\' is empty')
        return
    _data = _data.replace("|", " ")
    return _data


print('Custom-Highlight-Langs Tools')
print('keywordOnly[0] | keywordStyle[1] | uppercase[2] | lowercase[3] | spaceToLine[4] | lineToSpace[5] | spaceToBar[6] | barToSpace[7]')
ops = input('Options: ')
data = GetInputs('\n[DATA]:\n')

for op in ops.split(','):
    if op == '0':
        data = KeyWordOnly(data)
    elif op == '1':
        data = KeyWordStyle(data)
    elif op == '2':
        data = Upper(data)
    elif op == '3':
        data = Lower(data)
    elif op == '4':
        data = SpaceToLine(data)
    elif op == '5':
        data = LineToSpace(data)
    elif op == '6':
        data = SpaceToBar(data)
    elif op == '7':
        data = BarToSpace(data)
    else:
        print('erro! :(\n')

print('[RESULT]:\n'+data)
input('press \'enter\' to exit')
