phone_book={"aaaa":2222222 ,"oledfjg":23333444,"FFF":55555}
print(phone_book["aaaa"])
print(phone_book.items)  #I forhet the () with .items() 
phone_book.get("ssss","UNKOWN")

text="mississippi"
count={}
for word in text.split():   #text.split() we use it with letter sepearted with " " but here we just use letter in text
 count[word]=count.get(word,0)   #I miss +1
print(count.items)   #I forhet the () with .items() 



My_list=[3, 1, 3, 2, 1, 5]
new_list=set(My_list)
print(new_list)
My_list2=My_list.sort()   
new_list2=set(My_list2)
print(My_list2)



grades={"Sara": 15, "Ali": 12, "Nour": 18}
somme=0
for i in grades.values:   #I forhet the () with .values() 
 somme=i+somme

moyenne=somme/len(grades)
print(moyenne)

Max=grades[0]
for i in grades.values:    
 if i>Max:
  Max=i
