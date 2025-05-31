import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.preprocessing import LabelEncoder
#Loading the datasets for Visulization from NSS(78th) Survey of Multiple 
#Indicators in INDIA
#Data Source :- National Sample Survey Office,MoSPI
data1 = pd.read_csv("NSS1.csv")
data2 = pd.read_csv("NSS2.csv")
data3 = pd.read_csv("NSS3.csv")
data4 = pd.read_csv("NSS4.csv")
data5 = pd.read_csv("NSS5.csv")
data7 = pd.read_csv("NSS7.csv")
data8 = pd.read_csv("NSS8.csv")
data9 = pd.read_csv("NSS9.csv")
data10 = pd.read_csv("NSS10.csv")
data12 = pd.read_csv("NSS12.csv")
data14 = pd.read_csv("NSS14.csv")
data15 = pd.read_csv("NSS15.csv")
data17 = pd.read_csv("NSS17.csv")

#Visulization According to the:-
#Percentage of Persons Who Used Mobile Telephone....
#with Active Sim Card at Least Once During Last Three Months Preceding the Date of the Survey
class NSS_1:
    def first_plot(self):
# Group the data by 'Gender' and sum the 'Value' for each group
        gender_value_sum = data1.groupby('Gender')['Value'].sum().reset_index()

# Create a pie chart
        sns.set(style="whitegrid")
        plt.figure(figsize=(8, 8))
        plt.pie(gender_value_sum['Value'], labels=gender_value_sum['Gender'], autopct='%1.1f%%', startangle=90)
        plt.title('Percentage of Persons Who Used Mobile Telephone with Active Sim Card at Least Once During Last Three Months Preceding the Date of the Survey according to  Gender')
        plt.show()

    def second_plot(self):
        a=data1['Sector']
        b=data1['Value']
        plt.title("Percentage of Persons Who Used Mobile Telephone with Active Sim Card at Least Once During Last Three Months Preceding the Date of the Survey According to the Sectors")
        plt.xlabel("Sector vise distibution")
        plt.ylabel("value out of 100")
        sns.barplot(x=a,y=b,data=data1,palette="Greens")

    def Third_plot(self):
        ax=sns.countplot(x='Age Group',data=data1,color='orange')
        
        plt.xlabel("Age Group")
        plt.ylabel("count of Age Group")
        for bars in ax.containers:
            ax.bar_label(bars)
            plt.title("Percentage of Persons Who Used Mobile Telephone with Active Sim Card at Least Once During Last Three Months Preceding the Date of the Survey")   
            
        plt.show()

#Visulization According to the:-
#Percentage of Households Reported Access to Broadband Within the Premises and Mass Media
class NSS_2:    
    def first_plot(self):
        x=data2['State']
        y=data2['Value']
        plt.bar(x,y)
        plt.xticks(rotation=90) #rotate the x tickets
        plt.ylabel("value out of hundred")
        plt.xlabel("states of India")
        plt.title("Percentage of Households Reported Access to Broadband Within the Premises and Mass Media")

    plt.show()
    def second_plot(self):
        gender_value_sum = data2.groupby('Sector')['Value'].sum().reset_index()

# Create a pie chart
        sns.set(style="whitegrid")
        plt.figure(figsize=(8, 8))
        plt.pie(gender_value_sum['Value'], labels=gender_value_sum['Sector'], autopct='%1.1f%%', startangle=90)
        plt.title('Percentage of Households Reported Access to Broadband Within the Premises and Mass Media')
        plt.show()
    def third_plot(self) :
        plt.xlabel("values for the MassMedia in India")
        plt.ylabel("Count of of the values")
        plt.title("Uses of the internet in all over India")
    #create the histogram for the given data
        plt.hist(data2['Value'],bins=100,color='Purple')   
        plt.show()

