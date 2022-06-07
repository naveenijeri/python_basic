#most repeated words in the list
words_list = ["naveen", "nikil", "sagar", "nikil", "nikil", "naveen"]
words_set = set(words_list)
print(words_set)
result = {}
for word in words_set:
    count = 0
    for i in range(0,len(words_list)):
        if words_list[i] == word:
            count+=1
    if not result:
        result.update({word:count})
    if list(result.values())[0]<count:
        result.clear()
        result.update({word:count})

print(result)

    
