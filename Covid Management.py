import mysql.connector as sqlcon
from mysql.connector import Error
import matplotlib.pyplot as plt
import numpy as np    

def covidInfo():
    print("\t\t"+'\033[1;31;48m# '*75)
    print("\t\t"+'# '*75)
    print("\t\t"+'# #\033[1;37;48m'+' '*143+'\033[1;31;48m# #')
    print("\t\t"+'# #\033[1;34;48m'+'\t\tWelcome to  our Dharavi Covid-19 Management module!!!'+' '*85+'\033[1;31;48m# #')
    print("\t\t"+'# #\033[1;34;48m'+'\t\t                                      '+' '*100+'\033[1;31;48m# #')
    print("\t\t"+'# #\033[1;33;48m'+"\t\tIn a major shot in the arm of India's fight against Covid-19, the World Health Organization (WHO) has praised the Dharavi model of   "+' '*5+'\033[1;31;48m# #')    
    print("\t\t"+'# #\033[1;33;48m'+"\t\tcombating and controlling the deadly viral pandemic. The largest slum cluster of Asia, Dharavi is sandwiched between the Central and "+' '*5+'\033[1;31;48m# #')
    print("\t\t"+'# #\033[1;33;48m'+"\t\tWestern suburban lines in Mumbai. Spread over 2.1 sq km, Dharavi is a sort of mini-India, with over 7 to 10 lakh people staying and  "+' '*5+'\033[1;31;48m# #')
    print("\t\t"+'# #\033[1;33;48m'+"\t\tworking here. The WHO praise comes as a major boost to the efforts of the Maharashtra government. Dharavi is located nearly 1.5 km   "+' '*5+'\033[1;31;48m# #')
    print("\t\t"+'# #\033[1;33;48m'+"\t\taway from Matoshree, the private bungalow of Maharashtra chief minister Uddhav Thackeray. The Philippines government has reached out "+' '*5+'\033[1;31;48m# #')
    print("\t\t"+'# #\033[1;33;48m'+"\t\tto Brihanmumbai Municipal Corporation (BMC) to implement the Dharavi model of containing the outbreak of Covid-19 in its densely     "+' '*5+'\033[1;31;48m# #')
    print("\t\t"+'# #\033[1;33;48m'+"\t\tpopulated slums.                                                                                                                     "+' '*5+'\033[1;31;48m# #')
    print("\t\t"+'# #\033[1;34;48m'+'\t\t                                      '+' '*100+'\033[1;31;48m# #')
    print("\t\t"+'# #\033[1;33;48m'+"\t\tCivic officials said that the city succeeded in achieving what was earlier considered virtually a 'mission impossible', especially   "+' '*5+'\033[1;31;48m# #')
    print("\t\t"+'# #\033[1;33;48m'+"\t\tin Dharavi, earning the BMC and Maharashtra government a pat from the World Health Organization in early July.                       "+' '*5+'\033[1;31;48m# #')
    print("\t\t"+'# #\033[1;34;48m'+'\t\t                                      '+' '*100+'\033[1;31;48m# #')
    print("\t\t"+'# '*75)
    print("\t\t"+'# '*75+'\n\n\n\033[1;37;48m')    
    

def Login():
    status =input("Are you a registered user? y/n? Press 'q' to quit : ")  
    if status == "y" or status == "Y"  or status == "yes":
        oldUser()
    elif status == "n" or status == "N"  or status == "no":
        newUser() 
    elif status == "q" or status == "Q" or status == "quit":
        exitProgram()
    else:
        print("\033[1;31;48m\n\n\t\tINVAILD INPUT, Please try again\n\n\033[1;37;48m")
        Login()
    

