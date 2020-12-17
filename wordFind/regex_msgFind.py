def msg(line_list, line_matchRegex):
    regexFind_msgFind = line_matchRegex.search(line_list)
    # print(regexFind_msgFind)
    regexResult_msgFind = regexFind_msgFind.group()
    # print(regexResult_msgFind)
    return regexResult_msgFind