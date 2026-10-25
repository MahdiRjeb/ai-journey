with open("lines.txt","w") as f :  
 f.write("first line\n")
 f.write("the second line is longer\n")
 f.write("third line\n")

with open("lines.txt") as f :
 number_lignes={}
 number=0
 for line in f:
  number=number+1
  ligne=line.strip()
  print(number ,":" , ligne)
  


  
 
