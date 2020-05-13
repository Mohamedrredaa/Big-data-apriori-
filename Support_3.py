
# beginning of the code isa

import pandas as pd
import numpy as np
import os
import itertools
from collections import Counter

#from django.db.models.expressions import Col

data_df = pd.read_csv('Final.csv')

A = data_df['Column37'].values
B = data_df['Column38'].values
C = data_df['Column39'].values
D = data_df['Column40'].values
E = data_df['Column41'].values
F = data_df['Column42'].values
G = data_df['Column43'].values
H = data_df['Column44'].values
I = data_df['Column45'].values
J = data_df['Column46'].values
K = data_df['Column47'].values
L = data_df['Column48'].values
M = data_df['Column49'].values
real_att = {'A':'MINKM30','B': 'MINK3045','C': 'MINK4575', 'D':'MINK7512','E': 'MINK123M','F': 'MINKGEM','G': 'MKOOPKLA','H': 'PWAPART','I': 'PWABEDR','J': 'PWALAND','K': 'PPERSAUT','M': 'PBESAUT'}

columns = [A, B, C, D, E, F, G, H, I, J, K, M]
Columns_Index = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "M"]
All_Combinations = []
Combination_Dictionary = {}
A_white_list,B_white_list,C_white_list,D_white_list,E_white_list = [i for i in range(5822)],[i for i in range(5822)],[i for i in range(5822)],[i for i in range(5822)],[i for i in range(5822)]
F_white_list,G_white_list,H_white_list,I_white_list,J_white_list = [i for i in range(5822)],[i for i in range(5822)],[i for i in range(5822)],[i for i in range(5822)],[i for i in range(5822)]
K_white_list,M_white_list = [i for i in range(5822)],[i for i in range(5822)]
##################### put min support here ########################
#
#
#
#
min_support = float(input("Please enter min support in percentage : "))
min_confidence = float(input("Please enter min confidence in percentage : "))

print("you have entered Min support = {} %, and minConfidence = {} %".format(min_support,min_confidence))
min_confidence /=100
min_support /=100
#
#
#
####################################################################

def Assigning_Values(Row_Slice,Flag_A,Flag_B,Flag_C,Flag_D,Flag_E,Flag_F,Flag_G,Flag_H,Flag_I,Flag_J,Flag_K,Flag_M,input_length,counter):
    global Combination_Dictionary
    x = itertools.combinations(Row_Slice, input_length)

    for m in x:
        c = list(Combination_Dictionary)[counter]
        if Flag_A in c:
            counter +=1
            continue

        elif Flag_B in c:
            counter += 1
            continue

        elif Flag_C in c:
            counter += 1
            continue

        elif Flag_D in c:
            counter += 1
            continue

        elif Flag_E in c:
            counter += 1
            continue

        elif Flag_F in c:
            counter += 1
            continue

        elif Flag_G in c:
            counter += 1
            continue

        elif Flag_H in c:
            counter += 1
            continue

        elif Flag_I in c:
            counter += 1
            continue

        elif Flag_J in c:
            counter += 1
            continue

        elif Flag_K in c:
            counter += 1
            continue

        elif Flag_M in c:
            counter += 1
            continue

        else:
            Combination_Dictionary[c].append(m)
            counter += 1

def Slicing_rows(A,B,C,D,E,F,G,H,I,J,K,M,input_length):
    Flag_A,Flag_B,Flag_C,Flag_D,Flag_E,Flag_F,Flag_G,Flag_H,Flag_I,Flag_J,Flag_K,Flag_M = "S","S","S","S","S","S","S","S","S","S","S","S"
    counter = 0
    c = list(Combination_Dictionary)[counter]
    while len(c) != input_length:
        counter += 1
        c = list(Combination_Dictionary)[counter]

    for i in range(5822):
        Row_Slice = []
        if i in A_white_list:
            Row_Slice.append(A[i])
        else: Flag_A = 'A'

        if i in B_white_list:
            Row_Slice.append(B[i])
        else: Flag_B = 'B'

        if i in C_white_list:
            Row_Slice.append(C[i])
        else:
            Flag_C = 'C'

        if i in D_white_list:
            Row_Slice.append(D[i])
        else:
            Flag_D = 'D'

        if i in E_white_list:
            Row_Slice.append(E[i])
        else:
            Flag_E = 'E'

        if i in F_white_list:
            Row_Slice.append(F[i])
        else:
            Flag_F = 'F'

        if i in G_white_list:
            Row_Slice.append(G[i])
        else:
            Flag_G = 'G'

        if i in H_white_list:
            Row_Slice.append(H[i])
        else:
            Flag_H = 'H'

        if i in I_white_list:
            Row_Slice.append(I[i])
        else:
            Flag_I = 'I'

        if i in J_white_list:
            Row_Slice.append(J[i])
        else:
            Flag_J = 'J'

        if i in K_white_list:
            Row_Slice.append(K[i])
        else:
            Flag_K = 'K'

        if i in M_white_list:
            Row_Slice.append(M[i])
        else:
            Flag_M = 'M'
        Assigning_Values(Row_Slice,Flag_A,Flag_B,Flag_C,Flag_D,Flag_E,Flag_F,Flag_G,Flag_H,Flag_I,Flag_J,Flag_K,Flag_M,input_length,counter)


