import pickle as pk
file = open("member.dat","wb")
while True :
      dic={}
      no = int(input("Enter memberbno. :-"))
      name = input("Enter name:-")
      dic[ "Memberno."] = no
      dic["Name"] = name
      pk.dump( dic, file )
      user = input("For quit enter quit :-")
      if user == "quit":
            break
print("Thankyou")

file.close()
