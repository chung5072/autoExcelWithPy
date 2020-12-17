"""200129_inputRisk_inSuricataRule"""
"""
특정 내용을 추출하길 원하는 엑셀파일의 classtype 값을 가져와서 
해당 classtype에 매칭되는 risk의 수치를 가져와서
1이면 높음, 2면 중간, 3이면 낮음을 엑셀 파일에 저장한다.
"""

"""1. 필요 모듈을 호출"""
# 정규식을 제어하기 위한 모듈을 호출
import re

"""2. 리스크 값을 반환하기 위한 함수 선언"""
"""
해당 리스크를 반환하기 위해서는 classtype의 내용을 가져와야 함
"""
def memoForRisk(classification):
    # 리스크를 반환하려면 해당 결과값을 글로벌 변수로 선언을 해야 했음
    global riskGrade_text

    """2-1. classtype의 값을 가져옴 > ' '이 들어가 있어서 해당 내용을 전부 없엠"""
    result_classification = classification.replace(' ', '')
    print(result_classification)

    """2-2. 리스크에 대한 내용"""
    """
    리스크에 대한 내용이 숫자로 되어있고 해당 숫자에 따라서
    높음, 중간, 낮음을 설정하기 때문에 
    정규식으로 숫자를 긁어와야 함.
    """
    # 메모장의 리스크 값을 가져오기 위한 정규식
    findNum_classification = re.compile(r'\d')
    # 엑셀파일의 classtype과 비교하기 위한 정규식
    findClassification_classification = re.compile(r': (.*?),')

    """2-3. 메모장 관련"""
    # 메모장 파일을 불러옴
    memoFile = open("원하는 텍스트 파일 경로")
    # 메모장의 전체 내용을 한 리스트에 넣음
    memoFile_linesList = memoFile.readlines()
    # 메모장의 리스트의 길이를 구하여 메모장의 전체 줄 수를 구함
    memoFile_totalCount = len(memoFile_linesList)
    # 메모장의 전체 내용을 줄을 엑셀 파일의 classtype과 비교하기 위해서 반복문을 활용, 해당 조건을 위한 변수
    memoFile_linesCount = 0
    
    """2-4. 반복문 실행"""
    while memoFile_linesCount < memoFile_totalCount:
        print(f"{memoFile_linesCount+1}번째 줄 \n{memoFile_linesList[memoFile_linesCount]}")

        """2-5. 메모장에 classtype에 대한 내용이 먼저 있는지 확인"""
        """
        먼저 확인을 하고 값이 있을 경우에만 정규식을 활용하여 값을 발라냄
        값이 없는 상태에서 정규식을 이용하면 AttributeError를 발생시킴
        """
        findClassification_word = memoFile_linesList[memoFile_linesCount].find(result_classification)
        print(findClassification_word)

        if findClassification_word > -1:
            """2-6. 메모장에서 정규식을 활용하여 classtype에 대한 내용을 추출"""
            foundClassification = findClassification_classification.search(memoFile_linesList[memoFile_linesCount])
            g_classification = foundClassification.group()

            hihi = g_classification.replace(': ', '').replace(',', '')
            print(hihi)
            """2-7. 메모장의 classtype과 엑셀파일의 classtype이 같다면"""
            if hihi == result_classification:
                
                """2-8. 엑셀파일의 risk값을 가져옴 > 해당 리스크의 값은 먼저 숫자"""
                riskGrade_num = findNum_classification.search(memoFile_linesList[memoFile_linesCount])

                """2-9. 해당 숫자에 따라서 반환되는 값이 다름"""
                if riskGrade_num == '1':
                    riskGrade_text = 'High'
                elif riskGrade_num == '2':
                    riskGrade_text = 'Medium'
                elif riskGrade_num == '3':
                    riskGrade_text = 'Low'
                elif riskGrade_num == '4':
                    riskGrade_text = 'Low_4'
                else:
                    print('You need check other number')

        memoFile_linesCount = memoFile_linesCount + 1
        findClassification_word = None

    """2-10. 결과값으로 나온 리스트의 등급을 반환"""
    return riskGrade_text


        
