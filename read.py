data = []
count = 0
with open("reviews.txt", 'r') as f:
	for line in f:
		data.append(line)
		count  += 1
		# if count % 1000 == 0:
			# print(len(data))
print('檔案讀取完了，共有', len(data), '筆資料')
x=0
for d in data:
	x = len(d) + x
avg = x / len(data)
print('留言平均長度為:', avg)