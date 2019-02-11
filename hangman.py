
# coding: utf-8

# In[5]:


def hangman(word):
    wrong = 0
    stages = ["",
             "________        ",
             "|               ",
             "|        |      ",
             "|        0      ",
             "|       /|\     ",
             "|       / \     ",
             "|               "
              ]
    rletters = list(word)
    board = ["_"]*len(word)
    win = False
    print("welcome!")
    while wrong < len(stages) -1:
        print("\n")
        msg = "1文字を入力"
        char = input(msg)
        if char in rletters:
            cind = rletters.index(char)
            board[cind] = char
            rletters[cind] = "$"
        else:
            wrong +=1
            print(" ".join(board))
            e = wrong +1
            print("\n".join(stages[0:e]))
            if "_" not in board:
                print("you win")
                print(" ".join(board))
                win = True
                break


# In[3]:


list("hello")
x = list("hello")
print(x.index("l"))


# In[6]:


hangman("hello")


# In[29]:


def hangman2():    
    import random
    word_list = ["hello","goodmorning","steak","magcup","elephant","tissue","kingdom"]
    x = random.randint(0,len(word_list)-1)
    word = word_list[x]
    wrong = 0
    stages = ["",
             "________        ",
             "|               ",
             "|        |      ",
             "|        0      ",
             "|       /|\     ",
             "|       / \     ",
             "|               "
              ]
    rletters = list(word)
    board = ["_"]*len(word)
    win = False
    print("welcome!")
    while wrong < len(stages) -1:
        print("\n")
        msg = "1文字を入力"
        char = input(msg)
        if char in rletters:
            cind = rletters.index(char)
            board[cind] = char
            rletters[cind] = "$"
            print(" ".join(board))
            if "_" not in board:
                print("you win")
                print(" ".join(board))
                win = True
                break
        else:
            wrong +=1
            print(" ".join(board))
            e = wrong +1
            print("\n".join(stages[0:e]))
            if wrong >= len(stages) -1:
                print("you lose! the answer is {}.".format(word))
                break


# In[12]:


def random():
    import random
    word_list = ["hello","goodmorning","steak","magcup","elephant","tissue","kingdom"]
    x = random.randint(0,len(word_list)-1)
    word = word_list[x]
    print(word)


# In[16]:


random()


# In[31]:


hangman2()

