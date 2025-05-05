character1=input("enter a bunch of words:")
char_count={}
for char in character1:
    if char==" ":
        continue
    if char in char_count:
        char_count[char]+=1
    else:
        char_count[char]=1    
most_frequent_char=None
most_frequent_num=0
for char, count in char_count.items():
    if count>most_frequent_num:
        most_frequent_char=char
        most_frequent_num=count
least_frequent_char=None
least_frequent_char_num=0
for char, count in char_count.items():
    if least_frequent_char_num==0 or count<least_frequent_char_num:
        least_frequent_char=char
        least_frequent_char_num=count
print(f"most frequent character:'{most_frequent_char}'(appears'{most_frequent_num}'times)")                
print(f"least frequent character:'{least_frequent_char}'(appears'{least_frequent_char_num}'times)")    
    