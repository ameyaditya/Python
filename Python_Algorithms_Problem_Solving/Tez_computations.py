from itertools import combinations as cmb
list1_of_people = ['Amey','Abhisar','Kalpaj','Bhumika','Jayaram SP','VH Kustagi']
list2_of_people = ['Amey','Jayaram SP','VH Kustagi','Radhika Vadiraj','Anvita','Vaibhav']
Result1 = cmb(list1_of_people,2)
Result2 = cmb(list2_of_people,2)
for item in Result1:
    print(item[0]+'-->'+item[1])
