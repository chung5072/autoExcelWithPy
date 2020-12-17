"""200206_checkEndpoint_inDescFile"""
"""
cve 코드에 대한 상세설명이 들어간 파일에
정규식으로 값을 불러오기 위해서
규칙이 정확한지 확인하는 코드
맨 끝에 'ㅆ'이 들어가 있어야한다.
"""

"""1. 새로운 메모장에다가 원하는 내용을 작성"""
newMemoFile = open("원하는 텍스트 파일 경로", 'a', encoding="UTF8")


"""2. 어떠한 내용도 들어가 있지 않은 경우"""    
def blankContents(blank_contents):
    newMemoFile.write(blank_contents)

"""3. 알맞게 끝나는 문자가 들어가 있을 경우"""
def containRightEndPoint(right_endPoint):
    newMemoFile.write(right_endPoint)

"""4. 끝나는 문자가 잘못 들어가 있는 경우 > $가 작성된 경우"""
def wrongEndPoint01(wrong_endPoint_01):
    newMemoFile.write(wrong_endPoint_01)

"""5. 끝나는 문자가 잘못 들어가 있는 경우 > 끝나는 문자 자체가 없는 경우"""
def wrongEndPoint02(wrong_endPoint_02):
    newMemoFile.write(wrong_endPoint_02)

"""6. 작성이 끝나고 새 메모장을 닫는 함수"""
"""
처음에는 앞의 메모장처럼 with함수를 이용할 예정이었으나
with를 사용하면 계속 내용을 추가할 수가 없는 문제가 발생하여 
마지막에 한 번에 닫도록 설정
"""
def closeFile():
    newMemoFile.close()
        
