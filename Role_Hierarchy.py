
roles ={}
RH=['CEO','COO','CTO','Sr Product Eng Manager','Sr Product Marketing Manager','Director of Technology','Manager - Engineering','Manager - Marketing', 'Technical Architect','Devops','Developer','Tester','Marketing Analyst','Marketing Executive']
user_dict={}
user_list=[]
boss=['CEO','COO','CTO','Sr Product Eng Manager','Sr Product Marketing Manager','Director of Technology','Manager - Engineering','Manager - Marketing']
sub_roles=[['COO','CTO'],['Sr Product Eng Manager','Sr Product Marketing Manager'],['Director of Technology'],['Manager - Engineering'],['Manager - Marketing'],['Technical Architect'],['Devops','Developer','Tester'],['Marketing Analyst','Marketing Executive']]     
heigt_hierarcy=[['CEO'],['COO','CTO'], ['Sr Product Eng Manager','Sr Product Marketing Manager','Director of Technology'],['Manager - Engineering','Manager - Marketing','Technical Architect'],['Devops','Developer','Tester','Marketing Analyst','Marketing Executive']]
from_top =[['CEO','COO','Director of Technology','Technical Architect'],['CEO','COO','Sr Product Marketing Manager','Manager - Marketing',['Marketing Analyst','Marketing Executive']],['CEO','COO','Sr Product Eng Manager','Manager - Engineering',['Devops','Developer','Tester']]]

