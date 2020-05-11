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
good = [e for e in data if 'good' in e]

bad = ['bad' in d for d in data ]