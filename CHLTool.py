# [================================================================================================]
# IMPORT
# [================================================================================================]


import re


# [================================================================================================]
# VAR && CONST DATA
# [================================================================================================]


FUNC_OP_LINE_MAX = 4
SPLIT_OPTIONS = ',;|\\/'
SPLIT_ARGS = '.:'
SPLIT_DATA = ',|\n\t '
STRIP_QUOTES = '\'\"'

MACRO_VALUE = 'value'
MACRO_TEXT = 'text'
MACROS = {
    'NIL': {MACRO_VALUE: '', MACRO_TEXT: 'Empty'},
    'CM': {MACRO_VALUE: ',', MACRO_TEXT: 'Comma'},
    'BR': {MACRO_VALUE: '|', MACRO_TEXT: 'Bar'},
    'NWL': {MACRO_VALUE: '\n', MACRO_TEXT: 'New Line'},
    'TB': {MACRO_VALUE: '\t', MACRO_TEXT: 'Tab'},
    'SP': {MACRO_VALUE: ' ', MACRO_TEXT: 'Space'},
}


# [================================================================================================]
# FUNCTIONS MACRO
# [================================================================================================]


def GetMacro(macro):
    if macro in MACROS.keys():
        return MACROS[macro][MACRO_VALUE]
    else:
        return macro.strip(STRIP_QUOTES)


def GetMacrosStr():
    macros_str = '{\n'
    for macro in MACROS.keys():
        macros_str += f'\t\'{macro}\':\'{MACROS[macro][MACRO_TEXT]}\'\n'
    macros_str += '}'
    return macros_str


# [================================================================================================]
# FUNCTIONS DATA
# [================================================================================================]


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
    return input_data.strip()


def KeyWordOnly(_data):
    if _data == '':
        print('\'data\' is empty')
        return

    _line_dada = _data.split('\n')
    _ret_data = ''
    for _local_data in _line_dada:
        _local_data = _local_data.strip(SPLIT_DATA)
        _local_str = _local_data.split()[0]
        _ret_data += f'{_local_str}\n'
    _ret_data = _ret_data.strip(SPLIT_DATA)
    return _ret_data.strip()


def KeyWordStyle(_data):
    if _data == '':
        print('\'data\' is empty')
        return

    _line_dada = _data.split('\n')
    _ret_data = ''
    for _local_data in _line_dada:
        _local_data = _local_data.strip(SPLIT_DATA)
        _local_str = _local_data.split()[0]
        _ret_data += f'<keyword>{_local_str}</keyword>\n'
    _ret_data = _ret_data.strip(SPLIT_DATA)
    return _ret_data.strip()


def RemoveDuplicates(_data):
    if _data == '':
        print('\'data\' is empty')
        return
    _list_data = re.split(f'[{SPLIT_DATA}]+', _data)
    if len(_list_data[0]) == len(_data):
        print('\'data\' is only one word')
        return

    _split_mode = _data[len(_list_data[0])]
    _use_list = []
    _ret_data = ''
    for _local_data in _list_data:
        _local_data = _local_data.strip(SPLIT_DATA)
        if not (_local_data in _use_list):
            _use_list.append(_local_data)
            _ret_data += f'{_local_data}{_split_mode}'
    _ret_data = _ret_data.strip(SPLIT_DATA)
    return _ret_data.strip()


def OnlySingles(_data):
    if _data == '':
        print('\'data\' is empty')
        return
    _list_data = re.split(f'[{SPLIT_DATA}]+', _data)
    if len(_list_data[0]) == len(_data):
        print('\'data\' is only one word')
        return

    _split_mode = _data[len(_list_data[0])]
    _single_list = []
    _duplicate_list = []
    for _local_data in _list_data:
        if not (_local_data in _duplicate_list):
            if not (_local_data in _single_list):
                _single_list.append(_local_data)
            else:
                _single_list.remove(_local_data)
                _duplicate_list.append(_local_data)

    _ret_data = ''
    for _local_single in _single_list:
        _ret_data += f'{_local_single}{_split_mode}'
    _ret_data = _ret_data.strip(SPLIT_DATA)
    return _ret_data.strip()


def SortAscending(_data):
    if _data == '':
        print('\'data\' is empty')
        return
    _list_data = re.split(f'[{SPLIT_DATA}]+', _data)
    if len(_list_data[0]) == len(_data):
        print('\'data\' is only one word')
        return

    _split_mode = _data[len(_list_data[0])]
    _list_data.sort()
    _ret_data = ''
    for _local_data in _list_data:
        _local_data = _local_data.strip(SPLIT_DATA)
        _ret_data += f'{_local_data}{_split_mode}'
    _ret_data = _ret_data.strip(SPLIT_DATA)
    return _ret_data.strip()


