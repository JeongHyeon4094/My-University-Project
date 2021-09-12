#!/usr/bin/env python
# coding: utf-8

# In[1]:


#20214094 박정현


# In[4]:


def Truth_table(operator, propositions):
    print("논리 연산자 : ")
    print(" x = ", operator)

    #논리 연산자를 비트 연산자로 변경
    operator = operator.replace("and", "&") 
    operator = operator.replace("or", "|")
    operator = operator.replace("xor", "^")
    operator = operator.replace("not", "~")
    
    print("\n진리표 :")
    if propositions == 2: #명제가 2개 일 때
        print("-------------")
        print("| p | q | x |")
        print("-------------")
        for p in range(2):
            for q in range(2):
                x = eval(operator)
                print("| " + str(p) + " | " + str(q) + " | " + str(x) + " |" )
                print("-------------")
    
    elif propositions == 3: #명제가 3개 일 때
        print("-----------------")
        print("| p | q | r | x |")
        print("-----------------")
        for p in range(2):
            for q  in range(2):
                for r in range(2):
                    x = eval(operator)
                    print("| " + str(p) + " | " + str(q) + " | " + str(r) + " | " + str(x) + " |" )
                    print("-----------------")
                    
    elif propositions == 4: #명제가 4개 일 때
        print("---------------------")
        print("| p | q | r | s | x |")
        print("---------------------")
        for p in range(2):
            for q in range(2):
                for r in range(2):
                    for s in range(2):
                        x = eval(operator)
                        print("| " + str(p) + " | " + str(q) + " | " + str(r) + " | " + str(s) + " | " + str(x) + " |" )
                        print("---------------------")


# In[5]:


operator = "p and q" #논리 연산자 입력
Truth_table(operator, 2) #함수 호출


# In[ ]:




