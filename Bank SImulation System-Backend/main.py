#                                        JS BANK SIMULATION SYSTEM


# Importing neccessary modules
# ____________________________
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

print("\n==========================================================================BANK SIMULATION SYSTEM==============================================================================")
start =input("\nWelcome! Wanna Simulate or Analyze the Customer Details?\n________________________________________________________\n ")

# For Simulation randomly and Queueing Model
# __________________________________________

if(start == 'simulate' or start=='SIMULATE' or start == 'Simulate'): 
    user = input("\nWhat You wanna simulate?\n________________________\n")
    predicted = ['simulate customer details', 'simulate queueing model']
    # Converting predicted input list into upper case 
    upp = [i.upper() for a,i in enumerate(predicted)]

    # SIMULATING CUSTOMER DETAILS
    # ___________________________

    if (user == predicted[0] or user== upp[0]):
        day= int(input("\nWe have 3 days Record of Customer, which day you wanna see? \n"))
        if(day== 1):
            print("\n\t\t\t\t\tCUSTOMER RECORD HISTORY\n")
            Customer_data = pd.read_csv('Day1.csv')
            print(Customer_data)   

            print("\nSimulating Customer Details: \n____________________________")
            Avg_Arrival_Time = np.array(round(np.mean(Customer_data['Arrival'])))
            print("\n-Average Arrival Time of Customers : "+str(Avg_Arrival_Time))

            Avg_Service_Time = np.array(round(np.mean(Customer_data['Service'])))
            print("\n-Average Service Time of Customers : "+str(Avg_Service_Time))

            Avg_Inter_Arrival_Time = np.array(round(np.mean(Customer_data['Inter-Arrival'])))
            print("\n-Average Inter-Arrival Time of Customers : "+str(Avg_Inter_Arrival_Time))

            Avg_Turn_Around_Time = np.array(round(np.mean(Customer_data['TurnAround'])))
            print("\n-Average Turn Around Time of Customers : "+str(Avg_Turn_Around_Time))

            Avg_Wait_Time = np.array(round(np.mean(Customer_data['WaitTime'])))
            print("\n-Average Wait Time of Customers   : "+str(Avg_Wait_Time))

            Avg_Response_Time = np.array(round(np.mean(Customer_data['ResponseTime'])))
            print("\n-Average Response Time of Customers : "+str(Avg_Response_Time)+"\n")
        elif(day == 2):
            print("\n\t\t\t\t\tCUSTOMER RECORD HISTORY\n")
            Customer_data = pd.read_csv('Day2.csv')
            print(Customer_data)

            print("\nSimulating Customer Details: \n____________________________")
            Avg_Arrival_Time = np.array(round(np.mean(Customer_data['Arrival'])))
            print("\n-Average Arrival Time of Customers : "+str(Avg_Arrival_Time))

            Avg_Service_Time = np.array(round(np.mean(Customer_data['Service'])))
            print("\n-Average Service Time of Customers : "+str(Avg_Service_Time))

            Avg_Inter_Arrival_Time = np.array(round(np.mean(Customer_data['Inter-Arrival'])))
            print("\n-Average Inter-Arrival Time of Customers : "+str(Avg_Inter_Arrival_Time))

            Avg_Turn_Around_Time = np.array(round(np.mean(Customer_data['TurnAround'])))
            print("\n-Average Turn Around Time of Customers : "+str(Avg_Turn_Around_Time))

            Avg_Wait_Time = np.array(round(np.mean(Customer_data['WaitTime'])))
            print("\n-Average Wait Time of Customers   : "+str(Avg_Wait_Time))

            Avg_Response_Time = np.array(round(np.mean(Customer_data['ResponseTime'])))
            print("\n-Average Response Time of Customers : "+str(Avg_Response_Time)+"\n")
        elif(day == 3):
            print("\n\t\t\t\t\tCUSTOMER RECORD HISTORY\n")
            Customer_data = pd.read_csv('Day3.csv')
            print(Customer_data)

            print("\nSimulating Customer Details: \n____________________________")
            Avg_Arrival_Time = np.array(round(np.mean(Customer_data['Arrival'])))
            print("\n-Average Arrival Time of Customers : "+str(Avg_Arrival_Time))

            Avg_Service_Time = np.array(round(np.mean(Customer_data['Service'])))
            print("\n-Average Service Time of Customers : "+str(Avg_Service_Time))

            Avg_Inter_Arrival_Time = np.array(round(np.mean(Customer_data['Inter-Arrival'])))
            print("\n-Average Inter-Arrival Time of Customers : "+str(Avg_Inter_Arrival_Time))

            Avg_Turn_Around_Time = np.array(round(np.mean(Customer_data['TurnAround'])))
            print("\n-Average Turn Around Time of Customers : "+str(Avg_Turn_Around_Time))

            Avg_Wait_Time = np.array(round(np.mean(Customer_data['WaitTime'])))
            print("\n-Average Wait Time of Customers   : "+str(Avg_Wait_Time))

            Avg_Response_Time = np.array(round(np.mean(Customer_data['ResponseTime'])))
            print("\n-Average Response Time of Customers : "+str(Avg_Response_Time)+"\n")
        else:
            print("\nSorry, We only have 3 days record\n__________________________________\n")

    # SIMULATING QUEUEING MODEL DETAILS
    # ________________________________

    elif (user == predicted[1] or user== upp[1]):
        ask = input("\nWhat you wanna simulate from this queuing system?\n_________________________________________________\n")
        possibilities = ['all', 'mean wait time in the system','average wait time in the system', 'mean wait time in the queue','average wait time in the queue','mean number of customers in the system','average number of customers in the system','mean number of customers in the queue','average number of customers in the queue','w','l','wq','lq' ]
        upp_case = [i.upper() for a,i in enumerate(possibilities)]
        
        # in our case, there are 4 servers
        c=4
        if(ask == possibilities[0]): # if user wants all record 
            Arrival = 1/7.466667 # lambda
            Service = 1/8.946666667     # meu
            p= Arrival/(c*Service)
            Po= 1/((1+(c*p)+(((c*p)**2)/2)+(((c*p)**3)/6))+(((c*p)**4)/(24*(1-p))))
            # Mean Number of Customers In The Queue
            Lq = (Po*((Arrival/Service)**4)*p)/(24*((1-p)**2))
            print("\n -Mean Number Of Customers In The Queue(Lq): "+str(Lq)+ "\n")
            # Mean Wait time In The Queue
            Wq = Lq/Arrival
            print("\n -Mean Wait Time In The Queue(Wq): "+str(Wq)+"\n")
            # Mean Wait time In The System
            W = Wq + (1/Service)
            print("\n -Mean Wait Time In The System(W): "+str(W)+"\n")
            # Mean Number of Customers In The System
            L = Arrival*W
            print("\n -Mean Number Of Customers In The System(L): "+str(L)+"\n")


        elif(ask ==possibilities[1] or ask==possibilities[2] or ask==possibilities[-4]): # If user wants to calculate only mean wait time in the system
            Arrival = 1/7.466667 # lambda 
            Service = 1/8.946666667 # meu
            p= Arrival/(c*Service)
            Po= 1/((1+(c*p)+(((c*p)**2)/2)+(((c*p)**3)/6))+(((c*p)**4)/(24*(1-p))))
            Lq = (Po*((Arrival/Service)**4)*p)/(24*((1-p)**2))
            Wq = Lq/Arrival
            # Mean Wait Time In The System
            W = Wq + (1/Service)
            print("\n -Mean Wait Time In The System(W): "+str(W)+"\n")
        elif(ask ==possibilities[3] or ask==possibilities[4] or ask == possibilities[-2]): # If user wants to calculate only mean wait time in the queue
            Arrival = 1/7.466667 # lambda 
            Service = 1/8.946666667 # meu
            p= Arrival/(c*Service)
            Po= 1/((1+(c*p)+(((c*p)**2)/2)+(((c*p)**3)/6))+(((c*p)**4)/(24*(1-p))))
            Lq = (Po*((Arrival/Service)**4)*p)/(24*((1-p)**2))
            # Mean Wait Time In The Queue
            Wq = Lq/Arrival
            print("\n -Mean Wait Time In The Queue(Wq): "+str(Wq)+"\n")
        elif(ask ==possibilities[5] or ask==possibilities[6] or ask==possibilities[-3]): # If user wants to calculate only mean number of customers in the system
            Arrival = 1/7.466667 # lambda
            Service = 1/8.946666667 # meu
            p= Arrival/(c*Service)
            Po= 1/((1+(c*p)+(((c*p)**2)/2)+(((c*p)**3)/6))+(((c*p)**4)/(24*(1-p))))
            Lq = (Po*((Arrival/Service)**4)*p)/(24*((1-p)**2))
            Wq = Lq/Arrival
            W = Wq + (1/Service)
            # Mean Number of Customers In The System
            L = Arrival*W
            print("\n -Mean Number Of Customers In The System(L): "+str(L)+"\n")
        elif(ask ==possibilities[7] or ask==possibilities[8] or ask == possibilities[-1]): # If user wants to calculate only mean number of customers in the queue
            Arrival = 1/7.466667 # lambda
            Service = 1/8.946666667 # meu
            p= Arrival/(c*Service)
            Po= 1/((1+(c*p)+(((c*p)**2)/2)+(((c*p)**3)/6))+(((c*p)**4)/(24*(1-p))))
            Lq = (Po*((Arrival/Service)**4)*p)/(24*((1-p)**2))
            Wq = Lq/Arrival
            W = Wq + (1/Service)
            L = Arrival*W
            # Mean Number of Customers In The Queue
            Lq = L - (c*p)
            print("\n -Mean Number Of Customers In The Queue(Lq): "+str(Lq)+"\n")
        else:
            print("Can not recognize")


    else:
        print("\nCan not recognize :(\n_____________________\n")