#Visulization According to the:-
#Percentage Distribution of Persons by Main Reason for Leaving Last Usual Place of Residence
class NSS_3:

    def graph1(self):
    # Count the occurrences of each unique Migration Reason
        migration_reason_counts = data3['Migration Reason'].value_counts()
    
    # Plotting the bar chart
        sns.barplot(x=migration_reason_counts.index, y=migration_reason_counts.values)
        plt.xticks(rotation=70)
        plt.xlabel('Migration Reason')
        plt.ylabel('Count')
        plt.title('Migration Reason Counts')
        plt.show()

    def graph2(self):
        #sector vice migration of the peoples
        sec=data3['Sector'].value_counts()
        sns.barplot(x=sec.index,y=sec,palette='dark')
        plt.title("Count of the Migration form rular or Urban Areas")
        plt.xlabel("Ruler or Urban sectors")
        plt.ylabel("Count of the peoples ")
        plt.show()

#Visulization According to the:-
#Percentage Distribution of Persons by Availability of Hand Washing Facility Within the Premises

class NSS_4:

    def gr1(self):
        x=data4['Sector']
        y=data4['Value']
        plt.xlabel("Sectors of the India")
        plt.ylabel("percentage")
        plt.title("Percentage Distribution of Persons by Availability of Hand Washing Facility Within the Premises")
        plt.bar(x,y,color=['red','blue'])
        plt.show()
    def gr2(self):
        Y_axis=data4['Value']    
        X_axis=data4['Sub Indicator']
        plt.xlabel("Mediums of Hand Washing in India")
        plt.ylabel("Percentage of Hndwshing medium")
        plt.title("Percentage of Handwasing Medium in India")
        plt.xticks(rotation=5)
        plt.bar(X_axis,Y_axis,color='orange')
        plt.show()
    def gr3(self):
            
        d2=data4['Value']
        plt.hist(d2,bins=20,color='skyblue')
        plt.xlabel("Percentage of hand washing medium")
        plt.ylabel("Count of the maximum of minimum percentage")
        plt.title("Count of the Maximum or the minimum percentage ")
        plt.show()

#Visulization According to the:-
#Percentage of Persons Reported Access to Improved Latrine and Exclusive Access to Improved Latrine for Each State, Among Persons Reported to Have Access to Latrine
class NSS_5:

    print(data5.isnull().sum()) 
    def plot1(self):
        c1=data5["State"]
        c2=data5['Value']
        plt.xticks(rotation=90)
        plt.bar(c1,c2,color='brown')
        plt.xlabel("STATES OF INDIA")
        plt.ylabel("Percentage of  Persons Reported Access to Improved Latrine")
        plt.title("Percentage of  Persons Reported Access to Improved Latrine Amoung States ")
        plt.show()
    def plot2(self):
        enc=LabelEncoder()
        data5['Sub Indicator']=enc.fit_transform(data5['Sub Indicator'])
        x=data5['Sub Indicator']
        y=data5['Value']
        plt.scatter(x,y,color='red')
        # 0 for Access to Improved Latrine
        # 1 for Exclusive Access to Improved Latrine
        plt.xlabel("Exclusive Access to Improved Latrine or Access to Improved Latrine")
        plt.ylabel("Percentage of  Persons Reported Access to Improved Latrine")
        plt.title("count of people who uesd the latrin Exlusivly or normally")
        plt.show()

#Visulization According to the:-
#Percentage Distribution of Persons* Reporting as Earner in the Last Usual Place of Residence by Change in Income Due to Migration

class NSS_7:
   

    
    def plot1(self):
        x=data7['Value']
        y=data7['State']
        plt.xlabel("states of india")
        plt.ylabel("percentage of economy change due to migration")
        plt.title("Percentage Distribution of Persons* Reporting as Earner in the Last Usual Place of Residence by Change in Income Due to Migration over states")
        plt.xticks(rotation=90)
        plt.bar(y,x,color='red')
        
        plt.show()

    def plot2(self):
        d=data7['Value']
        plt.title("Count of the percentage ")
        sns.histplot(x=d,bins=50,color='green')
        plt.show()

    def plot3(self):
        x=data7['Sub Indicator']
        y=data7['Value']
        sns.barplot(x=x,y=y,data=data7,palette='dark')
        plt.title("Effect of The Migration on Economy")
        plt.show()

#Visulization According to the:-
#Percentage of Households Which Have Purchased/ Constructed New House/flat for Residential Purpose After 31.03.2014, 
#Purchased for the First Time and Owned that



