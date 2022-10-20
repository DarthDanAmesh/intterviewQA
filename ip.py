def ip_add(csv_list):
	ip = []
	counter = 0

	for t, u, i in csv_list:
		if i not in ip:
			ip.append(i)
			counter+=1
		else:
			counter+=1
			if counter>=2:
				return i
			print("Hello")
	#print("{i}" + "Pinged " +"{counter}" + "times")
	print("IP: {i} accessed server {counter}", i,counter)
	
	#print(counter)
print(ip_add([[11, 'index.html', '2.2.3.4.5'],[12, 'index.html', '1.2.3.4.5'],[12, 'index.html', '1.2.3.4.5'],[12, 'index.html', '1.2.3.4.5']]))