# For Analysis 
# ____________

elif(start== 'Analyze' or start=='ANALYZE' or start=='analyze'):
    plot_time = ['arrival','service','turn around','wait','response']
    plot_time_upp = [i.upper() for a,i in enumerate(plot_time)]
    print("\nFollowing are the available types in which you can analyze customer record:\n_____________________________________________________________\n\n",plot_time)
    plot_ask=input("\nwith respect to which time you wanna analyze customer interaction?\n__________________________________________________________________\n")
    if(plot_ask==plot_time[0] or plot_ask==plot_time_upp==[0]):
        day= int(input("\nWe have 3 days Analysis of Customers, which day you wanna see? \n"))
        if(day == 1):
            # Day-1 Analysis
            day1= pd.read_csv('day1.csv')
            # Customer Interaction With Respect To Arrival Time
            customer_no =np.array(day1['Case#'])
            Arrival_time=np.array(day1['Arrival'])
            plt.plot(customer_no,Arrival_time, color='purple')
            plt.scatter(customer_no,Arrival_time,color='black')
            plt.xlabel("Customers")
            plt.ylabel("Arrival Time")
            plt.title("Customer Analysis With Respect To Arrival Time")
            plt.show()
        elif(day == 2):
            # Day-2 Analysis
            day2= pd.read_csv('day2.csv')
            # Customer Interaction With Respect To Arrival Time
            customer_no =np.array(day2['Case#'])
            Arrival_time=np.array(day2['Arrival'])
            plt.plot(customer_no,Arrival_time, color='purple')
            plt.scatter(customer_no,Arrival_time,color='black')
            plt.xlabel("Customers")
            plt.ylabel("Arrival Time")
            plt.title("Customer Analysis With Respect To Arrival Time")
            plt.show()
        
        elif(day == 3):
            # Day-3 Analysis
            day3= pd.read_csv('day3.csv')
            # Customer Interaction With Respect To Arrival Time
            customer_no =np.array(day3['Case#'])
            Arrival_time=np.array(day3['Arrival'])
            plt.plot(customer_no,Arrival_time, color='purple')
            plt.scatter(customer_no,Arrival_time,color='black')
            plt.xlabel("Customers")
            plt.ylabel("Arrival Time")
            plt.title("Customer Analysis With Respect To Arrival Time")
            plt.show()
        
        else:
            print("\nSorry! We Have Only 3 Days Record\n_________________________________\n")
    elif(plot_ask == plot_time[1] or plot_ask == plot_time_upp[1]):
        day= int(input("\nWe have 3 days Analysis of Customers, which day you wanna see? \n"))
        if(day == 1):
            # Day-1 Analysis
            day1= pd.read_csv('day1.csv')
            # Customer Interaction With Respect To Service Time
            customer_no =np.array(day1['Case#'])
            Service_time=np.array(day1['Service'])
            plt.plot(customer_no,Service_time, color='purple')
            plt.scatter(customer_no,Service_time,color='black')
            plt.xlabel("Customers")
            plt.ylabel("Service Time")
            plt.title("Customer Analysis With Respect To Service Time")
            plt.show()
        elif(day == 2):
            # Day-2 Analysis
            day2= pd.read_csv('day2.csv')
            # Customer Interaction With Respect To Service Time
            customer_no =np.array(day2['Case#'])
            Service_time=np.array(day2['Service'])
            plt.plot(customer_no,Service_time, color='purple')
            plt.scatter(customer_no,Service_time,color='black')
            plt.xlabel("Customers")
            plt.ylabel("Service Time")
            plt.title("Customer Analysis With Respect To Service Time")
            plt.show()
        
        elif(day == 3):
            # Day-3 Analysis
            day3= pd.read_csv('day3.csv')
            # Customer Interaction With Respect To Service Time
            customer_no =np.array(day3['Case#'])
            Service_time=np.array(day3['Service'])
            plt.plot(customer_no,Service_time, color='purple')
            plt.scatter(customer_no,Service_time,color='black')
            plt.xlabel("Customers")
            plt.ylabel("Service Time")
            plt.title("Customer Analysis With Respect To Service Time")
            plt.show()
    elif(plot_ask == plot_time[2] or plot_ask == plot_time_upp[2]):
        day= int(input("\nWe have 3 days Analysis of Customers, which day you wanna see? \n"))
        if(day == 1):
            # Day-1 Analysis
            day1= pd.read_csv('day1.csv')
            # Customer Interaction With Respect to Turn Around Time
            customer_no =np.array(day1['Case#'])
            Turn_Around_time=np.array(day1['TurnAround'])
            plt.plot(customer_no,Turn_Around_time, color='purple')
            plt.scatter(customer_no,Turn_Around_time,color='black')
            plt.xlabel("Customers")
            plt.ylabel("Turn Around Time")
            plt.title("Customer Analysis With Respect To Turn Around Time")
            plt.show()
        elif(day == 2):
            # Day-2 Analysis
            day2= pd.read_csv('day2.csv')
            # Customer Interaction With Respect to Turn Around Time
            customer_no =np.array(day2['Case#'])
            Turn_Around_time=np.array(day2['TurnAround'])
            plt.plot(customer_no,Turn_Around_time, color='purple')
            plt.scatter(customer_no,Turn_Around_time,color='black')
            plt.xlabel("Customers")
            plt.ylabel("Turn Around Time")
            plt.title("Customer Analysis With Respect To Turn Around Time")
            plt.show()
        
        elif(day == 3):
            # Day-3 Analysis
            day3= pd.read_csv('day3.csv')
            # Customer Interaction With Respect to Turn Around Time
            customer_no =np.array(day3['Case#'])
            Turn_Around_time=np.array(day3['TurnAround'])
            plt.plot(customer_no,Turn_Around_time, color='purple')
            plt.scatter(customer_no,Turn_Around_time,color='black')
            plt.xlabel("Customers")
            plt.ylabel("Turn Around Time")
            plt.title("Customer Analysis With Respect To Turn Around Time")
            plt.show()
    elif(plot_ask == plot_time[3] or plot_ask == plot_time_upp[3]):
        day= int(input("\nWe have 3 days Analysis of Customers, which day you wanna see? \n"))
        if(day == 1):
            # Day-1 Analysis
            day1= pd.read_csv('day1.csv')
            # Customer Interaction With Respect to Wait Time
            customer_no =np.array(day1['Case#'])
            Wait_time=np.array(day1['WaitTime'])
            plt.plot(customer_no,Wait_time, color='purple')
            plt.scatter(customer_no,Wait_time,color='black')
            plt.xlabel("Customers")
            plt.ylabel("Wait Time")
            plt.title("Customer Analysis With Respect To Wait Time")
            plt.show()
        elif(day == 2):
            # Day-2 Analysis
            day2= pd.read_csv('day2.csv')
            # Customer Interaction With Respect to Wait Time
            customer_no =np.array(day2['Case#'])
            Wait_time=np.array(day2['WaitTime'])
            plt.plot(customer_no,Wait_time, color='purple')
            plt.scatter(customer_no,Wait_time,color='black')
            plt.xlabel("Customers")
            plt.ylabel("Wait Time")
            plt.title("Customer Analysis With Respect To Wait Time")
            plt.show()
        
        elif(day == 3):
            # Day-3 Analysis
            day3= pd.read_csv('day3.csv')
             # Customer Interaction With Respect to Wait Time
            customer_no =np.array(day3['Case#'])
            Wait_time=np.array(day3['WaitTime'])
            plt.plot(customer_no,Wait_time, color='purple')
            plt.scatter(customer_no,Wait_time,color='black')
            plt.xlabel("Customers")
            plt.ylabel("Wait Time")
            plt.title("Customer Analysis With Respect To Wait Time")
            plt.show()
    elif(plot_ask == plot_time[4] or plot_ask == plot_time_upp[4]):
        day= int(input("\nWe have 3 days Analysis of Customers, which day you wanna see? \n"))
        if(day == 1):
            # Day-1 Analysis
            day1= pd.read_csv('day1.csv')
            # Customer Interaction With Respect to Response Time
            customer_no =np.array(day1['Case#'])
            Response_time=np.array(day1['ResponseTime'])
            plt.plot(customer_no,Response_time, color='purple')
            plt.scatter(customer_no,Response_time,color='black')
            plt.xlabel("Customers")
            plt.ylabel("Response Time")
            plt.title("Customer Analysis With Respect To Response Time")
            plt.show()
        elif(day == 2):
            # Day-2 Analysis
            day2= pd.read_csv('day2.csv')
            # Customer Interaction With Respect to Response Time
            customer_no =np.array(day2['Case#'])
            Response_time=np.array(day2['ResponseTime'])
            plt.plot(customer_no,Response_time, color='purple')
            plt.scatter(customer_no,Response_time,color='black')
            plt.xlabel("Customers")
            plt.ylabel("Response Time")
            plt.title("Customer Analysis With Respect To Response Time")
            plt.show()
        
        elif(day == 3):
            # Day-3 Analysis
            day3= pd.read_csv('day3.csv')
            # Customer Interaction With Respect to Response Time
            customer_no =np.array(day3['Case#'])
            Response_time=np.array(day3['ResponseTime'])
            plt.plot(customer_no,Response_time, color='purple')
            plt.scatter(customer_no,Response_time,color='black')
            plt.xlabel("Customers")
            plt.ylabel("Response Time")
            plt.title("Customer Analysis With Respect To Response Time")
            plt.show()
        
        else:
            print("\nSorry! We Have Only 3 Days Record\n_________________________________\n")

    else:
        print("\nSorry! We are not able to plot\n______________________________\n")
else:
    print("\nSorry!, You can just analyze or simulate the record.\n____________________________________________________\n")
