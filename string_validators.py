def review(s):
	#print (len(s))
	if len(s) < 1000:	
		f=1
		for c in s: 
			if c.isalnum() is True: 
				#print ("alnum", True)
				print (True)
				break
			else: 
				if f == len(s):
					#print (False, f, len(s))				
					print (False)				
				f = f+1
		f=1
		for c in s: 
			if c.isalpha() is True: 
				#print ("alnum", True)
				print (True)
				break
			else: 
				if f == len(s):
					#print (False, f, len(s))				
					print (False)				
				f = f+1

		f=1
		for c in s: 
			if c.isdigit() is True: 
				#print ("alnum", True)
				print (True)
				break
			else: 
				if f == len(s):
					#print (False, f, len(s))				
					print (False)				
				f = f+1

		f=1
		for c in s: 
			if c.islower() is True: 
				#print ("alnum", True)
				print (True)
				break
			else: 
				if f == len(s):
					#print (False, f, len(s))				
					print (False)				
				f = f+1
		f=1
		for c in s: 
			if c.isupper() is True: 
				#print ("alnum", True)
				print (True)
				break
			else: 
				if f == len(s):
					#print (False, f, len(s))				
					print (False)				
				f = f+1

if __name__ == '__main__':
	s = input()
	review(s)


