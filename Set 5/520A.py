from collections import Counter

number = int(input())
word = input().lower()
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
for i in range(0,number):
    if(word[i] in alphabet):
        alphabet.remove(word[i])
if(len(alphabet)==0):
    print("YES")
else:
    print("NO")