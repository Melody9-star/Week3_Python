#리스트 (내장함수)
li = [3,1,'배가',4,'고파요',5,1]

#인덱싱 슬라이싱
print(li[0:3])

#리스트 원소 오름차순 정렬해주는 함수 : 변수.sort()
li.sort()
print(li.sort())

#리스트 내의 특정 원소 인덱스 반환해주는 함수 : .index()
print(li.index("배가"))

#리스트 내의 특정 원소의 갯수 세기 : .count(요소)
print(li.count(1))
