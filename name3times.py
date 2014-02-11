##nyobain function

def repeat(s,exclaim):
 result = s + s + s # can also use "s * 3" which is faster (Why?)
 if exclaim:
  result = result + '!!!'
 return result
	
def main():
 print (repeat('Yay ',False))
 print (repeat('Woo Yeah ',True))

#def main():
# name='Guido'
# if name == 'Guido':
#  print (repeeet(name,False)+'!!!!')
# else:
#  print (repeat(name,True))
  
if __name__ == '__main__':
 main()