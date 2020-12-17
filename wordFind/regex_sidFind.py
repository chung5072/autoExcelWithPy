def sid(line_list, line_matchRegex):
    regexFind_sidFind = line_matchRegex.search(line_list)
    # print(regexFind_msgFind)
    regexResult_sidFind = regexFind_sidFind.group()
    # print(regexResult_msgFind)
    return regexResult_sidFind