class Role_Hierarchy:

    def create_root(root_role_name):
        
        global roles
        global RH

        if (root_role_name in RH):
            if(root_role_name not in roles ):
                roles[root_role_name]= []
                print("\n *** Operation Success - The Specified Root role added successfully! *** \n")
                return(root_role_name)
            else:
                print("\n *** Operation Failed - The Specified Role alredy Exist! *** \n")
                
                return(Role_Hierarchy.display_roles())
        else:
            res="\n *** Operation Failed - The Specified Role does not exist. Please Select role from existing list *** \n"
            print(res)
            print("Find the List of Valid Roles below : \n")

            return(RH)
        

    def add_sub_role(root_role_name, sub_role):
        global roles
        global user_dict
        global RH

        if(root_role_name not in RH):
            res="\n *** Operation Failed - The Specified Role does not exist. Please Select role from existing list *** \n"
            print(res)
            print("Find the List of Valid Roles below : \n")

            return(RH)

        if(sub_role not in RH):
            res="\n *** Operation Failed - The Specified Role does not exist. Please Select role from existing list *** \n"
            print(res)
            print("Find the List of Valid Roles below : \n")

            return(RH)

        if(root_role_name not in user_dict):
            user_dict[root_role_name]=[]

        if(sub_role not in user_dict):
            user_dict[sub_role]=[]
        else:
            res="\n *** Operation Failed - The Entred Sub Role - '"+sub_role+"', alredy Exist *** "
            print(res)
            return(Role_Hierarchy.display_roles())

        if(root_role_name in roles.keys() ):
            sub_list= (roles[root_role_name])
            if(sub_role not in sub_list):
                sub_list.append(sub_role)
                roles[root_role_name]=sub_list
            else:
                print("\n *** Operation Failed - The Entred Root Role - '"+sub_role+"', alredy Exist *** ")
                return(Role_Hierarchy.display_roles())
        else:
            roles[root_role_name]= [sub_role]

        
        
        print("\n *** Operation Success - Root role '"+root_role_name+"' and sub role '"+sub_role+"' added successfully! *** ")

        return(Role_Hierarchy.display_roles())

    def delete_role(transfer_role_name, del_role):

        global roles
        global RH
        global user_dict
        global user_list
        global heigt_hierarcy
        global from_top
        global sub_roles
        global boss

            
        if(del_role not in user_dict):
            print("\n *** Operation Failed *** \n")
            res="The Role entred for deleting - '"+del_role+"', does not Exist"
            print(res)
            return(Role_Hierarchy.display_roles())
        if(transfer_role_name not in user_dict):
            print("\n *** Operation Failed *** \n")
            res="The Role entred for transfering - '"+transfer_role_name+"', does not Exist"
            print(res)
            return(Role_Hierarchy.display_roles())
        if(transfer_role_name in RH):
            RH.remove(transfer_role_name)

        for i in range(0,len(RH)):
            if(RH[i]==del_role):
                RH.pop(i)
                RH.insert(i,transfer_role_name)

        for key, value in roles.items():
            if(key==del_role):
                roles[transfer_role_name] =roles.pop(key)
            
            for i in range(0,len(value)):
                if(value[i]==transfer_role_name):
                    value.remove(transfer_role_name)
  
            for i in range(0,len(value)):
                if(value[i]==del_role):
                    value.pop(i)
                    value.insert(i,transfer_role_name)
        for i in boss:
            if(i==transfer_role_name):
                boss.remove(transfer_role_name)

        for i in range(0,len(boss)):
            
            if(boss[i]==del_role):
                boss.pop(i)
                boss.insert(i,transfer_role_name)
        
        for i in sub_roles:
            for j in i:
                if(j==transfer_role_name):
                    i.remove(j)
        
        for i in sub_roles:
            for j in i:
                if(j==del_role):
                    i.remove(j)
                    i.append(transfer_role_name)

        keys = user_dict.keys()
        ks=[]
        for i in keys:
            ks.append(i)

        usr_lst = user_dict[transfer_role_name]
        sam_lst= user_list
        for i in usr_lst:
            for j in sam_lst:
                if(i==j):
                    sam_lst.remove(i)
        user_list=sam_lst
        for key in ks:
            if(key==transfer_role_name):
                user_dict.pop(key)

        for key in ks:
            if(key==del_role):
                user_dict[transfer_role_name] =user_dict.pop(key)
      
        
        for i in heigt_hierarcy:
            for j in i :
                if (j==del_role):
                    index = i.index(j)
                    i[index]= transfer_role_name
                    
                elif(j==transfer_role_name):
                    i.remove(j)
                    
        for i in from_top:
            for j in i :
                if(type(j) is list):
                    for k in j :
                        if (k==transfer_role_name):
                            j.remove(k)
                        elif (k==del_role):
                            index = j.index(k)
                            j[index]= transfer_role_name
                else:
                    if (j==del_role):
                        index = i.index(j)
                        i[index]= transfer_role_name
                    elif(j==transfer_role_name):
                        i.remove(j)
        for i in boss:
            if(i==del_role):
                index = boss.index(i)
                boss[index]= transfer_role_name
            elif(i==transfer_role_name):
                boss.remove(i)
        

        return(Role_Hierarchy.display_roles())
        
    
    def add_user(role_name, user):
        
        user = str(user).capitalize()

        if(user not in user_list):
            if(role_name not in user_dict):
                print("\n *** Operation Failed - Specified Role does not exist. *** ")
                return(Role_Hierarchy.display_roles())
            else :
                user_list.append(user)
                list_1 = user_dict[role_name]
                list_1.append(user)
                user_dict[role_name]=list_1
        else :
            for k, v in user_dict.items():
                if(user in v):
                    print("\n *** Operation Failed *** \n")
                    res= ("Specified User alredy exist with the Role - "+k)
                    return(res)
        
        print("\n *** Operation Success - Specified User added to the mentioned Role successfully! *** \n")
        return(Role_Hierarchy.display_users())
        
    def display_users():
        va=""
        for i in RH:
            for key, values in user_dict.items():
                if(key==i):
                    for j in values:
                        va+=j+" - "+key+".\n"
        report =va.strip()[:len(va.strip())-1]+'.'
        return (report)

    def display_user_subuser():

        global roles
        global RH
        global user_dict
        res=""
        role=[]
        sub_role=[]
        user_role=[]
        user_name=[]
        for k,v in roles.items():
            role.append(k)
            sub_role.append(v)
        for i in RH:
            for k,v in user_dict.items():
                if(k==i):
                    user_role.append(k)
                    user_name.append(v)

        for i in range(0,len(user_role)):
            user_n=[]
            sub_user_n = []
            if(user_role[i] in role):
                if(len(user_name[i])>0):
                    for m in user_name[i]:
                        user_n.append(m)
                if(len(user_name[i])>0):
                    index_r= role.index(user_role[i])
                    for j in sub_role[index_r]:
                        indx= user_role.index(j)
                        if(len(user_name[indx])>0):
                            for m in user_name[indx]:
                                sub_user_n.append(m)
                        if(j in role):
                            indi = role.index(j)
                            r=sub_role[indi]
                            for k in r:
                                indis = user_role.index(k)
                                if(len(user_name[indis])>0):
                                    for m in user_name[indis]:
                                        sub_user_n.append(m)  

                sub_user=set(sub_user_n)
                sub_user_n=[]
                for i in RH:
                    for j in sub_user:
                        for k in range(0,len(user_name)):
                            if(j in user_name[k]):
                                rol= user_role[k]
                                if(rol==i):
                                    sub_user_n.append(j)


                if(len(user_n)>0):
                    if(len(sub_user_n)!=0):
                        rs=""
                        for i in sub_user_n:
                            rs+=i+', '
                        if(len(user_n)>1):
                            r=""
                            for i in user_n:
                                r=i
                                res+=(r+" - "+rs[:len(rs)-2]+'.\n')
                        else:
                            r=""
                            for i in user_n:
                                r=i
                                res+=(r+" - "+rs[:len(rs)-2]+'.\n')

                    else:
                        if(len(user_n)>1):
                            r=""
                            for i in user_n:
                                r=i
                                res+=(r+" - \n")
                        else:
                            r=""
                            for i in user_n:
                                r=i
                                res+=(r+" - \n")
                        

        for i in sub_role:
            for j in i:
                if(j not in role):
                    index = user_role.index(j)
                    if(len(user_name[index])>0):
                        for m in user_name[index]:
                            res+=(m+' - \n')
        return(res[:len(res)-1])    

    def delete_user(del_user):

        global user_dict
        global user_list

        del_user = str(del_user).capitalize()

        if(len(user_list)==0):
            print("\n*** Operation Failed - There are no Users added to the Roles yet *** ")
            return("")

        if(del_user not in user_list):
            res="\n*** Operation Failed - The Specified User is not in the list, please check for Spelling\n\nThe Existing Users are mentioned below,"
            print(res)
            return(Role_Hierarchy.display_users())
        else:
            for key, value in user_dict.items():
                if(del_user in value):
                    value.remove(del_user)

            user_list.remove(del_user)
            res="\n*** Operation Success - The Specified User deleted from the list. *** "
            print(res)
            return(Role_Hierarchy.display_user_subuser())
        
    def num_of_user(user_name):

        global user_dict
        global from_top

        user_name = str(user_name).capitalize()

        if(user_name not in user_list):
            res="\n*** Operation Failed - The Specified User is not in the list, please check for Spelling\n\nThe Existing Users are mentioned below,"
            print(res)
            return(Role_Hierarchy.display_users())
        else:
            user_role_list=[]
            user_name_list=[]
            for i in RH:
                for k,v in user_dict.items():
                    if(k==i):
                        user_role_list.append(k)
                        user_name_list.append(v)

            for i in range(0,len(user_name_list)):
                if(user_name in user_name_list[i]):
                    user_role = user_role_list[i]

            count=0
            indi = 0
            for i in range(0,len(from_top)):
                for j in from_top[i]:
                    if(type(j) is list):
                        if(user_role in j):
                            indi = i
                            break
                    else :
                        if(j==user_role):
                            indi =i
                            break
            lst = from_top[indi]
            for i in lst :
                if(type(i) is list):
                    if(user_role in i):
                        break
                else:
                    if(i==user_role):
                        break
                    else:
                      
                        count_1 = len(user_name_list[user_role_list.index(i)])
                        count+=count_1

            print("\n")
            report = "Number of Users from top : "+str(count)
            return(report)

    def height_hierarchy():
        global heigt_hierarcy
        
        global roles
        
        res=[]
        for i in range(0,len(heigt_hierarcy)):
            for k,  v in roles.items():
                for j in v :
                    if(j in heigt_hierarcy[i]):
                        res.append(i)
        
        height = int(max(res)) + 1

        print("\n")
        report = "Height - "+str(height)
        return(report)

    def common_boss(user_1,user_2):
        global roles
        global RH
        global user_dict
        global user_list
        global boss
        global sub_roles
        
        user_1= str(user_1).capitalize()
        user_2= str(user_2).capitalize()
       
        if(user_1 not in user_list):
            res="\n*** Operation Failed - The Specified User '"+user_1+"' is not in the list, please check for Spelling\n\nThe Existing Users are mentioned below,"
            print(res)
            return(Role_Hierarchy.display_users())
        elif(user_2 not in user_list):
            res="\n*** Operation Failed - The Specified User '"+user_2+"' is not in the list, please check for Spelling\n\nThe Existing Users are mentioned below,"
            print(res)
            return(Role_Hierarchy.display_users())
        else:
            role=[]
            sub_role=[]
            user_role=[]
            user_name=[]
            
            for i in RH:
                for k,v in roles.items():
                    if(k==i):
                        role.append(k)
                        sub_role.append(v)
            
                for k,v in user_dict.items():
                    if(k==i):
                        if(len(user_dict[k])!=0):
                            user_role.append(k)
                            user_name.append(v) 

            for i in range(0,len(user_role)):
                if (user_1 in user_name[i]):
                    user_1_role= user_role[i]
                if (user_2 in user_name[i]):
                    user_2_role= user_role[i]
                    
            user_1_boss = [user_1_role]
            user_2_boss = [user_2_role]

            def comm_boss(user_1_role,user_2_role):
                
                for i in range(0, len(sub_role)):
                    if(user_1_role in sub_role[i]):
                        user_1_boss.append(role[i])
                    if(user_2_role in sub_role[i]):
                        user_2_boss.append(role[i])

                u1b=[]
                u2b=[]
                for i in user_1_boss:
                    if(i in user_role):
                        u1b.append(i)

                for i in user_2_boss:
                    if(i in user_role):
                        u2b.append(i)

                comm= set(u1b).intersection(u2b)

                if(len(comm)>0):
                    r_l=[]
                    for i in RH:
                        for j in comm:
                            if(i==j):
                                r_l.append(j)
                    rol=r_l[0]
                    user_name_list=[]
                    if(rol in user_role ):
                        user_name_list = user_name[user_role.index(str(rol))]
                    res=""
                    if(len(user_name_list)>0):
                        for i in user_name_list:
                            res+=i+", "
                        res=res[:len(res)-2]+".\nRole - "+rol
                        return(res)
                    else:
                        user_1_role=user_1_boss[-1]
                        user_2_role=user_2_boss[-1]

                        user_1_boss.remove(user_1_boss[-1])
                        user_2_boss.remove(user_2_boss[-1])
                        return(comm_boss(user_1_role, user_2_role))
                else:
                    user_1_role=user_1_boss[-1]
                    user_2_role=user_2_boss[-1]
   
                    user_1_boss.remove(user_1_boss[-1])
                    user_2_boss.remove(user_2_boss[-1])
                    return(comm_boss(user_1_role, user_2_role))
  
            if(user_1_role=='CEO' or user_2_role=='CEO'):
                if(user_1_role=='CEO'):
                    print("\n *** Operation Failed *** \n")
                    report = user_1+" is the CEO, he reports to no one"
                else:
                    print("\n *** Operation Failed *** \n")
                    report = user_2+" is the CEO, he reports to no one"
            else:
                comm_bosses=comm_boss(user_1_role, user_2_role)
                print("\n")
                report = "Top Most Common Boss : "+str(comm_bosses)+"."

            return report  

    def display_roles():
        global roles
        global RH
        res =[]
        res_dict=[]
        for key, value in roles.items() :
            res_dict.append(key)
            for v in value:
                res_dict.append(v)
        for role in RH:
            for i in res_dict:
                if(i==role and (i not in res)):
                    res.append(i)
        va=""
        for i in res:
            va+=i+", "
        report ="\nExisting Role Hierarchy :- "+va.strip()[:len(va.strip())-1]+'.'
        return(report)

