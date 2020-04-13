import pandas as pd
import matplotlib.pyplot as plt



Input_Data_File = pd.read_csv("/content/gender_submission.csv")
Input_Test_File = pd.read_csv("/content/test.csv")
Input_Train_File =pd.read_csv("/content/train.csv")



print("Welcome to the information section......!!!")
ID = input("Enter the passanger Id:"+" ")
for i in range (len(Input_Data_File["Survived"])):
   if float(ID) == float(Input_Data_File["PassengerId"][i]) : 
      
      if Input_Train_File["Survived"][i] == 0 :
        print("The passanger is Alive")
      else:
        print("Dead")
      print("Name of the passanger:"+" "+ Input_Train_File["Name"][i])
      print("Sex:"+" "+ Input_Train_File["Sex"][i])
      print("Age:"+" "+ str(Input_Train_File["Age"][i]))
      if str(Input_Train_File["Cabin"][i])  == "Nan" or str(Input_Train_File["Cabin"][i])  == "nan" :
        print("No Table Booked.........!!!")
      else:
        print("Table Name:"+" "+ str(Input_Train_File["Cabin"][i]))  
      print("Ticket number:"+" "+ Input_Train_File["Ticket"][i])  
   else:
        pass
      
