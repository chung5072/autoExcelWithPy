def reference(line_list, line_matchRegex):
    regexFind_referenceFind = line_matchRegex.search(line_list)
    # print(regexFind_msgFind)
    regexResult_referenceFind = regexFind_referenceFind.group()
    # print(regexResult_msgFind)
    return regexResult_referenceFind