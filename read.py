data = []
count = 0
with open('reviews.txt','r') as f:
	for line in f:
		data.append(line)
		count += 1 # count = count +1
		if count % 1000 == 0: # %用來求餘數
		#print很花效能，故以千為單位產出計數情況
			print(len(data))
print('檔案讀取完了，', '總共有', len(data), '筆資料')

#exercise: 求每筆留言的平均長度
sum_len = 0
for d in data:
	sum_len = sum_len + len(d)
	#print(sum_len)
#print('所有留言總長度為',sum_len)
print('每筆留言平均長度為', sum_len/len(data))

#篩選內容長度小於100的留言
new = []
for d in data: #從存放100萬筆留言中,再提取出每1筆留言
	if len(d) < 100:
		new.append(d)
print('一共有', len(new),'筆留言長度小於100')

print(new[0])
print(new[1])

#篩選內容出現good的留言
good = []
for d in data:
	if 'good' in d:
		good.append(d)
print('一共有', len(good),'筆資料提到good')
print(good[0])