def newUser():
     try:
         mycon=sqlcon.connect(host="localhost",user="root",passwd='admin',database='IP_Project')
         createLogin = input("Create login name: ")
         sql_query="select * from userpass where username='"+createLogin+"'"
         cursor = mycon.cursor()
         cursor.execute(sql_query)
         cursor.fetchall()
         
         if cursor.rowcount > 0 :
             print ("\033[1;31;48m\n\n\t\tLogin name already exists! Please try again!!\n\n\033[1;37;48m")
             newUser()
         else:
             createPassw =input("Create password: ")
             confirmpassw=input("Re-enter the password : ")
             sql="select * from userpass where password='"+confirmpassw+"'"
             cursor = mycon.cursor()
             cursor.execute(sql)
             cursor.fetchall()            
             if cursor.rowcount > 0 :
                 print("\033[1;31;48m\n\n\t\tPassword already taken. Please try again.\n\n\033[1;37;48m")
                 newUser()
             else:
                 if confirmpassw==createPassw :
                     sql_insert_Query = "insert into userpass values('"+createLogin+"','"+createPassw+"')"
                     cursor.execute(sql_insert_Query)
                     mycon.commit()
                     print("\033[1;32;48m\n\n\t\tUser created!\n\n\033[1;37;48m")
                     oldUser()
                 else:
                     print("\033[1;31;48m\n\n\t\tPasswords do not match! Please try again!!\n\n\033[1;37;48m")
                     newUser()
     
     except Error as e:
            print("Error reading data from MySQL table", e)
     finally:
            if (mycon.is_connected()):
                mycon.close()
                cursor.close()

def oldUser():
    login = input("Enter login name: ")
    passw = input("Enter password: ")
    sql_pwdchk_Query = "select * from userpass where username ='"+login+"' and password='"+passw+"'"
    try:
        mycon=sqlcon.connect(host="localhost",user="root",passwd='admin',database='IP_Project')
        cursor = mycon.cursor()
        cursor.execute(sql_pwdchk_Query)
        cursor.fetchall()
        if cursor.rowcount > 0 :
            print ("\033[1;32;48m\n\n\t\tLogin successful!\n\n\033[1;37;48m")
            showMenu()
        else:
            print ("\033[1;31;48m\n\n\t\tUser doesn't exist or wrong password! Please Try Again!!\n\n\033[1;37;48m")
            Login()
    except Error as e:
        print("Error reading data from MySQL table", e)
    finally:
        if (mycon.is_connected()):
            mycon.close()
            cursor.close()

def showMenu():
    print("What do you want to do? Please choose from below options")
    
    print("\n\t1. show all records \n\t2. add records of patient \n\t3. search records \n\t4. delete records of patient \n\t5. Graphical representation \n\t6. update the records \n\t7. Exit Program")  
    x=int(input("Enter your choice with corresponding number: "))
    if x==1:
        showAllRecords()
    elif x==2:
        addRecords()
    elif x==3:
        searchRecords()
    elif x==4:
        deleteRecords()
    elif x==5:
        showGraphs()      
    elif x==6:
        updateRecord()
    elif x==7:
        exitProgram()
    else:
        print("\033[1;31;48m\n\n\t\tINVAILD INPUT, Please try again\n\n\033[1;37;48m")
        showMenu()

def showAllRecords():
     sql_Query = "select * from patient"
     displayRecords(sql_Query)
     wanttoContinue()

def displayRecords(sql_select_Query):    
     try:
         mycon=sqlcon.connect(host="localhost",user="root",passwd='admin',database='IP_Project')         
         cursor = mycon.cursor()
         cursor.execute(sql_select_Query)
         records = cursor.fetchall()
         print("Total number of Patients: ", cursor.rowcount)
         if cursor.rowcount > 0 :
             print("\nPrinting each Patient's record")
         for row in records:
            print("Patient ID = ", row[0], )
            print("Name = ", row[1],' ', row[2])
            print("Age  = ", row[3])
            print("Area  = ", row[4])
            print("Admission date  = ", row[5])
            print("Discharged date  = ", row[6])
            print("Insurance  = ", row[7])
            print("Status  = ", row[8], "\n")

         return cursor.rowcount    
     except Error as e:
        print("Error reading data from MySQL table", e)
     finally:
            if (mycon.is_connected()):
                mycon.close()
                cursor.close()
        
def wanttoContinue():
    if (input("Do you want to continue using this program(Y/N): ")).upper()=='Y': 
        showMenu()
    else :
        exitProgram()
        
        
