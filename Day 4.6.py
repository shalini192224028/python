def delChar(s, c) :
	counts = s.count(c)
	s = list(s)
	while counts :
		s.remove(c)
		counts -= 1
	s = '' . join(s)
	print(s)
s = input("Enter a string: ")
c = input("Enter a character: ")
print(delChar(s,c))