for L in range(1, len(Columns_Index)+1):
    All_Combinations.append(list(itertools.combinations(Columns_Index, L)))

for i in All_Combinations:
    for j in i:
        Combination_Dictionary[j] = []


List_Values1 = []
List_Values2 = []


for NS in range(1,12):
    if (A_white_list == []) and (B_white_list == []) and (C_white_list == []) and (D_white_list == []) and (E_white_list == []) and (F_white_list == []) and (G_white_list == []) and (H_white_list == []) and (I_white_list == []) and (J_white_list == []) and (K_white_list == []) and (M_white_list == []):
        break
    Slicing_rows(A, B, C, D, E, F, G, H, I, J, K, M, NS)
    A_white_list, B_white_list, C_white_list, D_white_list, E_white_list = [], [], [], [], []
    F_white_list, G_white_list, H_white_list, I_white_list, J_white_list = [], [], [], [], []
    K_white_list, M_white_list = [], []
    for key in Combination_Dictionary.keys():
        if NS == len(key):
            flag = 0
            temp = []
            counter = 0
            tmp = 0
            Above_min = []
            for i in Combination_Dictionary[key]:
                if i in temp:
                    if i in Above_min:
                        for mm in range(len(key)):
                            if key[mm] == 'A':
                                A_white_list.append(counter)

                            if key[mm] == 'B':
                                B_white_list.append(counter)

                            if key[mm] == 'C':
                                C_white_list.append(counter)

                            if key[mm] == 'D':
                                D_white_list.append(counter)

                            if key[mm] == 'E':
                                E_white_list.append(counter)

                            if key[mm] == 'F':
                                F_white_list.append(counter)

                            if key[mm] == 'G':
                                G_white_list.append(counter)

                            if key[mm] == 'H':
                                H_white_list.append(counter)

                            if key[mm] == 'I':
                                I_white_list.append(counter)

                            if key[mm] == 'J':
                                J_white_list.append(counter)

                            if key[mm] == 'K':
                                K_white_list.append(counter)

                            if key[mm] == 'M':
                                M_white_list.append(counter)
                        counter += 1
                    else:
                        counter += 1
                        continue
                else:
                    temp.append(i)
                    tmp = Combination_Dictionary[key].count(i)/5822
                    if tmp > min_support:
                        if flag == 0:
                            List_Values2.append(key)
                            List_Values1.append(key)
                            flag = 1

                        List_Values2.append(tmp)
                        List_Values1.append(i)
                        Above_min.append(i)
                        for mm in range(len(key)):
                            if key[mm] == 'A':
                                A_white_list.append(counter)

                            if key[mm] == 'B':
                                B_white_list.append(counter)

                            if key[mm] == 'C':
                                C_white_list.append(counter)

                            if key[mm] == 'D':
                                D_white_list.append(counter)

                            if key[mm] == 'E':
                                E_white_list.append(counter)

                            if key[mm] == 'F':
                                F_white_list.append(counter)

                            if key[mm] == 'G':
                                G_white_list.append(counter)

                            if key[mm] == 'H':
                                H_white_list.append(counter)

                            if key[mm] == 'I':
                                I_white_list.append(counter)

                            if key[mm] == 'J':
                                J_white_list.append(counter)

                            if key[mm] == 'K':
                                K_white_list.append(counter)

                            if key[mm] == 'M':
                                M_white_list.append(counter)
                        counter += 1
                    else:
                        counter += 1
        else:
            continue





# List of dict maps a tuple to its corresponding support

Fin_out = []

