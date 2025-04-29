# Tower of Hanoi
# Rules:    The number of moves needed to solve it with n disks is always: 2^𝑛 − 1 where 𝑛 n is the number of disks.
#           The allowed disk movements between the rods exhibit a repetitive pattern occurring every three moves.



# Import module(s)
from utils import tower_of_hanoi_iterative


# Use dictionary to represent rods
rods = {
    "A": [],  # source rod
    "B": [],  # auxiliary rod
    "C": []   # target rod
}


# Call the function
tower_of_hanoi_iterative(3, "A", "B", "C", rods)


