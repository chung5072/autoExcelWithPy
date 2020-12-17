def metadata(line_list, line_matchRegex):
    regexFind_metadataFind = line_matchRegex.search(line_list)
    # print(regexFind_msgFind)
    regexResult_metadataFind = regexFind_metadataFind.group()
    # print(regexResult_msgFind)
    return regexResult_metadataFind