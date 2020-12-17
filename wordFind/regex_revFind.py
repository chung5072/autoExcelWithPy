def rev(line_list, line_matchRegex):
    regexFind_revFind = line_matchRegex.search(line_list)
    # print(regexFind_msgFind)
    regexResult_revFind = regexFind_revFind.group()
    # print(regexResult_msgFind)
    return regexResult_revFind