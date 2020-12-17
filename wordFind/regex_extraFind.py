def extra(line_list, line_matchRegex):
    regexFind_extraFind = line_matchRegex.search(line_list)
    # print(regexFind_msgFind)
    regexResult_extraFind = regexFind_extraFind.group()
    # print(regexResult_msgFind)
    return regexResult_extraFind