def addRecords():
     try:
         mycon=sqlcon.connect(host="localhost",user="root",passwd='admin',database='IP_Project')
         patientid = input('please enter Patient\'s ID: ')
         firstName = input('please enter Patient\'s first name: ')
         lastName = input('please enter Patient\'s last name: ')
         age = input('please enter Patient\'s age: ')
         area = input('please enter Patient\'s area name: ')
         admissionDate = input('please enter Patient\'s admission date: ')
         dischargeDate = input('please enter Patient\'s discharge date: ')
         insurance = input('please enter whether Patient has medical insurance(Yes/No): ')
         status = input('please enter Patient\'s status (ACTIVE/RECOVERED/DEAD): ')
         if len(dischargeDate)>0:
             sql_add_Query = "insert into patient values("+patientid+",'"+firstName+"','"+lastName+"',"+age+",'"+area+"','"+admissionDate+"','"+dischargeDate+"','"+insurance+"','"+status+"')"
         else:
             sql_add_Query = "insert into patient values("+patientid+",'"+firstName+"','"+lastName+"',"+age+",'"+area+"','"+admissionDate+"',NULL,'"+insurance+"','"+status+"')"
         cursor = mycon.cursor()
         cursor.execute(sql_add_Query)
         mycon.commit()
         print("Record added successfully ")
             
     except Error as e:
        print("Error reading data from MySQL table", e)
     finally:
            if (mycon.is_connected()):
                mycon.close()
                cursor.close()
            wanttoContinue()
                
                
def searchRecords():
     
    print("Please choose option for your search from below ")
    print("\n\t1. Patient ID \n\t2. First Name \n\t3. Last Name \n\t4. Age \n\t5. Area" +
          " \n\t6. Admission Date \n\t7. Discharge Date \n\t8. Insurance \n\t9. Status")  
   
    x=int(input("Enter your choice with corresponding number: "))
    if x==1:
        sql_Query = "select * from patient where patient_id="+input("enter ID: ")    
    elif x==2:
        sql_Query = "select * from patient where First_Name_of_patient like '%"+input("enter first name: ")+"%'"
    elif x==3:
        sql_Query = "select * from patient where last_Name_of_patient like '%"+input("enter last name: ")+"%'"
    elif x==4:
        sql_Query = "select * from patient where age="+input("enter age: ")
    elif x==5:
        sql_Query = "select * from patient where area like '%"+input("enter area: ")+"%'"      
    elif x==6:
        sql_Query = "select * from patient where admitted='"+input("enter admission date: ")+"'"
    elif x==7:
        str=input("enter discharged date: ")
        if len(str) > 0 :
            sql_Query = "select * from patient where discharged='"+str+"'"
        else :
            sql_Query = "select * from patient where discharged is null "
    elif x==8:
        sql_Query = "select * from patient where insurance like '%"+input("has insurance (Y/N): ")+"%'" 
    elif x==9:
        sql_Query = "select * from patient where status like '%"+input("enter status: ")+"%'"     
    else:
        print("\033[1;31;48m\n\n\t\tINVAILD INPUT, Showing all records\n\n\033[1;37;48m")
        sql_Query = "select * from patient"
    displayRecords(sql_Query)
    wanttoContinue()

def deleteRecords():
     try:
         mycon=sqlcon.connect(host="localhost",user="root",passwd='admin',database='IP_Project')
         patientid = input('please enter Patient\'s ID for deletion: ')
         
         sql_delete_Query = "delete from patient where patient_id ="+patientid
         cursor = mycon.cursor()
         reccount = displayRecords("select * from patient where patient_id ="+patientid)
         if reccount is not None :
             sureFlag = input("Above displayed records would be deleted, do you want to proceed (Y/N): ")
             if sureFlag.upper()=='Y':
                 cursor.execute(sql_delete_Query)
                 mycon.commit()
                 print("Record deleted successfully ")
             else:
                 print("\033[1;31;48m\n\n\t\tExiting deletion program\n\n\033[1;37;48m")
         else:
             print("No patient found with Patient ID " + patientid)
             print('Please use search functionality to find the patient ID to be deleted.')
             
     except Error as e:
        print("Error reading data from MySQL table", e)
     finally:
            if (mycon.is_connected()):
                mycon.close()
                cursor.close()
            wanttoContinue()

     
def showGraphs():
    print("Please choose option for your charts from below ")
    print("\n\t1. Areawise Patient status \n\t2. Agewise Patient status ")  
   
    x=int(input("Enter your choice with corresponding number: "))
    if x==1 or x==2:
        plotgraph(x)    
    else:
        print("\033[1;31;48m\n\n\t\tINVAILD INPUT\n\n\033[1;37;48m")
        
    wanttoContinue()

