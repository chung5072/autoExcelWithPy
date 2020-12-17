"""20200205_inputDetailDesc_inSuricataExcelFile"""
"""
엑셀파일에 상세설명을 작성하기 위한 코드
엑셀파일의 cve 코드에 대한 내용을 검색한 후 메모장에 작성
엑셀파일의 cve 코드와 메모장의 cve 코드 값을 비교한 후 같은 cve 코드 값일 경우
해당 cve의 설명을 엑셀파일의 상세 설명란에 작성
"""

"""1. 딕셔너리에 저장된 내용을 메모장에 저장함"""
def inputDifferentCVE(dictCVE):
    """메모장 > 내용 작성 > 종료"""
    """2-1. 메모장을 열어서 해당 내용을 넣고 종료까지 한 번에"""
    with open('원하는 텍스트 파일 경로', 'w', encoding='UTF8') as memo_diff_cveFile:

        memo_diff_cveFile.write(str(dictCVE))

