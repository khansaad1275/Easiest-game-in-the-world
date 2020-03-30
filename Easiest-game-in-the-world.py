import time
points = 0
wronganswers = 0

'''
print("|This Game is A Logical|")
print("|                      |")
print("|                      |")
print("|                      |")
print("|                      |")
print("|                      |")
print(" -----------------------")'''


# Question 1
print("1) Enter Your Name ")
ans = input("Enter Your Answer: ")

print(" ____________________")
print("< Hello!, "+ ans+"    >")
print(" -------------------- ")
print("      \   ^__^        ")
print("       \  (oo)\_______")
print("          (__)\       )/")
print("              ||----w |")
print("              ||     ||")
print("-----------------------")

time.sleep(3)




# Question 2
print(" ")
print("2:Press The Enter Button")
print("")
ans2 = input("Enter Your Answer: ")






# Question 3
print(" ")
print("3: ?siHT daeR ruoY naC")
print("(a)No\n(b)Yes\n(c)I am Sleeping\n(d)i hate this game\n")
ans2 = input("Enter Your Answer: ")
if(ans2 == "b"):
     points+=1
else:
     wronganswers+=1





# Question 3
print(" ")

print("3: Guess the Contry Flag")
print("")
print(" _________")
print("|::_,^._::|")
print("|::\___/::|")
print("|::__|__::|")
print("")

print("(a)India\n(b)USA\n(c)China\n(d)Canada\n")

ans3 = input("Enter Your Answer: ")
if(ans3 == "d"):
     points+=1
else:
     wronganswers+=1



# Question 4
print("4) Can you see THIS?")
print("(a)Yes\n(b)No\n")
ans = input("Enter Your Answer: ")
if(ans == "a"):
     points+=1
else:
     wronganswers+=1






print("Your total points :" + str(points))
print("wronganswers :" + str(wronganswers))

