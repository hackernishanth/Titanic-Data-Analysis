import pandas as pd
import matplotlib.pyplot as plt



Input_Data_File = pd.read_csv("/content/gender_submission.csv")
Input_Test_File = pd.read_csv("/content/test.csv")
Input_Train_File =pd.read_csv("/content/train.csv")


X_label = Input_Data_File["Survived"]
Y_label = Input_Data_File["PassengerId"]
      

Alive = 0
Dead = 0
for index in X_label:
    if index == 0:
      Alive = Alive + 1
    else:
      Dead = Dead + 1
  

#print(Alive)
#print(Dead)
fig =plt.figure()
ax = fig.add_axes([0,0,1,1])
ax.bar(["Alive"], [Alive], color = ["red"] )
ax.bar(["Dead"], [Dead], color = ["yellow"])
plt.xlabel("Rate")
plt.ylabel("No.of Count")
plt.title("Death Analysis in Titanic Ship")
plt.show()
