k = int(input( ))
satr = [1]
for _ in range(k):
   print(" ".join ( map ( str, satr ) ) )
   satr = [ 1 ] + [ satr [ i ] + satr [ i + 1 ] for i in range( len ( satr ) - 1 ) ] + [ 1 ]