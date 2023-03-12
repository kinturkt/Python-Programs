def fact(x):
	if x==1 or x==0:    
	   
	# 0!=1 and 1!=1
	
		return 1
	else: 
		return (x*fact(x-1))
num=0
print ("The Factoriaal of",num,"is",fact(num))