import random
li=['hi','bye','ml','ai','co']
s=random.choice(li)
#print(s)
print("WELCOME TO HANGMAN GAME")
c=0
print("There are",len(s),"letters in the word")
a=0
while(c<6):
 m=(input())
 k=0
 for i in range(0,len(s)):
  if(s[i]==m):
    print("Correct and it's found at",i+1,"position in the",len(s),"lettered word")
    a=a+1
  else:
   k=k+1
 if(k==len(s)):
   c=c+1
   print(" w You are left with",6-c,"more chances")
 if(a==len(s)):
   print("You got it!")
   exit()

