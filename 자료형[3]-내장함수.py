#문자열(내장함수)

#덧셈

str = "멋쟁이 사자처럼"
str2 = "은 좋은 동아리입니다"

print(str[0:4]) #슬라이싱

#문자열의 길이 : len(문자열 변수)

print(len(str))

#문자열 내에서 특정 문자의 등장 횟수 : 문자열 변수 .count('특정문자)
print(str.count('사'))

#문자열을 (측정 기준으로) 나누기 : 문자령 변수.split()
print(str.split()) #공백을 기준으로 나누겠다

#특정 문자 인덱스 찾기 : find('문자'), index('문자')
print(str.find('사'))