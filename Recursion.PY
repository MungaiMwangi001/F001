#Recursion is a programming approach that allows you 
#to solve complicated computational problems with just a little code.
# solved in 2n - 1 moves, where n isthe number of disks

'''
The first rod is the source, where all the disks are stacked on top of each other at the beginning of the game.
The second rod is an auxiliary rod, and it helps in moving the disks to the target rod.
The third rod is the target, where all the disks should be placed in order at the end of the game.
'''

NUMBER_OF_DISKS = 5  # store the number of disks 

A = list(range(NUMBER_OF_DISKS, 0, -1))
B = []
C = []

def move(n, source, auxiliary, target):
    if n <= 0:
        return
        # move n - 1 disks from source to auxiliary, so they are out of the way
    move(n - 1, source, target, auxiliary)
        
        # move the nth disk from source to target
    target.append(source.pop())
        
        # display our progress
    print(A, B, C, '\n')
        
        # move the n - 1 disks that we left on auxiliary onto target
    move(n - 1,  auxiliary, source, target)
              
# initiate call from source A to target C with auxiliary B
move(NUMBER_OF_DISKS, A, B, C)