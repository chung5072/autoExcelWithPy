"""200206_checkEndpoint_inDescFile"""
"""
cve 코드에 대한 상세설명이 들어간 파일에
정규식으로 값을 불러오기 위해서
규칙이 정확한지 확인하는 코드
맨 끝에 'ㅆ'이 들어가 있어야한다.
"""

"""1. 필요한 모듈 호출"""
# 메모장을 그대로 덮어쓰는 방법을 찾지 못하여 새로 메모장을 작성하는 방향으로 진행
from rule_readMemo.inputEndPoint.testNewFile import *

"""2. 메모장의 내용을 작성하기 위해서 메모장을 불러옴"""
"""
close()를 사용하지 않고 자동으로 메모장을 닫기 위해서 with를 이용함
그리고 인코딩에 관해서 문제가 있어서 encoding 항목을 추가
"""
with open("원하는 텍스트 파일 경로", 'r', encoding="UTF8") as memoFIle:

    """3. 메모장 항목 관련"""
    # 메모장의 전체 내용을 한 리스트에 저장
    memoList = memoFIle.readlines()
    # 해당 리스트의 길이를 구하여 해당 메모장의 줄 수를 파악
    totalCount = len(memoList)
    # 반복문을 이용하여 해당 내용을 확인, 조건을 위해 필요한 변수 선언
    memo_count = 0

    """4. 메모장에 규칙을 위해 필요한 문자와 잘못 작성된 문자열"""
    # cve 코드 부분을 자르기 위해 필요한 문자
    word_seperate = 'ㅃ'
    # 상세 설명의 마지막 부분을 나타내기 위한 문자
    word_endPoint = 'ㅆ'
    # 초기에 잘못 작성된 마지막 부분 문자
    word_endPoint_wrong = '$'

    """5. 반복문 실행"""
    while memo_count < totalCount:
        """5-1. cve 코드를 자르는 부분 파악"""
        """
        cve코드가 없으면 해당 문자열에는 상세 설명에 대한 내용을 넣지 않았으므로
        조건을 실행하지 않도록 설정
        """
        sentenceSeperate = memoList[memo_count].find(word_seperate)

        if sentenceSeperate > -1:
            print(f'{memo_count}행에는 구분자는 있음')
            
            """5-2. 구분자가 있을 경우"""
            """
            구분자가 있더라도 마지막에 끝나는 부분에 어떠한 문자도 넣지 않았거나
            $를 잘못 넣었을 경우가 있기 때문에
            해당 조건마다 다른 행동을 실행
            """
            sentenceEndPoint = memoList[memo_count].find(word_endPoint)        
            if sentenceEndPoint > -1:
                print('끝에 ㅆ이 잘 들어가 있음')
                containRightEndPoint(memoList[memo_count])
            else:
                print('끝에 ㅆ이 들어가 있지 않음')
                sentenceWrongEnd = memoList[memo_count].find(word_endPoint_wrong)
                    
                if sentenceWrongEnd > -1:
                    print('끝에 $가 들어가 있음')
                    
                    replaceLines1 = memoList[memo_count].replace('$\n', 'ㅆ\n')

                    wrongEndPoint01(replaceLines1)
                else:
                    print('끝에 끝나는 말이 없음')

                    replaceLines2 = memoList[memo_count].replace('\n', 'ㅆ\n')

                    wrongEndPoint02(replaceLines2)
                   
        else:
            print(f'{memo_count}행 에는 구분자도 없음')
            blankContents(memoList[memo_count])
            

        memo_count = memo_count + 1

    closeFile()

    
                