class NSS8:
   
    print(data8.isnull().sum())
    def plot1(self):
        x=data8['Value']
        y=data8['Sector']
        sns.barplot(x=y,y=x,data=data8,palette='dark')
        plt.xlabel("Sector of India")
        plt.ylabel("Values According to the Sectors")
        plt.title("Percentage of Households Which Have Purchased/ Constructed New House/flat for Residential Purpose After 31.03.2014, Purchased for the First Time and Owned that House/flat as on Date of Survey")
        plt.show()

    def plot2(self):
        dt1=data8['Value']
        dt2=data8['State']
        plt.bar(dt2,dt1)
        plt.ylabel("Percentage of the People who purchased House/Flat")
        plt.xlabel("State vice Partician")
        plt.title("Percentage of the People who purchased House/Flat According to States")
        plt.tick_params(axis='x',rotation=90,labelsize=10)
        
        
        plt.show()
    def plot3(self):
        df=data8.groupby('Sub Indicator')['Value'].sum().reset_index()
        plt.pie(df['Value'],labels=df['Sub Indicator'],autopct='%1.1f%%',startangle=180) 
        plt.title('Percentage of Households  Constructed New House/flat for Residential Purpose After 31.03.2014, Purchased for the First Time and Owned  as on Date of Survey')
        
    def plot4(self):
        ax=sns.countplot(x='Sector',data=data8,color='yellow')
        plt.xlabel("Sector")
        plt.ylabel("count of Sector")
        for bars in ax.containers:
            ax.bar_label(bars)
            plt.title(" Percentage of Households  Constructed New House/flat for Residential Purpose After 31.03.2014, Purchased for the First Time and Owned  as on Date of Survey")
            plt.show()
     
        plt.show()


    
#Visulization According to the:-
#Percentage of Persons Reported Access to Drinking Water,
# Exclusive Access to Drinking Water, 
# Access to Improved Source of Drinking Water and Sufficiency of Drinking Water





class NSS_9:
    data = pd.read_csv("NSS9.csv")
    #checking weather the data have the null values
    print(data.isnull().sum())
    def plot1(self):
        x=data9['Value']
        y=data9['State']
        plt.xlabel("states")
        plt.ylabel("percentage of Drinkig Water")
        plt.title("Percentage of Persons Reported Access to Drinking Water, Exclusive Access to Drinking Water, Access to Improved Source of Drinking Water and Sufficiency of Drinking Water")
        plt.xticks(rotation=60)
        plt.bar(y,x,color='green')
        plt.tick_params(axis='x',labelsize=9)
        
        plt.show()
    def plot2(self):
        d=data9['Value']
        plt.title("Count of the percentage of Drinking Water ")
        sns.histplot(x=d,bins=50,color='green')
        plt.tick_params(axis='x',labelsize=8)
        plt.show()
    def plot3(self):
        enc=LabelEncoder()
        data9['Sub Indicator']=enc.fit_transform(data9['Sub Indicator'])
        x=data9['Sub Indicator']
        y=data9['Value']
        plt.ylabel("percentage of Drinkig Water")
        plt.xlabel("Sub indicators")
        plt.title("Percentage of Persons Reported Access to Drinking Water, Exclusive Access to Drinking Water, Access to Improved Source of Drinking Water and Sufficiency of Drinking Water")
        
        plt.scatter(x,y,c=x,cmap='rainbow')
        plt.xticks(rotation=2)
        # 0 for Piped Water into Dwelling or Yard/plot Which was Sufficiently Available Throughout the Year
        # 1 for Improved Source of Drinking Water Located in the Household Premises Which is Sufficiently Available Throughout the Year
        # 2 for Improved Source of Drinking Water Located in the Household Premises
        # 4 for Exclusive Access to Improved Source of Drinking Water Located in the Household Premises Which is Sufficiently Available Throughout the Year
        # 5 for Exclusive Access to Improved Source of Drinking Water Located in the Household Premises Which is Sufficiently Available Throughout the Year
        
        plt.show()

#Visulization According to the:-
#Percentage Distribution of Households by the Availabilty of Basic Transport and Public Facility

