ins=[0,1,2,3,4,5,6,7,8]
check=[]
compare=['x','o']
x=compare[0]
o=compare[1]

print("welcome to Tic_Tac_Toe game!!!")
print("------------------------------")

print("\nFirst player will use 'o' ")

def result():

    # This first two cases are for the x player
    if (ins[0]==x and ins[1]==x and ins[2]==x)or (ins[3]==x and ins[4]==x and ins[5]==x)or (ins[6]==x and ins[7]==x and ins[8]==x)or (ins[0]==x and ins[4]==x and ins[8]==x)or (ins[2]==x and ins[4]==x and ins[6]==x):
        return True
    elif (ins[0]==x and ins[3]==x and ins[6]==x)or (ins[1]==x and ins[4]==x and ins[7]==x)or (ins[2]==x and ins[5]==x and ins[8]==x):
        return True 

    # This first two cases are for the o player
    elif (ins[0]==o and ins[1]==o and ins[2]==o)or (ins[3]==o and ins[4]==o and ins[5]==o)or (ins[6]==o and ins[7]==o and ins[8]==o)or (ins[0]==o and ins[4]==o and ins[8]==o)or (ins[2]==o and ins[4]==o and ins[6]==o):
        return True
    elif (ins[0]==o and ins[3]==o and ins[6]==o)or (ins[1]==o and ins[4]==o and ins[7]==o)or (ins[2]==o and ins[5]==o and ins[8]==o):
        return True 
    else:
        return False 


# this function is used to get the user input
def user(i):
    global user_input
    if i%2==0:
        user_input=int(input("\nEnter player1: "))
        return user_input
    else:
        user_input=int(input("\nEnter player2: "))
        return user_input


# this function is used to view the table
def view(user_input,i):
    check.append(user_input)
    if i%2!=0:
        ins[user_input]="x"
    else:
        ins[user_input]="o"
    print()
    print(ins[0],"|",ins[1],"|",ins[2])
    print("----------")
    print(ins[3],"|",ins[4],"|",ins[5])
    print("----------")
    print(ins[6],"|",ins[7],"|",ins[8])
    print()
    print()


user_input=None

for i in range(len(ins)):
    # calls the user function to get the user input
    user(i)
    print(user_input)
    
    if user_input>8:
        print("Enter value from 0 to 8")
    else:
        if user_input in check:
            # this for loop is used to get the user value which is does not exist in the check
            for j in range(len(check)+1):
                print("This value is already taken")
                user(i)
                if user_input in check:
                    continue
                else:
                    view(user_input,i)
                    break
            if result():
                if i%2!=0:
                    print("second player won")
                else:
                    print("First player won")
                break
            

           
        else:
            # calling the view function is used to view the place selected by the player
            view(user_input,i)
            if result():
                if i%2!=0:
                    print("second player won")
                else:
                    print("First player won")
                break
            
            