tt = ('MINKM30','MINK3045')
Final_out = []
for i in range(len(List_Values1)):
    if List_Values1[i][0] not in range(0,12):
        tt = List_Values1[i]
        for k in range(len(tt)):
            if tt[k]  == 'A':
                nnn = list(tt)
                nnn[k] = 'MINKM30'
                tt = tuple(nnn)
            elif tt[k] == 'B':
                nnn = list(tt)
                nnn[k] = 'MINK3045'
                tt = tuple(nnn)

            elif tt[k] == 'C':
                nnn = list(tt)
                nnn[k] = 'MINK4575'
                tt = tuple(nnn)

            elif tt[k] == 'D':
                nnn = list(tt)
                nnn[k] = 'MINK7512'
                tt = tuple(nnn)

            elif tt[k] == 'E':
                nnn = list(tt)
                nnn[k] = 'MINK123M'
                tt = tuple(nnn)

            elif tt[k] == 'F':
                nnn = list(tt)
                nnn[k] = 'MINKGEM'
                tt = tuple(nnn)

            elif tt[k] == 'G':
                nnn = list(tt)
                nnn[k] = 'MKOOPKLA'
                tt = tuple(nnn)

            elif tt[k] == 'H':
                nnn = list(tt)
                nnn[k] = 'PWAPART'
                tt = tuple(nnn)

            elif tt[k] == 'I':
                nnn = list(tt)
                nnn[k] = 'PWABEDR'
                tt = tuple(nnn)

            elif tt[k] == 'J':
                nnn = list(tt)
                nnn[k] = 'PWALAND'
                tt = tuple(nnn)

            elif tt[k] == 'K':
                nnn = list(tt)
                nnn[k] = 'PPERSAUT'
                tt = tuple(nnn)

            elif tt[k] == 'M':
                nnn = list(tt)
                nnn[k] = 'PBESAUT'
                tt = tuple(nnn)
        i += 1
        x = (tt,List_Values1[i],List_Values2[i])
        Final_out.append(x)
    else:
        x = (tt,List_Values1[i],List_Values2[i])
        Final_out.append(x)

#for i in Final_out:
#    print(i)
    
nnn = ('A','B')
x = ()

for i in range(len(List_Values1)):

    if List_Values1[i][0] not in range(0,12):
        nnn = List_Values1[i]

    else:
        for mns in range(len(nnn)):
            xxx = nnn[mns].replace(nnn[mns] , real_att[nnn[mns]])
            x = x + (xxx + str('_'+str(List_Values1[i][mns])),)
            #x = x + (nnn[mns] + str(List_Values1[i][mns]),)
        c = (x, float("{:.3f}".format(List_Values2[i]))  )
        Fin_out.append(c)
        x = ()
#for i in Fin_out:
#    print(i)
    

def Retrieve_L1_Support(Fin_out , strr):

    for i in range(len(Fin_out)):
        x =  Fin_out[i][0] 

        if x == (strr,) :
            return float(Fin_out[i][1])
            #continue here 
    return 1
def Retrieve_L2_Support(Fin_out , strr1,strr2):

    for i in range(len(Fin_out)):
        if(len(Fin_out[i][0]) == 2):
            x = Fin_out[i][0]

            if x[0] == strr1 and x[1] == strr2 :
                return float(Fin_out[i][1])
        else:
            continue
    return 0
def Retrieve_L3_Support(Fin_out , strr1,strr2,strr3):
    for i in range(len(Fin_out)):
        if Fin_out[i][0] == strr1 and Fin_out[i][1] == strr2 and Fin_out[i][2]== strr3 :
            return float(Fin_out[i][3])
    return 0
def Retrieve_L4_Support(Fin_out , strr1,strr2,strr3,strr4):
    for i in range(len(Fin_out)):
        if Fin_out[i][0] == strr1 and Fin_out[i][1] == strr2 and Fin_out[i][2]== strr3 and Fin_out[i][3]== strr4:
            return float(Fin_out[i][4])
    return 0
def Retrieve_L5_Support(Fin_out , strr1,strr2,strr3,strr4,strr5):
    for i in range(len(Fin_out)):
        if Fin_out[i][0] == strr1 and Fin_out[i][1] == strr2 and Fin_out[i][2]== strr3 and Fin_out[i][3]== strr4and and Fin_out[i][4]== strr4 and Fin_out[i][5]== strr4:
            return float(Fin_out[i][5])
    return 0
def Retrieve_L6_Support(Fin_out , strr1,strr2,strr3,strr4,strr5,strr6):
    for i in range(len(Fin_out)):
        if Fin_out[i][0] == strr1 and Fin_out[i][1] == strr2 and Fin_out[i][2]== strr3 and  Fin_out[i][3]== strr4 and Fin_out[i][4]== strr4 and Fin_out[i][5]== strr4 and Fin_out[i][6]== strr4:
            return float(Fin_out[i][6])
    return 0
def Retrieve_L7_Support(Fin_out , strr1,strr2,strr3,strr4,strr5,strr6,strr7):
    for i in range(len(Fin_out)):
        if Fin_out[i][0] == strr1 and Fin_out[i][1] == strr2 and Fin_out[i][2]== strr3 and  Fin_out[i][3]== strr4 and Fin_out[i][4]== strr4 and Fin_out[i][5]== strr4 and Fin_out[i][6]== strr4:
            return float(Fin_out[i][6])
    return 0
