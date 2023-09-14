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


SCRIPT_NAME = 'Custom-Pattern Tools'
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
