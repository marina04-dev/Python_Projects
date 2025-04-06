################# Geneva Confection ##############
''' If the current cart on the mountain is the correct number send
it into the lake, otherwise see if the current cart of the branch
can be sent in the lake, if it can, send it in. If neither the branch 
or the mountain top have the correct cart then send the cart from 
the mountain to the branch and repeat the process. Once there are 
no more carts on the mountain and the cart on the branch can't be sent into
the lake then you cannot complete the recipe'''

testCases = int(input("Enter the amount of Test Cases: "))
testlist = []

# Creates a nested list with each test case inside of the main list 'testlist'
for x in range(testCases):
    testlist.append([])
    f = input(f"Enter number of elements in the {x+1} case: ")
    for y in range(int(f)):
        testlist[x].append(int(input(f"Enter {x+1}-{y+1} element: ")))
        
# For each test Case
for x in range(testCases):
    # we need to store the location of the cars on the mountain, branch and the car we are looking for 
    carList = testlist[x]
    branch = []
    current = 1 
    
    while True:
        # First Step: If cars are on the mountain try to send them into the lake
        if len(carList) > 0:
            # If the car on the mountain is the car we are looking for send it to the lake (remove from mountain)
            if carList[-1] == current:
                current += 1 
                carList.pop();
            
            # Otherwise see if there are any cars in the branch
            elif len(branch) > 0:
                # If there are cars on the branch see if they can be sent into the lake 
                if branch[-1] == current:
                    current += 1 
                    branch.pop()
                
                # Otherwise send the car from the mountain to the branch
                else:
                    branch.append(carList.pop())
            
            # Otherwise send the car from the mountain to the branch
            else:
                branch.append(carList.pop())
        
        # If there are no more cars on the mountain see if there are any on the branch
        elif len(branch) > 0:
            if branch[-1] == current: # If the car on the branch can be moved into the lake do so
                current += 1 
                branch.pop()
            else: # Otherwise there is no way for us to complete the recipe
                print('N')
                break 
            
        # If the mountain and the branch are empty then we are done 
        else:
            print('Y')
            break 
                
    
