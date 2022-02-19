##############################################################################
# My Recursive Implementation for the Tower of Hanoi
# Mark Barros
# CS3310 - Design and Analysis of Algorithms
# Cal Poly Pomona: Spring 2021
##############################################################################

# This is an imported module. ------------------------------------------------
import time

# These are global variables. ------------------------------------------------
n = 3                       # is the number of disks

start = 0                   # start is the "time" when an iteration of
                            # quickSort begins.
finish = 0                  # finish is the "time" when an iteration of
                            # quickSort ends.
period = 0                  # period is the amount of time, in seconds, that
                            # quickSort took to complete an iteration.

# This is the recursive definition. ------------------------------------------
def TowerOfHanoi(n , source, destination, auxiliary):

    if n == 1:
        print ("Move disk 1 from source", \
                source,"to destination", destination)
        return

    TowerOfHanoi(n - 1, source, auxiliary, destination)

    print ("Move disk", n, "from source", \
            source,"to destination", destination)

    TowerOfHanoi(n - 1, auxiliary, destination, source)

# This is the driver code. ---------------------------------------------------

if __name__ == '__main__':

    # This is the output header.
    print("------------------------------------------------------")
    print("Recursive Implementation for the Tower of Hanoi")
    print("------------------------------------------------------")
    print("Mark Barros")
    print("CS3310 - Design and Analysis of Algorithms")
    print("Cal Poly Pomona: Spring 2021")
    print("------------------------------------------------------")
    print("Move the disks in the following order:\n")

    # This repeatedly calls TowerOfHanoi and outputs the results.
    while n <= 3:

        # A, B, and C are the names of the pegs.
        start = time.perf_counter_ns()
        TowerOfHanoi(n,'A','B','C')
        finish = time.perf_counter_ns()

        # This calculates the elapsed time in seconds.
        period = ((finish - start) * (10**-9))

        # This outputs to the screen the number of disks and the
        # corresponding time it took to solve the problem.
        print("------------------------------------------------------")
        print("Execution time: For n = ", f'{n:1,}', " t = ", f'{period:.3}')
        print("------------------------------------------------------")

        n += 1



# End of Script. #############################################################