class NSS10:
    
    def graph1(self):
        x1=data10['State']
        y1=data10['Value']
        plt.bar(x1,y1)
        plt.xticks(rotation=65)
        plt.title("Percentage Distribution of Households by the Availabilty of Basic Transport and Public Facility By States")
        plt.ylabel("Percentage values")
        plt.show()
    def graph2(self):
        x1=data10['Sub Indicator']
        y1=data10['Value']
        sns.barplot(x=y1,y=x1,data=data10)
        plt.title("percentage of transport services")
        plt.yticks(rotation=65)
        plt.show()
    def graph3(self):
        df=data10.groupby('Sector')['Value'].sum().reset_index()   
        plt.pie(df['Value'],labels=df['Sector'],autopct="%1.1f%%")
        plt.title("Sector vice Partician of the Transport Facilitis in India")
        plt.show()
    def graph4(self):    
        ax=sns.countplot(x='Sector',data=data10,color='yellow')
        plt.xlabel("Sector")
        plt.ylabel("count of Sector")
        for bars in ax.containers:
            ax.bar_label(bars)
            plt.title("Count of the sectors in transport Facilities in India ")
            plt.show()

#Visulization According to the:-
#Percentage of Persons* Whose Current Place of Residence is Different From the Last Usual Place of Residence

class NSS12:
    
    def grp1(self):
        x1=data12['State']
        y1=data12['Value']
        sns.barplot(x=x1,y=y1,data=data12,color='green')
        plt.ylabel("Percentage of peoples who changed their Residance")
        plt.title("Percentage of Persons* Whose Current Place of Residence is Different From the Last Usual Place of Residence")
        plt.xticks(rotation=75)
        plt.show()

    def grp2(self):
        x1=data12['Sector']
        y1=data12['Value']
        plt.bar(x1,y1,color='orange')
        plt.xlabel("Sectors of India")
        plt.ylabel("Percentage of peoples who changed their Residance")
        plt.title("People who change their Residance According to sector")
        plt.show()
    def grp3(self):
        dt=data12['Value']
        plt.hist(dt,bins=50,color='skyblue')
        plt.xlabel("Values")
        plt.ylabel("count of values")
        plt.title("Count of Persons* Whose Current Place of Residence is Different From the Last Usual Place of Residence")
        plt.show()
#Visulization According to the:-        
#Percentage of Persons* Willing to Move Out From the Present Place of Residence and Percentage Distribution of such Persons by Main Reason# for Leaving Present Place of Residence
class NSS14:
    
    def pl1(self):
        
        ax=sns.countplot(x='Gender',data=data14,color='green')
        plt.xlabel("Gender")
        plt.ylabel("count of Gender")
        for bars in ax.containers:
            ax.bar_label(bars)
            plt.title("Count of Main reason for Migration on Gender ")
            plt.show()
            
    def pl2(self):
        df=data14.groupby('Main reason for Migration')['Value'].count().reset_index()   
        plt.pie(df['Value'],labels=df['Main reason for Migration'],autopct="%1.1f%%")
        plt.title("Main reason for Migration in India")
        plt.show()

    def pl3(self):
        df=data14.groupby('Sector')['Main reason for Migration'].count().reset_index()   
        plt.pie(df['Main reason for Migration'],labels=df['Sector'],autopct="%1.1f%%")
        plt.title("Sector vice reason for Migration in India")
        plt.show()

    def pl4(self):
        ax=sns.countplot(x='State',data=data14,color='green')
        plt.xlabel("States of India")
        plt.ylabel("count of State")
        for bars in ax.containers:
            ax.bar_label(bars)
            plt.title("Count of Main reason for Migration in the Various States ")
            plt.xticks(rotation=70)
            plt.show()

#Visulization According to the:-   
#Percentage Distribution of Different Sources of Finance From Which Maximum Amount was Financed by the Household for New House/flat*