def plotgraph(x):
    
    try:
        mycon=sqlcon.connect(host="localhost",user="root",passwd='admin',database='IP_Project')
        cursor = mycon.cursor()
        if x==1:
            sql_query = 'select status, area, count(1) from patient group by  status, area   order by status, area'
            sql_area = 'select distinct area from patient order by area' 
            cursor.execute(sql_area)
            arearecords = cursor.fetchall()
            cursor.execute(sql_query)
            allrecords = cursor.fetchall()
            arealist=[]
            ACTIVElist = []
            RECOVEREDlist = []
            DEADlist=[]
            for rowarea in arearecords:
                arealist.append(rowarea[0])
                countofACTIVEPatients =0
                countofRECOVEREDPatients =0
                countofDEADPatients =0
                for rowall in allrecords:
                    if rowarea[0]==rowall[1]:
                        if (rowall[0]).upper() =="ACTIVE":
                            countofACTIVEPatients = rowall[2]
                        elif (rowall[0]).upper() =="DEAD":
                            countofDEADPatients = rowall[2]
                        elif (rowall[0]).upper() =="RECOVERED":
                            countofRECOVEREDPatients = rowall[2]
                ACTIVElist.append(countofACTIVEPatients)
                DEADlist.append(countofDEADPatients)
                RECOVEREDlist.append(countofRECOVEREDPatients)
            #for bar graph
            ind = np.arange(len(arealist)) # the x locations for the groups
            fig = plt.figure()
            ax = fig.add_axes([0,0,1,1])
            ax.bar(ind + 0.00, DEADlist, color = 'r', width = 0.25)
            ax.bar(ind + 0.25, ACTIVElist, color = 'y', width = 0.25)
            ax.bar(ind + 0.50, RECOVEREDlist, color = 'g', width = 0.25)
            ax.set_ylabel('No of Patients')
            ax.set_title('Areawise status of Patients')
            ticks=[0,1,2,3,4,5,6,7,8,9,10,11,12,13]
            ticks = ticks[0:len(arealist)]
            plt.xticks(ticks, arealist)
            ax.set_yticks(np.arange(0, 10, 1)) # y axis max and interval
            ax.legend(labels=['DEAD', 'ACTIVE','RECOVERED'])
            plt.show()
            i=0
            #for pie chart
            fig, plt1 = plt.subplots(1,4,figsize=(20, 6), sharey=True)
            statuslabels=['DEAD', 'ACTIVE','RECOVERED']    
            colr=['red','yellow','green']
            for area in arealist:  
                status=[DEADlist[i],ACTIVElist[i],RECOVEREDlist[i]]
                fig.suptitle('Areawise status of Patients')
                plt1[i].text(-0.4,1.2,area,fontsize=12, fontweight='bold')
                plt1[i].pie(status,labels=statuslabels,colors=colr,autopct='%4d%%')
                i=i+1
            plt.show()
            
        elif x==2:
            sql_query = 'select status, age, count(1) from patient group by  status, age   order by status, age'
            cursor.execute(sql_query)
            allrecords = cursor.fetchall()
            agelist=['Below 25','25 to 50','50 to 75','Above 75']
            ACTIVElist = []
            RECOVEREDlist = []
            DEADlist=[]
            for age in agelist:
                countofACTIVEPatients =0
                countofRECOVEREDPatients =0
                countofDEADPatients =0
                for rowall in allrecords:
                    if (age == agelist[0] and rowall[1] <=25) or (age == agelist[1] and rowall[1] > 25 and rowall[1] <= 50) or (age == agelist[2] and rowall[1] > 50 and rowall[1] <= 75)  or (age == agelist[3] and rowall[1] > 75):
                        if (rowall[0]).upper() =="ACTIVE":
                            countofACTIVEPatients = countofACTIVEPatients+ rowall[2]
                        elif (rowall[0]).upper() =="DEAD":
                            countofDEADPatients = countofDEADPatients+ rowall[2]
                        elif (rowall[0]).upper() =="RECOVERED":
                            countofRECOVEREDPatients = countofRECOVEREDPatients + rowall[2]
                                               
                ACTIVElist.append(countofACTIVEPatients)
                DEADlist.append(countofDEADPatients)
                RECOVEREDlist.append(countofRECOVEREDPatients)
        
            ind = np.arange(len(agelist)) # the x locations for the groups
            fig = plt.figure()
            ax = fig.add_axes([0,0,1,1])
            ax.bar(ind + 0.00, DEADlist, color = 'r', width = 0.25)
            ax.bar(ind + 0.25, ACTIVElist, color = 'y', width = 0.25)
            ax.bar(ind + 0.50, RECOVEREDlist, color = 'g', width = 0.25)
            ax.set_ylabel('No of Patients')
            ax.set_title('Ageawise status of Patients')
            ticks=[0,1,2,3,4,5,6,7,8,9,10,11,12,13]
            ticks = ticks[0:len(agelist)]
            plt.xticks(ticks, agelist)
            ax.set_yticks(np.arange(0, 10, 1)) # y axis max and interval
            ax.legend(labels=['DEAD', 'ACTIVE','RECOVERED'])
            plt.show()
            i=0
            fig, plt1 = plt.subplots(1,4,figsize=(20, 6), sharey=True)
            statuslabels=['DEAD', 'ACTIVE','RECOVERED']    
            colr=['red','yellow','green']
            for age in agelist:  
                status=[DEADlist[i],ACTIVElist[i],RECOVEREDlist[i]]
                
                fig.suptitle('Agewise status of Patients')
                plt1[i].text(-0.3,1.2,age,fontsize=12, fontweight='bold')
                plt1[i].pie(status,labels=statuslabels,colors=colr,autopct='%4d%%')
                i=i+1
            plt.show()
    except Error as e:
        print("Error reading data from MySQL table", e)
    finally:
            if (mycon.is_connected()):
                mycon.close()
                cursor.close()

