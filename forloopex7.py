#ForLoopEx4.py
s="PYTHON"
print("By using for loop--Forward Direction without Indices")
for ch in s:
    print("\t{}".format(ch))
print("---------------------------------------------")
print("By using for loop--Backward Direction without Indices")
for ch in s[::-1]: # Extended Slicing
    print("\t{}".format(ch))
print("---------------------------------------------")
print("By using for loop--Forward Direction with +VE Indices")
for index in range(len(s)):
    print("\t{}".format(s[index]))
print("---------------------------------------------")
print("By using for loop--Forward Direction with -VE Indices")
for index in range(-len(s),0):
    print("\t{}".format(s[index]))
print("---------------------------------------------")
print("By using for loop--Backward Direction with +VE Indices")
for index in range(len(s)-1,-1,-1):
    print("\t{}".format(s[index]))
print("---------------------------------------------")
print("By using for loop--Backward Direction with -VE Indices")
for index in range(-1,-(len(s)+1),-1):
    print("\t{}".format(s[index]))
print("---------------------------------------------")