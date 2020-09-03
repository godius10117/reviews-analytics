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

#list comprehension 清單快寫法；同上方good篩選
good = [d for d in data if 'good' in d]
#for 前面可放篩選的留言d,凡有good則印出留言
#或數字1，凡有good則印出1
#或合併字串d+'123'凡有good則印出留言+'123'
#或運算，如：
bad = ['bad'in d for d in data]
#即印出100萬筆留言，留言出現bad，則為True,否則為False
print(bad)
#等同下方寫法：
bad = []
for d in data:
    bad.append('bad' in d)


# 文字計數

wc = {} #word_count
for d in data:
	words = d.split() #預設為空白鍵，且連續空白時不會切成空字串
	for word in words:
		if word in wc:
			wc[word] += 1
		else:
			wc[word] = 1 #新增新的key進wc字典

for word in wc:
	if wc[word]>1000000:
		print(word,wc[word])

print(len(wc))
print(wc['Allen'])

while True:
	word = input('請問你想查什麼字：')
	if word == 'q':
		break
	if word in wc:
		print(word, '出現過的字數為：', wc[word])
	else:
		print('這個字沒有出現過喔!')

print('感謝使用本查詢功能')









