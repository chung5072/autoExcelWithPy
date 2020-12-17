def referenceDoc(line_list, line_matchRegex):
    regexFind_referenceDocFind = line_matchRegex.search(line_list)
    # print(regexFind_msgFind)
    regexResult_referenceDocFind = regexFind_referenceDocFind.group()
    # print(regexResult_msgFind)
    return regexResult_referenceDocFind