def SortDescending(_data):
    if _data == '':
        print('\'data\' is empty')
        return
    _list_data = re.split(f'[{SPLIT_DATA}]+', _data)
    if len(_list_data[0]) == len(_data):
        print('\'data\' is only one word')
        return

    _split_mode = _data[len(_list_data[0])]
    _list_data.sort()
    _list_data = _list_data[::-1]
    _ret_data = ''
    for _local_data in _list_data:
        _local_data = _local_data.strip(SPLIT_DATA)
        _ret_data += f'{_local_data}{_split_mode}'
    _ret_data = _ret_data.strip(SPLIT_DATA)
    return _ret_data.strip()


def Arg1ToArg2(_data, A1, A2):
    if _data == '':
        print('\'data\' is empty')
        return

    _arg1 = GetMacro(A1)
    _arg2 = GetMacro(A2)
    _data = _data.replace(_arg1, _arg2).strip(_arg2)
    return _data.strip()


def Upper(_data):
    if _data == '':
        print('\'data\' is empty')
        return

    _data = _data.upper()
    return _data.strip()


def Lower(_data):
    if _data == '':
        print('\'data\' is empty')
        return

    _data = _data.lower()
    return _data.strip()


# [================================================================================================]
# FUNCTIONS START
# [================================================================================================]


def nameof(function):
    if callable(function):
        return function.__name__
    else:
        return None


def getOptionChunk(functionDataList, index):
    functionName = nameof(functionDataList[index]["func"])
    if len(functionDataList) == index + 1 or \
            index % FUNC_OP_LINE_MAX == FUNC_OP_LINE_MAX - 1:
        return f'{functionName}[{index}]'
    else:
        return f'{functionName}[{index}] | '


def getOptionMsg(functionDataList):
    msg = ''
    for i in range(len(functionDataList)):
        if (i % FUNC_OP_LINE_MAX == 0) and (not (i == 0)):
            msg += '\n'
        msg += getOptionChunk(functionDataList, i)
    return msg


# [================================================================================================]
# START
# [================================================================================================]


SCRIPT_NAME = """################################
# Custom-Highlight-Langs Tool
################################"""
SCRIPT_HELP = f"""
### Start CHLTool Help ###

Arg[X]         =>  X Index Argument
Split Options  =>  "{SPLIT_OPTIONS}"
Split Args     =>  "{SPLIT_ARGS}"
Macros         => {GetMacrosStr()}

### End CHLTool Help ###
"""
OPTIONS = '\nOptions: '
INPUT = '\n[DATA]:\n'
RESULT = '[RESULT]:\n'
EXIT = '\npress \'enter\' to exit'
functionDataList = [
    {'func': KeyWordOnly, 'argc': 1},
    {'func': KeyWordStyle, 'argc': 1},
    {'func': RemoveDuplicates, 'argc': 1},
    {'func': OnlySingles, 'argc': 1},
    {'func': SortAscending, 'argc': 1},
    {'func': SortDescending, 'argc': 1},
    {'func': Upper, 'argc': 1},
    {'func': Lower, 'argc': 1},
    {'func': Arg1ToArg2, 'argc': 3},
]


print(SCRIPT_NAME)
print(SCRIPT_HELP)
print(getOptionMsg(functionDataList))
opts = input(OPTIONS)
data = GetInputs(INPUT)


optsList = re.split(f'[{SPLIT_OPTIONS}]+', opts)
for opList in optsList:
    opData = re.split(f'[{SPLIT_ARGS}]+', opList)
    opInt = int(opData[0])
    if opInt < len(functionDataList) and opInt >= 0:
        if not (functionDataList[opInt]['argc'] == len(opData)):
            print("ERROR: Args Incorrect")
            exit(-1)
        match (functionDataList[opInt]['argc']):
            case 1:
                data = functionDataList[opInt]["func"](data)
            case 2:
                data = functionDataList[opInt]["func"](data, opData[1])
            case 3:
                data = functionDataList[opInt]["func"](
                    data, opData[1], opData[2])
            case 4:
                data = functionDataList[opInt]["func"](
                    data, opData[1], opData[2], opData[3])
    else:
        print('erro! :(\n')


print(RESULT + data)
input(EXIT)
