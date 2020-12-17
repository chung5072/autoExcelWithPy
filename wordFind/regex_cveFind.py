def cve(line_list, line_matchRegex):
    regexFind_cveFind = line_matchRegex.search(line_list)
    # print(regexFind_msgFind)
    regexResult_cveFind = regexFind_cveFind.group()
    # print(regexResult_msgFind)
    return regexResult_cveFind