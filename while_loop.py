def main():
	count = 0
	while True:
		count+=1
		if count == 500:
			break
		if count%2==0:
			continue
		print(f'the count is {count}, mod equals 0: {count%2==0}')
main()