flag = True

while flag :
    print("\n-------------------------------------------------------------")
    print("\t--x-- To STOP the operation, type 'quit' --x--")
    print("--------------------------------------------------------------")
    option_1 = "\t*  To create the root role, type ----------- 1"
    option_2 = "\t*  To add sub role to the root role, type -- 2"
    option_3 = "\t*  To delete the role, type ---------------- 3"
    option_4 = "\t*  To add User to the role, type ----------- 4"
    option_5 = "\t*  To display users, type ------------------ 5"
    option_6 = "\t*  To display Users and sub-users, type ---- 6"
    option_7 = "\t*  To delete the user, type ---------------- 7"
    option_8 = "\t*  To find number of user from top, type --- 8"
    option_9 = "\t*  To find height of role hierarchy, type -- 9"
    option_10 = "\t*  To find the most common Boss, type ------ 10\n"

    print(option_1)
    print(option_2)
    print(option_3)
    print(option_4)
    print(option_5)
    print(option_6)
    print(option_7)
    print(option_8)
    print(option_9)
    print(option_10)
    
    option = input("     Enter the option number of the operation to be performed - ")
    

    print("\n     The selected option is - ",option)
    if(str(option).lower()=='quit'):
        flag = False
    elif(str(option)=='1'):
        print("\n--------------------------------------------------------------")
        print("\tOperation - To create the root role")
        print("--------------------------------------------------------------\n")
        root_role_name = input("     Enter the root role name\t: ")
        print(Role_Hierarchy.create_root(root_role_name))

    elif(str(option)=='2'):
        print("\n--------------------------------------------------------------")
        print("\tOperation - To add sub role to the root role")
        print("--------------------------------------------------------------\n")
        
        sub_role = input("     Enter the sub role name\t\t: ")
        report_role_name = input("     Enter reporting to role name\t: ")
        print(Role_Hierarchy.add_sub_role(report_role_name, sub_role))
        
    elif(str(option)=='3'):
        print("\n--------------------------------------------------------------")
        print("\tOperation - To delete the role")
        print("--------------------------------------------------------------\n")
        
        del_role = input("     Enter the role to be deleted : ")
        transfer_role_name = input("     Enter the role to be transferred : ")
        print(Role_Hierarchy.delete_role(transfer_role_name, del_role))
    
    elif(str(option)=='4'):
        print("\n--------------------------------------------------------------")
        print("\tOperation - To add User to the role")
        print("--------------------------------------------------------------\n")
        
        user = input("     Enter User Name : ")
        role_name = input("     Enter role : ")
        print(Role_Hierarchy.add_user(role_name, user))
    
    elif(str(option)=='5'):
        print("\n--------------------------------------------------------------")
        print("\tOperation - To display users")
        print("--------------------------------------------------------------\n")
        print(Role_Hierarchy.display_users())

    elif(str(option)=='6'):
        print("\n--------------------------------------------------------------")
        print("\tOperation - To display Users and sub-users")
        print("--------------------------------------------------------------\n")
        print(Role_Hierarchy.display_user_subuser())

    elif(str(option)=='7'):
        print("\n--------------------------------------------------------------")
        print("\tOperation - To delete the user")
        print("--------------------------------------------------------------\n")

        del_user = input("     Enter User Name to be deleted : ")
        print(Role_Hierarchy.delete_user(del_user))

    elif(str(option)=='8'):
        print("\n--------------------------------------------------------------")
        print("\tOperation - To find number of user from top")
        print("--------------------------------------------------------------\n")

        user_name = input("     Enter the user name : ")
        print(Role_Hierarchy.num_of_user(user_name))

    elif(str(option)=='9'):
        print("\n--------------------------------------------------------------")
        print("\tOperation - To find height of role hierarchy")
        print("--------------------------------------------------------------\n")

        print(Role_Hierarchy.height_hierarchy())
    elif(str(option)=='10'):
        print("\n--------------------------------------------------------------")
        print("\tOperation - To find the most common Boss")
        print("--------------------------------------------------------------\n")
        user_1 = input("     Enter user name 1 : ")
        user_2 = input("     Enter user name 2 : ")
        print(Role_Hierarchy.common_boss(user_1,user_2))
    else:
        print("\n--------------------------------------------------------------")
        print("\t*** Please select the valid option ***")
    