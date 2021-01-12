#################### 필터링 단어 삭제 함수 ####################\
import csv 

lines = [] 
Word_Delete = '' # 필터링 삭제 단어 변수

# Filter_Word.csv 읽기 모드로 열음
i = open('Filter_Word.csv', 'r', encoding='utf-8-sig')
Filter_Word = csv.reader(i, delimiter=',')

# 필터링 단어들을 한 글자씩 읽어들임
for x in Filter_Word: 
     lines.append(x[0]) # 한 글자씩 새로운 배열에 저장

# 필터링 단어 출력

# 필터링 단어가 종료일 때 까지 반복
while(Word_Delete != '종료'): 
 Word_Delete= str(input('text : '))  # 필터링 단어 입력

 if (Word_Delete in lines):
     lines.remove(Word_Delete) # 배열에서 삭제하려는 필터링 단어 삭제

 # 삭제하려는 필터링 단어가 csv에 있는지 확인
 if(Word_Delete == '종료'):  # 필터링 단어가 종료이면 
     i = open('Filter_Word.csv', 'w', encoding='utf-8-sig',  newline='')
     Filter_Word = csv.writer(i, delimiter=',')
     for y in lines:
         Filter_Word.writerow([y])
     break # While문 빠져나감 