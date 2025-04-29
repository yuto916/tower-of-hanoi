def move_disk(rod1, rod2, rods):
    """
    Description:
    1. Determine in which direction a disk needs to be moved (forward vs backward).
    2. Move a disk from one rod to another and print the move.

    Parameters:
    rod1 (str): Name of the rod closer to the source rod.
    rod2 (str): Name of the rod closer to the target rod.
    rods (dict): Dictionary of rods with disks.
    """
    forward = False

    # Display current setup of rods
    print(f"Current Setup : {rods}")

    # The disk can be forwarded under following conditions:
    # 1. If the rod2 has no disk.
    # 2. If rod 1 has disk(s) & the top disk on rod1 is smaller than the top disk on rod2.
    if not rods[rod2]:
        forward = True
    elif rods[rod1] and rods[rod1][-1] < rods[rod2][-1]:
        forward = True

    # Forward == True : Move the disk towards the target
    # Forward == False: Move the disk towards the source
    if forward == True:
        print(f"Forward: Moving disk {rods[rod1][-1]} from {rod1} to {rod2}")
        rods[rod2].append(rods[rod1].pop())
    else:
        print(f"Backward: Moving disk {rods[rod2][-1]} from {rod2} to {rod1}")
        rods[rod1].append(rods[rod2].pop())


    # Display updated setup of rods
    print(f"Updated Setup: {rods}\n")



def tower_of_hanoi_iterative(num_of_disks, source, auxiliary, target, rods):
    """
    Description:
    Solves the Tower of Hanoi problem.
    
    Parameters:
    num_of_disks (int): The number of disks to move.
    source (str): The name of the rod where the disks are initially placed.
    auxiliary (str): The name of the auxiliary rod, used for temporarily holding disks during the process.
    target (str): The name of the rod where the disks need to be moved to in the end.
    rods (dict): Dictionary of rods with disks.
    """
    # Number of total moves required
    num_of_moves = 2 ** num_of_disks - 1

    # Assign the sequence of numbers to rod A.
    # num_of_disks represents the largest disk at the bottom
    rods["A"] = list(range(num_of_disks, 0, -1))
    print(f"Initial Rods Setup: {rods}\n")

    for i in range(num_of_moves):
        remainder = (i + 1) % 3

        if remainder == 1:
            if num_of_disks % 2 == 1:
                print(f'Move {i + 1}: between {source} and {target}')
                move_disk(source, target, rods)
            else:
                print(f'Move {i + 1}: between {source} and {auxiliary}')
                move_disk(source, auxiliary, rods)

        elif remainder == 2:
            if num_of_disks % 2 == 1:
                print(f"Move {i + 1}: between {source} and {auxiliary}")
                move_disk(source, auxiliary, rods)
            else:
                print(f"Move {i + 1}: between {source} and {target}")
                move_disk(source, target, rods)

        elif remainder == 0:
            print(f"Move {i + 1}: between {auxiliary} and {target}")
            move_disk(auxiliary, target, rods)


    # Print the final state of rods
    print("Final Rods Setup:", rods)


   
