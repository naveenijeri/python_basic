#deep copy whenever we change the nested elements it won't effect the original elements
import copy
list1 = [1,[2,3],4,5]
list2 = copy.deepcopy(list1)
list2[1][0]="naveen"
print(list1)
print(list2)