def updateRecord():
     try:
         mycon=sqlcon.connect(host="localhost",user="root",passwd='admin',database='IP_Project')
         patientid = input('please enter Patient\'s ID for updation: ')
         cursor = mycon.cursor()
         displayRecords("select * from patient where patient_id ="+patientid)
         sql_update_Query_p1 = "update patient "
         sql_update_Query_p3 = " where patient_id ="+patientid
         print("Above displayed record would be updated, Please choose option for your field from below : ")
         print("\n\t1. First Name \n\t2. Last Name \n\t3. Age \n\t4. Area" +
          " \n\t5. Admission Date \n\t6. Discharge Date \n\t7. Insurance \n\t8. Status")  
   
         x=int(input("Enter your choice with corresponding number: "))
         validoption = True
         if x==1:
             sql_update_Query_p2 = "set First_Name_of_patient ='"+input("enter first name: ")+"'"
         elif x==2:
            sql_update_Query_p2 = "set last_Name_of_patient = '"+input("enter last name: ")+"'"
         elif x==3:
            sql_update_Query_p2 = "set age="+input("enter age: ")
         elif x==4:
            sql_update_Query_p2 = "set area = '"+input("enter area: ")+"'"      
         elif x==5:
            sql_update_Query_p2 = "set admitted='"+input("enter admission date: ")+"'"
         elif x==6:
             str = input("enter discharge date: ")
             if len(str)>0:
                 sql_update_Query_p2 = "set discharged='"+str+"'"
             else:
                sql_update_Query_p2 = "set discharged=NULL" 
         elif x==7:
             sql_update_Query_p2 = "set insurance='"+input("has insurance (Yes/No): ")+"'" 
         elif x==8:
             sql_update_Query_p2 = "set status = '"+input("enter status (ACTIVE/RECOVERED/DEAD): ")+"'" 
         else:
             print("\033[1;31;48m\n\n\t\tINVAILD INPUT\n\n\033[1;37;48m")
             validoption=False
         if validoption:
             cursor.execute(sql_update_Query_p1+sql_update_Query_p2+sql_update_Query_p3)
             mycon.commit()
             print("\033[1;32;48m\n\n\t\t Record has been updated.  \n\n\033[1;37;48m")
     except Error as e:
        print("Error reading data from MySQL table", e)
     finally:
            if (mycon.is_connected()):
                mycon.close()
                cursor.close()
            wanttoContinue()
            
def exitProgram():
     print("\033[1;32;48m\n\n\t\t Exiting program. Thank you for using Covid Management System.  \n\n\033[1;37;48m")
            
def main():
    covidInfo()
    Login()

main()