def Retrieve_L8_Support(Fin_out , strr1,strr2,strr3,strr4,strr5,strr6,strr7,strr8):
    for i in range(len(Fin_out)):
        if Fin_out[i][0] == strr1 and Fin_out[i][1] == strr2 and Fin_out[i][2]== strr3 and  Fin_out[i][3]== strr4 and Fin_out[i][4]== strr4 and Fin_out[i][5]== strr4 and Fin_out[i][6]== strr4:
            return float(Fin_out[i][6])
    return 0
def Retrieve_L9_Support(Fin_out , strr1,strr2,strr3,strr4,strr5,strr6,strr7,strr8,strr9):
    for i in range(len(Fin_out)):
        if Fin_out[i][0] == strr1 and Fin_out[i][1] == strr2 and Fin_out[i][2]== strr3 and  Fin_out[i][3]== strr4 and Fin_out[i][4]== strr4 and Fin_out[i][5]== strr4 and Fin_out[i][6]== strr4:
            return float(Fin_out[i][6])
    return 0
def Retrieve_L10_Support(Fin_out , strr1,strr2,strr3,strr4,strr5,strr6,strr7,strr8,strr9,strr10):
    for i in range(len(Fin_out)):
        if Fin_out[i][0] == strr1 and Fin_out[i][1] == strr2 and Fin_out[i][2]== strr3 and  Fin_out[i][3]== strr4 and Fin_out[i][4]== strr4 and Fin_out[i][5]== strr4 and Fin_out[i][6]== strr4:
            return float(Fin_out[i][6])
    return 0
def Retrieve_L11_Support(Fin_out , strr1,strr2,strr3,strr4,strr5,strr6,strr7,strr8,strr9,strr10,strr11):
    for i in range(len(Fin_out)):
        if Fin_out[i][0] == strr1 and Fin_out[i][1] == strr2 and Fin_out[i][2]== strr3 and  Fin_out[i][3]== strr4 and Fin_out[i][4]== strr4 and Fin_out[i][5]== strr4 and Fin_out[i][6]== strr4:
            return float(Fin_out[i][6])
    return 0
def Retrieve_L12_Support(Fin_out , strr1,strr2,strr3,strr4,strr5,strr6,strr7,strr8,strr9,strr10,strr11,strr12):
    for i in range(len(Fin_out)):
        if Fin_out[i][0] == strr1 and Fin_out[i][1] == strr2 and Fin_out[i][2]== strr3 and  Fin_out[i][3]== strr4 and Fin_out[i][4]== strr5 and Fin_out[i][5]== strr6 and Fin_out[i][6]== strr7:
            return float(Fin_out[i][6])
    return 0



