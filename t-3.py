
import os
import shutil

s=r"C:\Users\Srikanth\OneDrive\Desktop\source"
d=r"C:\Users\Srikanth\OneDrive\Desktop\destination"

f=os.listdir(s)
if not os.path.exists(d):
    os.makedirs(d)

for i in f:
  
  if(i.lower().endswith(".jpg")):
    sp=os.path.join(s,i)
    dp=os.path.join(d,i)
    
    try:
        shutil.move(sp,dp)
               
    except FileNotFoundError:
      print("not found")
print("The moved .jpg files are: ")
print(os.listdir(d))