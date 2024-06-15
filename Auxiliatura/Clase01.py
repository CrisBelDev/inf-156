v = []
t = c = 0
while True:
	if c == 0:
		v.append(0.0)
	else:
		n = v[c-1]+(9.8-((12.5/68.1)*v[c-1]))*2
		if v.count(n) <= 3:
			v.append(n)
			t = t+2
		else:
			break
	c = c+1
print("n   v[m/s] \t \t    er")
for i in range(len(v)-1):
	e = (v[i+1]-v[i])/v[i+1]*100
	n = i*2
	print(n, v[i], e)