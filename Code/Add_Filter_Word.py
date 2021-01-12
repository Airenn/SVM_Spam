#################### 필터링 단어 추가 함수 ####################
import csv 

lines = [] 

 # Filter_Word.csv 읽기 모드로 열음 
i = open('Filter_Word.csv', 'w', encoding='utf-8-sig',  newline='')
Filter_Word = csv.writer(i) 
Word = '' # 필터링 추가 단어 변수

#for x in Filter_Word: 
#     lines.append(x[0]) # 한 글자씩 새로운 배열에 저장

 # Filter_Word.csv 추가 모드로 열음 
i = open('Filter_Word.csv', 'a', encoding='utf-8-sig',  newline='')
Filter_Word = csv.writer(i) 

# 필터링 단어가 종료일 때 까지 반복
while(Word != '종료'): 
 Word= str(input('text : ')) # 필터링 단어 입력
 
 if (Word in lines):
      continue

 if(Word == '종료'): # 필터링 단어가 종료이면
     break # While문 빠져나감 


 Filter_Word.writerow([Word]) # CSV에 필터링 단어 한 행씩 추가
 lines.append(Word) # 한 글자씩 새로운 배열에 저장

i.close() # 파일 닫음
