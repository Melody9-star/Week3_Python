#딕셔너리 (내장함수)
pairs={'노':'현승', '한':'현정', '멋':'쟁이'}

#하나의 키-value 쌍을 추가하는 방법
pairs['붕']='어빵'
print(pairs)

#특정 키-Value 삭제하는 방법 : del 함수
#del 변수[키]
del pairs['한']
print(pairs)

#key로 value 얻기 : 변수.get(키)
v=pairs.get('멋')
print(v)
