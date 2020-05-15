data = []
count = 0
with open('reviews.txt', 'r') as f :
	for line in f :
		data.append(line)
		count += 1
		if count % 1000 == 0 :# %求餘數
			print(len(data))
print('讀取完畢，共有', len(data), '筆資料')


sum_len = 0
for e in data :
	sum_len += len(e)
print('留言平均長度為',sum_len/len(data), '個字')

new = []
for e in data :
	if len(e) < 100 :
		new.append(e)
print('有', len(new), '筆留言少於100字')
print(new[0])

good_words = []
for e in data :
	if 'good' in e :
		good_words.append(e)
print('留言中有出現good筆數共', len(good_words), '筆留言')

#清單快寫法
good = [e for e in data if 'good' in e] #第一個e為要裝進清單的值

bad = ['bad' in d for d in data ] #'bad' in d 是一個運算，結果為true false


#文字記數
word_count = {}
counting = 0
words = []
for d in data:
	words = d.split()
	for w in words :
		if w in word_count:
			word_count[w] += 1
		else:
			word_count[w] = 1
for word in word_count:
	if word_count[word] > 100000 :
		print(word, word_count[word])
# # print(len(word_count))
# # print(word_count['Allen'])

while True :
	word = input('請問你想查什麼字？　')
	if word == 'q':

		break
	if word in word_count :
		print(word, '出現過的次數為: ', word_count[word])
	else :
		print('這個字沒有出現過')
print('感謝使用字典查詢系統')