def classtype(line_list, line_matchRegex):
    regexFind_classtypeFind = line_matchRegex.search(line_list)
    # print(regexFind_msgFind)
    regexResult_classtypeFind = regexFind_classtypeFind.group()
    # print(regexResult_msgFind)
    return regexResult_classtypeFind