class NSS15:
    
    
    def plot1(self):
        s1=data15['State']
        s2=data15['Value']
        plt.bar(s1,s2,color='brown')
        plt.xlabel("states of India")
        plt.ylabel("Percentage Values")
        plt.title("Percentage Distribution of Different Sources of Finance From Which Maximum Amount was Financed by the Household for New House/flat")
        plt.xticks(rotation=70)
        plt.show()

    def plot2(self):
        a1=data15["Source of finance"]
        a2=data15['Value']
        sns.barplot(x=a1,y=a2,data=data15,palette="Greens")
        plt.xlabel("source of finance in India")
        plt.ylabel("Values in Percentage")
        plt.title("Source of finance for the new House/Flat")
        plt.show()

    def plot3(self):
        s1=data15['Sector']
        s2=data15['Value']
        plt.bar(s1,s2,color='orange')
        plt.xlabel("Sectors of india")
        plt.ylabel("Values in Percentage")
        plt.title("Sector vice Source of finance for the new House/Flat")
        plt.show()
    def plot4(self):
        dt=data15['Value']
        sns.histplot(dt,bins=100,color='pink')
        plt.xlabel("Values in Percentage")
        plt.ylabel("count of values")
        plt.title("Count of Persons*who has Different Sources of Finance From Which Maximum Amount was Financed by the Household for New House/flat*")

        plt.show()

#Visulization According to the:-
#Percentage of Households Reporting Possession of Air Conditioner and Air Cooler



class NSS17:
    
    
    def pl1(self):
      
        ax=sns.countplot(x='Sector',data=data17,color='pink')
        plt.xlabel("Sector")
        plt.ylabel("count of Sectors")
        for bars in ax.containers:
            ax.bar_label(bars)
            plt.title("Count of Households Reporting Possession of Air Cooler in Different Sectors ")
            plt.show()
            
    def pl2(self):
        df=data17.groupby('Sub Indicator')['Value'].count().reset_index()   
        plt.pie(df['Value'],labels=df['Sub Indicator'],autopct="%1.1f%%")
        plt.title("Percentage of Households Reporting Possession of Air Conditioner and Air Cooler")
        plt.show()

    

    def pl4(self):
        ax=sns.countplot(x='State',data=data17,color='green')
        plt.xlabel("States of India")
        plt.ylabel("count of State")
        for bars in ax.containers:
            ax.bar_label(bars)
            plt.title(" Percentage of Households Reporting Possession of Air Conditioner and Air Cooler")
            plt.xticks(rotation=70)
            plt.show()

#calling the different methos of classes for viewing the plots

#Calling the NSS_1 class and its methods
cl1=NSS_1()
cl1.first_plot()
cl1.second_plot()
cl1.Third_plot()
#Calling the NSS_2 class and its methods
cl2=NSS_2()
cl2.first_plot()
cl2.second_plot()
cl2.third_plot()
#Calling the NSS_3 class and its methods
cl3=NSS_3()
cl3.graph1()
cl3.graph2()
#Calling the NSS_4 class and its methods
cl4=NSS_4()
cl4.gr1()
cl4.gr2()
cl4.gr3()
#Calling the NSS_5 class and its methods
cl5=NSS_5()
cl5.plot1()
cl5.plot2()
#Calling the class NSS_7 for viualization
cl7=NSS_7()
#Calling the functions of  class NSS_7 for viualization
cl7.plot1()     
cl7.plot2()  
cl7.plot3()

#Calling the class NSS_8 for viualization
cl8=NSS8()
#Calling the functions of  class NSS_8 for viualization
cl8.plot1()
cl8.plot2()
cl8.plot3()
cl8.plot4()

#Calling the class NSS_9 for viualization
pl9=NSS_9()
#Calling the functions of  class NSS_9 for viualization
pl9.plot1()
pl9.plot2()
pl9.plot3()

#Calling the class NSS_10 for viualization
cl10=NSS10() 
#Calling the functions of  class NSS_10 for viualization 
cl10.graph1()
cl10.graph2()
cl10.graph3()
cl10.graph4()

#Calling the class NSS_12 for viualization
cl12=NSS12()
#Calling the functions of  class NSS_12 for viualization
cl12.grp1()
cl12.grp2()
cl12.grp3()

#Calling the class NSS_12 for viualization
cl14=NSS14()
#Calling the functions of  class NSS_12 for viualization
cl14.pl1()
cl14.pl2()
cl14.pl3()
cl14.pl4()  

#Calling the class NSS_15 for viualization
cl15=NSS15()
#Calling the functions of  class NSS_15 for viualization
cl15.plot1()
cl15.plot2()
cl15.plot3()
cl15.plot4()

#Calling the class NSS_17 for viualization
cl17=NSS17()
#Calling the functions of  class NSS_17 for viualization
cl17.pl1()
cl17.pl2()
cl17.pl4()