final_Out = []
def Calculate_All(Fin_out):
    global min_support
    global min_confidence

    for i in Fin_out:
        #print(i)
        attributes = i[0]
        if len(i[0] )==1:
            print("{} , support = {}".format(attributes ,i[1]))
            final_Out.append(i)
            print('---------------------------------------------------------------------------------------------------')#level 2       #level 2 #level 1
        elif len(i[0] )==2:
            #print(i[0])
            confidence = []
            support   = float(i[1])
            support_firstAtt = Retrieve_L1_Support(Fin_out , attributes[0])
            support_secondAtt = Retrieve_L1_Support(Fin_out , attributes[1])
            if support_firstAtt !=0:
                confidence.append(float("{:.3f}".format(support/support_firstAtt) ))
            else:
                confidence.append(0)
            if support_secondAtt !=0:
                confidence.append(float("{:.3f}".format(support/support_secondAtt))) 
            else:
                confidence.append(0)
            if  confidence[0] >= min_confidence:
                lift = float("{:.3f}".format(support/(support_firstAtt*support_secondAtt))) 
                lev  = float("{:.3f}".format(support-(support_firstAtt*support_secondAtt))) 
                print("{} ==============>{} support={} ,Confidence={} , lift = {},leverage={} ".format(attributes[0] , attributes[1],support , confidence[0],lift,lev))
                final_Out.append((attributes[0],attributes[1] , support))
                print('---------------------------------------------------------------------------------------------------')
            if confidence[1] >= min_confidence:
                lift = float("{:.3f}".format(support/(support_firstAtt*support_secondAtt))) 
                lev  = float("{:.3f}".format(support-(support_firstAtt*support_secondAtt))) 
                print("{} ==============>{} support={} ,Confidence={} , lift = {},leverage={} ".format(attributes[1],attributes[0],support , confidence[0],lift,lev))
                final_Out.append((attributes[1],attributes[0], support))
                print('---------------------------------------------------------------------------------------------------')
            else:
                continue
        elif len(i[0] )==3:

            #print("length :i[0] == 3 = "+str(i[0]) )
            firstAtt = i[0][0]
            secondAtt = i[0][1]
            thirdAtt = i[0][2]
            #forthAtt = attributes[3]
            support   = float(i[1])
            support_firstAtt  = Retrieve_L1_Support(Fin_out , attributes[0])
            support_secondAtt = Retrieve_L1_Support(Fin_out , attributes[1])
            support_thirdAtt  = Retrieve_L1_Support(Fin_out , attributes[2])

            support_first2ndAtt  = Retrieve_L2_Support(Fin_out , attributes[0],attributes[1])
            support_second3rdAtt = Retrieve_L2_Support(Fin_out , attributes[1],attributes[2])
            support_third1stAtt  = Retrieve_L2_Support(Fin_out , attributes[2],attributes[0])

            if support_firstAtt !=0:
                confidence.append(float("{:.3f}".format(support/support_firstAtt) ))   #A--->B,C
            else:
                confidence.append(0)
            if support_secondAtt !=0:
                confidence.append(float("{:.3f}".format(support/support_secondAtt)))    #B--->A,C
            else:
                confidence.append(0)
            if support_thirdAtt !=0:
                confidence.append(float("{:.3f}".format(support/support_thirdAtt)))     #C--->B,A
            else:
                confidence.append(0)
            if support_first2ndAtt !=0:
                confidence.append(float("{:.3f}".format(support/support_first2ndAtt)))  #AB--->C
            
            else:
                confidence.append(0)    

            if support_second3rdAtt !=0:
                confidence.append(float("{:.3f}".format(support/support_second3rdAtt))) #BC--->A
            else:
                confidence.append(0)
            if support_third1stAtt !=0:
                confidence.append(float("{:.3f}".format(support/support_third1stAtt)))  #AC--->B
            else:
                confidence.append(0)
            if confidence[0]>=min_confidence:
                if support_firstAtt*support_second3rdAtt == 0:
                    continue
                else:
                    lift = float("{:.3f}".format(support/(support_firstAtt*support_second3rdAtt))) 
                    lev  = float("{:.3f}".format(support-(support_firstAtt*support_second3rdAtt))) 
                    print("{} ==============>{},{} support={} ,Confidence={} , lift = {},leverage={} ".format(firstAtt , secondAtt,thirdAtt,support , confidence[0],lift,lev))
                    final_Out.append((firstAtt , secondAtt,thirdAtt,support , confidence[0],lift,lev))
                    print('---------------------------------------------------------------------------------------------------')
            if confidence[1]>=min_confidence:
                if (support_secondAtt*support_third1stAtt) == 0:
                    continue
                else:

                    lift = float("{:.3f}".format(support/(support_secondAtt*support_third1stAtt))) 
                    lev  = float("{:.3f}".format(support-(support_secondAtt*support_third1stAtt))) 
                    print("{} ==============>{},{} support={} ,Confidence={} , lift = {},leverage={} ".format(secondAtt,thirdAtt , firstAtt,support , confidence[1],lift,lev))
                    final_Out.append((secondAtt,thirdAtt , firstAtt,support , confidence[1],lift,lev))
                    print('---------------------------------------------------------------------------------------------------')
            if confidence[2]>=min_confidence:
                if (support_thirdAtt*support_first2ndAtt) == 0:
                    continue
                else:
                    lift = float("{:.3f}".format(support/(support_thirdAtt*support_first2ndAtt))) 
                    lev  = float("{:.3f}".format(support-(support_thirdAtt*support_first2ndAtt))) 
                    print("{}==============>{},{} support={} ,Confidence={} , lift = {},leverage={} ".format(thirdAtt,firstAtt,secondAtt,support , confidence[2],lift,lev))
                    final_Out.append((firstAtt,thirdAtt,secondAtt,support , confidence[2],lift,lev))
                    print('---------------------------------------------------------------------------------------------------')
            if confidence[3]>=min_confidence:
                if (support_first2ndAtt*support_thirdAtt) == 0:
                    continue
                else:
                    lift = float("{:.3f}".format(support/(support_first2ndAtt*support_thirdAtt))) 
                    lev  = float("{:.3f}".format(support-(support_first2ndAtt*support_thirdAtt))) 
                    print("{} ,{}==============>,{} support={} ,Confidence={} , lift = {},leverage={} ".format(secondAtt,firstAtt,thirdAtt,support , confidence[3],lift,lev))
                    final_Out.append((secondAtt,firstAtt,thirdAtt,support , confidence[3],lift,lev))
                    print('---------------------------------------------------------------------------------------------------')
            if confidence[4]>=min_confidence:
                if (support_second3rdAtt*support_firstAtt) == 0:
                    continue
                else:
                    lift = float("{:.3f}".format(support/(support_second3rdAtt*support_firstAtt))) 
                    lev  = float("{:.3f}".format(support-(support_second3rdAtt*support_firstAtt))) 
                    print("{} ,{}==============>.{} support={} ,Confidence={} , lift = {},leverage={} ".format(thirdAtt,secondAtt,firstAtt,support , confidence[4],lift,lev))
                    final_Out.append((thirdAtt,secondAtt,firstAtt,support , confidence[4],lift,lev))
                    print('---------------------------------------------------------------------------------------------------')
            if confidence[5]>=min_confidence:
                if (support_third1stAtt*support_secondAtt)== 0:
                    continue
                else:
                    lift = float("{:.3f}".format(support/(support_third1stAtt*support_secondAtt))) 
                    lev  = float("{:.3f}".format(support-(support_third1stAtt*support_secondAtt))) 
                    print("{} ,{}==============>.{} support={} ,Confidence={} , lift = {},leverage={} ".format(thirdAtt,firstAtt,secondAtt,support , confidence[5],lift,lev))
                    final_Out.append((thirdAtt,secondAtt,firstAtt,support , confidence[5],lift,lev))
                    print('---------------------------------------------------------------------------------------------------')
            else:
                continue
            confidence = []
        elif len(i[0] )==4:
            firstAtt = attributes[0]
            secondAtt = attributes[1]
            thirdAtt = attributes[2]
            forthAtt = attributes[3]

            support   = float(i[1])
            support_firstAtt  = Retrieve_L1_Support(Fin_out , firstAtt)
            support_secondAtt = Retrieve_L1_Support(Fin_out , secondAtt)
            support_thirdAtt  = Retrieve_L1_Support(Fin_out , thirdAtt)
            support_forthAtt  = Retrieve_L1_Support(Fin_out , forthAtt)
            support_first2ndAtt  = Retrieve_L2_Support(Fin_out , firstAtt,secondAtt)
            support_second3rdAtt = Retrieve_L2_Support(Fin_out , secondAtt,thirdAtt)
            support_third4thAtt  = Retrieve_L2_Support(Fin_out , thirdAtt,forthAtt)
            support_forth1stAtt  = Retrieve_L2_Support(Fin_out , forthAtt,firstAtt)
            support_first2nd3rdAtt  = Retrieve_L3_Support(Fin_out , firstAtt,secondAtt,thirdAtt)
            support_second3rd4thAtt = Retrieve_L3_Support(Fin_out , secondAtt,thirdAtt,forthAtt)
            support_third4th1stAtt  = Retrieve_L3_Support(Fin_out , thirdAtt,forthAtt,firstAtt)
            support_forth1st2ndAtt  = Retrieve_L3_Support(Fin_out , forthAtt,firstAtt,secondAtt)




            if support_firstAtt !=0:
                confidence.append(float("{:.3f}".format(support/support_firstAtt) )) #A ->>>BCD
            else:
                confidence.append(0)
            if support_secondAtt !=0:
                confidence.append(float("{:.3f}".format(support/support_secondAtt))) #B ->>>ACD
            else:
                confidence.append(0)
            if support_thirdAtt !=0:
                confidence.append(float("{:.3f}".format(support/support_thirdAtt)))  #C ->>>BDA
            else:
                confidence.append(0)
            if support_forthAtt !=0:
                confidence.append(float("{:.3f}".format(support/support_forthAtt)))  #D ->>>BCA
            else:
                confidence.append(0)
            if support_first2ndAtt !=0:
                confidence.append(float("{:.3f}".format(support/support_first2ndAtt) )) #AB ->>>CD
            else:
                confidence.append(0)
            if support_second3rdAtt !=0:
                confidence.append(float("{:.3f}".format(support/support_second3rdAtt))) #BC ->>>AD
            else:
                confidence.append(0)
            if support_third4thAtt !=0:
                confidence.append(float("{:.3f}".format(support/support_third4thAtt)))  #CD ->>>AB
            else:
                confidence.append(0)
            if support_forth1stAtt !=0:
                confidence.append(float("{:.3f}".format(support/support_forth1stAtt)))  #DA ->>>BC
            else:
                confidence.append(0)
            if support_first2nd3rdAtt !=0:
                confidence.append(float("{:.3f}".format(support/support_first2nd3rdAtt) )) #ABC ->>>D
            else:
                confidence.append(0)
            if support_second3rd4thAtt !=0:
                confidence.append(float("{:.3f}".format(support/support_second3rd4thAtt))) #BCD ->>>A
            else:
                confidence.append(0)
            if support_second3rd4thAtt !=0:
                confidence.append(float("{:.3f}".format(support/support_second3rd4thAtt)))  #CDA ->>>B
            else:
                confidence.append(0)
            if support_forth1st2ndAtt !=0:
                confidence.append(float("{:.3f}".format(support/support_forth1st2ndAtt)))  #DAB ->>>C
            else:
                confidence.append(0)
            if confidence[0] >=min_confidence:
                if (support_firstAtt*support_second3rd4thAtt)== 0:
                    continue
                else:
                    lift = float("{:.3f}".format(support/(support_firstAtt*support_second3rd4thAtt))) 
                    lev  = float("{:.3f}".format(support-(support_firstAtt*support_second3rd4thAtt)))
                    print("{} ==============>{},{},{} support={} ,Confidence={} , lift = {},leverage={} ".format(firstAtt , secondAtt,thirdAtt,forthAtt,support , confidence[0],lift,lev))
                    final_Out.append((firstAtt , secondAtt,thirdAtt,forthAtt,support , confidence[0],lift,lev))
                    print('---------------------------------------------------------------------------------------------------')
            if confidence[1] >=min_confidence:
                if (support_secondAtt*support_third4th1stAtt)== 0:
                    continue
                else:
                    lift = float("{:.3f}".format(support/(support_secondAtt*support_third4th1stAtt))) 
                    lev  = float("{:.3f}".format(support-(support_secondAtt*support_third4th1stAtt))) 
                    print("{} ==============>{},{},{} support={} ,Confidence={} , lift = {},leverage={} ".format(secondAtt , firstAtt  ,thirdAtt,forthAtt,support , confidence[0],lift,lev))
                    final_Out.append((secondAtt,firstAtt , thirdAtt,forthAtt,support , confidence[1],lift,lev))
                    print('---------------------------------------------------------------------------------------------------')
            if confidence[2] >=min_confidence:
                if (support_thirdAtt*support_forth1st2ndAtt)== 0:
                    continue
                else:
                    lift = float("{:.3f}".format(support/(support_thirdAtt*support_forth1st2ndAtt))) 
                    lev  = float("{:.3f}".format(support-(support_thirdAtt*support_forth1st2ndAtt))) 
 
                    print("{} ==============>{},{},{} support={} ,Confidence={} , lift = {},leverage={} ".format(thirdAtt,firstAtt , secondAtt,forthAtt,support , confidence[0],lift,lev))
                    final_Out.append((thirdAtt,firstAtt , secondAtt,forthAtt,support , confidence[2],lift,lev))
                    print('---------------------------------------------------------------------------------------------------')
            if confidence[3] >=min_confidence:
                if (support_forthAtt*support_first2nd3rdAtt)== 0:
                    continue
                else:
                    lift = float("{:.3f}".format(support/(support_forthAtt*support_first2nd3rdAtt))) 
                    lev  = float("{:.3f}".format(support-(support_forthAtt*support_first2nd3rdAtt))) 

                    print("{} ==============>{},{},{} support={} ,Confidence={} , lift = {},leverage={} ".format(forthAtt,firstAtt , secondAtt,thirdAtt,support , confidence[0],lift,lev))
                    final_Out.append((forthAtt,firstAtt , secondAtt,thirdAtt,support , confidence[3],lift,lev))
                    print('---------------------------------------------------------------------------------------------------')
            if confidence[4] >=min_confidence:
                if (support_first2ndAtt*support_second3rd4thAtt)== 0:
                    continue
                else:
                    lift = float("{:.3f}".format(support/(support_first2ndAtt*support_second3rd4thAtt))) 
                    lev  = float("{:.3f}".format(support-(support_first2ndAtt*support_second3rd4thAtt))) 

                    print("{},{} ==============>{},{} support={} ,Confidence={} , lift = {},leverage={} ".format(firstAtt , secondAtt,thirdAtt,forthAtt,support , confidence[0],lift,lev))
                    final_Out.append((firstAtt , secondAtt,thirdAtt,forthAtt,support , confidence[4],lift,lev))
                    print('---------------------------------------------------------------------------------------------------')
            if confidence[5] >=min_confidence:
                if (support_second3rdAtt*support_forth1stAtt)== 0:
                    continue
                else:
                    lift = float("{:.3f}".format(support/(support_second3rdAtt*support_forth1stAtt))) 
                    lev  = float("{:.3f}".format(support-(support_second3rdAtt*support_forth1stAtt))) 
       
                    print("{},{} ==============>{},{} support={} ,Confidence={} , lift = {},leverage={} ".format(thirdAtt , secondAtt,firstAtt,forthAtt,support , confidence[0],lift,lev))
                    final_Out.append((secondAtt,thirdAtt,firstAtt , forthAtt,support , confidence[5],lift,lev))
                    print('---------------------------------------------------------------------------------------------------')
            if confidence[6] >=min_confidence:
                if (support_third4thAtt*support_forth1st2ndAtt)== 0:
                    continue
                else:
                    lift = float("{:.3f}".format(support/(support_third4thAtt*support_forth1st2ndAtt))) 
                    lev  = float("{:.3f}".format(support-(support_third4thAtt*support_forth1st2ndAtt))) 

                    print("{},{} ==============>{},{} support={} ,Confidence={} , lift = {},leverage={} ".format(firstAtt , secondAtt,thirdAtt,forthAtt,support , confidence[0],lift,lev))
                    final_Out.append((thirdAtt,forthAtt,firstAtt , secondAtt,support , confidence[6],lift,lev))
                    print('---------------------------------------------------------------------------------------------------')
            if confidence[7] >=min_confidence:
                if (support_forth1stAtt*support_second3rdAtt)== 0:
                    continue
                else:
                    lift = float("{:.3f}".format(support/(support_forth1stAtt*support_second3rdAtt))) 
                    lev  = float("{:.3f}".format(support-(support_forth1stAtt*support_second3rdAtt))) 

                    print("{},{} ==============>{},{} support={} ,Confidence={} , lift = {},leverage={} ".format(firstAtt , secondAtt,thirdAtt,forthAtt,support , confidence[0],lift,lev))
                    final_Out.append((firstAtt ,forthAtt, secondAtt,thirdAtt,support , confidence[7],lift,lev))
                    print('---------------------------------------------------------------------------------------------------')
            if confidence[8] >=min_confidence:
                if (support_firstAtt*support_second3rd4thAtt)== 0:
                    continue
                else:
                    lift = float("{:.3f}".format(support/(support_firstAtt*support_second3rd4thAtt))) 
                    lev  = float("{:.3f}".format(support-(support_firstAtt*support_second3rd4thAtt))) 

                    print("{},{},{} ==============>{} support={} ,Confidence={} , lift = {},leverage={} ".format( secondAtt,thirdAtt,forthAtt,firstAtt ,support , confidence[0],lift,lev))
                    final_Out.append((secondAtt,thirdAtt,forthAtt,firstAtt ,support , confidence[8],lift,lev))
                    print('---------------------------------------------------------------------------------------------------')
            if confidence[9] >=min_confidence:
                if (support_secondAtt*support_third4th1stAtt)== 0:
                    continue
                else:
                    lift = float("{:.3f}".format(support/(support_secondAtt*support_third4th1stAtt))) 
                    lev  = float("{:.3f}".format(support-(support_secondAtt*support_third4th1stAtt))) 

                    print("{},{},{} ==============>{} support={} ,Confidence={} , lift = {},leverage={} ".format(secondAtt,firstAtt , thirdAtt,forthAtt,support , confidence[0],lift,lev))
                    final_Out.append((thirdAtt,secondAtt,firstAtt,forthAtt , support , confidence[9],lift,lev))
                    print('---------------------------------------------------------------------------------------------------')
            if confidence[10] >=min_confidence:
                if (support_thirdAtt*support_second3rd4thAtt)== 0:
                    continue
                else:
                    lift = float("{:.3f}".format(support/(support_thirdAtt*support_second3rd4thAtt))) 
                    lev  = float("{:.3f}".format(support-(support_thirdAtt*support_second3rd4thAtt))) 

                    print("{},{},{} ==============>{} support={} ,Confidence={} , lift = {},leverage={} ".format(thirdAtt,firstAtt , secondAtt,forthAtt,support , confidence[0],lift,lev))
                    final_Out.append((firstAtt , secondAtt,thirdAtt,forthAtt,support , confidence[10],lift,lev))
                    print('---------------------------------------------------------------------------------------------------')
            if confidence[11] >=min_confidence:
                if (support_forthAtt*support_first2nd3rdAtt)== 0:
                    continue
                else:
                    lift = float("{:.3f}".format(support/(support_forthAtt*support_first2nd3rdAtt))) 
                    lev  = float("{:.3f}".format(support-(support_forthAtt*support_first2nd3rdAtt))) 

                    print("{},{},{} ==============>{} support={} ,Confidence={} , lift = {},leverage={} ".format(forthAtt,firstAtt , secondAtt,thirdAtt,support , confidence[0],lift,lev))
                    final_Out.append((forthAtt,firstAtt , secondAtt,thirdAtt,support , confidence[11],lift,lev))
                print('---------------------------------------------------------------------------------------------------')#level 5     #level 5 
        else:
            print(i)
            final_Out.append(i)
            print('---------------------------------------------------------------------------------------------------')

    print("There are {} Association Rules generated !".format(len(final_Out)))
Calculate_All(Fin_out)
