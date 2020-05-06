from time import sleep
import sys
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
Name = input("Enter Your Answer: ")

print(" ____________________")
print("< Hello!, "+ Name+"    >")
print(" -------------------- ")
print("      \   ^__^        ")
print("       \  (oo)\_______")
print("          (__)\       )/")
print("              ||----w |")
print("              ||     ||")
print("-----------------------")

time.sleep(1)




# Question 2
print(" ")
print("2:Press The Enter Button")
print("")
print("""\

███████╗███╗   ██╗████████╗███████╗██████╗ 
██╔════╝████╗  ██║╚══██╔══╝██╔════╝██╔══██╗
█████╗  ██╔██╗ ██║   ██║   █████╗  ██████╔╝
██╔══╝  ██║╚██╗██║   ██║   ██╔══╝  ██╔══██╗
███████╗██║ ╚████║   ██║   ███████╗██║  ██║
╚══════╝╚═╝  ╚═══╝   ╚═╝   ╚══════╝╚═╝  ╚═╝
                                           

          """)
print("")
ans2 = input("Enter Your Answer: ")
if(ans2 == ""):
     points+=1
else:
     wronganswers+=1







# Question 3
print(" ")
print("3: ?siHT daeR ruoY naC")
print("(a)No\n(b)Yes\n(c)I am Sleeping\n(d)i hate this game\n")
anss = input("Enter Your Answer: ")
if(anss == "b"):
     points+=1
else:
     wronganswers+=1





# Question 4
print(" ")
print("4: Guess the Contry Flag")
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



# Question 5
print("5) Can you see THIS?")
print("(a)Yes\n(b)No\n(c)Probably\n(d)Who Cares?\n")
ans = input("Enter Your Answer: ")
if(ans == "a"):
     points+=1
else:
     wronganswers+=1



# Question 6
print("6)")
print("""\
          ^         
         | |        
       @#####@      
     (###   ###)-.  
   .(###     ###) \ 
  /  (###   ###)   )
 (=-  .@#####@|_--"      This is a hold up! Put all your money in the
 /\    \_|l|_/ (\        disk drive slot, and no one gets hurt!
(=-\     |l|    /   
 \  \.___|l|___/    
 /\      |_|   /    
(=-\._________/\    
 \             /    
   \._________/     
     #  ----  #     
     #   __   #       
     \########/      

         V
             V
           V
     """)
print("(a)Yes\n(b)No\n(c)I WON'T\n(d)ok,ok I am putting the Money But Please Don't Hurt me")
ans = input("Enter Your Answer: ")
if(ans == "a" or "d"):
     points+=2



     thanks = "ĹМŦĂŐ XD, 𝕿𝖍𝖆𝖓𝖐𝖘   " + Name
     youaregetting = "You are Getting One Extra Point For It ^_^"
     for x in thanks:
          print(x, end='')
          sys.stdout.flush()
          sleep(0.1)
     print("")
     for x in youaregetting:
          print(x, end='')
          sys.stdout.flush()
          sleep(0.1)


else:
     wronganswers+=1






print("Your total points :" + str(points))
print("wronganswers :" + str(wronganswers))

