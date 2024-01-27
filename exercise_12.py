x=int( input( ))
y=int(input( ))
z=int(input( ))
while z:
			p=int(input( ))
			if p<32:
						if x & (1<<p):
									print ("yes")
						else:
									print("no")
			else:
						if y &(1<<(p-32)):
									print("yes")
						else:
							 		print("no")
			z -= 1
			if z==0:
						break
						