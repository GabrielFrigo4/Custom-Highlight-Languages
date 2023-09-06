#[================================================================================================]
# FUNCTIONS DATA
#[================================================================================================]


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
    _data = _data.upper().strip()
    return _data


def Lower(_data):
    if _data == '':
        print('\'data\' is empty')
        return
    _data = _data.lower().strip()
    return _data


def SpaceToLine(_data):
    if _data == '':
        print('\'data\' is empty')
        return
    _data = _data.replace(" ", "\n").strip("\n")
    return _data


def LineToSpace(_data):
    if _data == '':
        print('\'data\' is empty')
        return
    _data = _data.replace("\n", " ").strip(" ")
    return _data


def SpaceToBar(_data):
    if _data == '':
        print('\'data\' is empty')
        return
    _data = _data.replace(" ", "|").strip("|")
    return _data


def BarToSpace(_data):
    if _data == '':
        print('\'data\' is empty')
        return
    _data = _data.replace("|", " ").strip(" ")
    return _data


def SpaceToComma(_data):
    if _data == '':
        print('\'data\' is empty')
        return
    _data = _data.replace(" ", ",").strip(",")
    return _data


def CommaToSpace(_data):
    if _data == '':
        print('\'data\' is empty')
        return
    _data = _data.replace(",", " ").strip(" ")
    return _data


#[================================================================================================]
# FUNCTIONS START
#[================================================================================================]


def nameof(function):
    if callable(function):
        return function.__name__
    else:
        return None


def getOptionChunk(functionDataList, index):
    functionName = nameof(functionDataList[index])
    if len(functionDataList) == index + 1:
        return f'{functionName}[{index}]'
    else:
        return f'{functionName}[{index}] | '


def getOptionMsg(functionDataList):
    msg = ''
    for i in range(len(functionDataList)):
        msg = msg +  getOptionChunk(functionDataList, i)
    return msg


#[================================================================================================]
# START
#[================================================================================================]


SCRIPT_NAME = 'Custom-Highlight-Langs Tools'
OPTIONS = 'Options: '
INPUT = '\n[DATA]:\n'
RESULT = '[RESULT]:\n'
EXIT = 'press \'enter\' to exit'
functionDataList = [
    KeyWordOnly,
    KeyWordStyle,
    Upper,
    Lower,
    SpaceToLine,
    LineToSpace,
    SpaceToBar,
    BarToSpace,
    SpaceToComma,
    CommaToSpace
]


print(SCRIPT_NAME)
print(getOptionMsg(functionDataList))
opts = input(OPTIONS)
data = GetInputs(INPUT)


for op in opts.split(','):
    opInt = int(op)
    if opInt < len(functionDataList) and opInt >= 0:
        data = functionDataList[opInt](data)
    else:
        print('erro! :(\n')


print(RESULT + data)
input(EXIT)
