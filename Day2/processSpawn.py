# Author: Mckenzie Mack
# GenCyber Workshop

from multiprocessing import Process
import time


# the fileCreate() function creates a new file and writes a given string to the file
# parameters: name = the desired name of the new file, number = number of the file (used in string written in file)

def fileCreate(name, number):
    print("Started new process, creating processSpawn" + str(i) + ".txt...")          # lets the user know that the process has started executing
    newFile = open(name, "w+")                                                        # opens new file and names the file the name given in the name parameter
    newFile.write("This is file #" + str(number) + " created by a spawned process.")  # prints given string to new file
    time.sleep(3)                                                                     # has process wait 1 second
    newFile.close()                                                                   # closes new file


for i in range(20):                                                                   # creates for loop that will loop through numbers 0-19
    spawn = Process(target=fileCreate(('processSpawn' + str(i) + '.txt'),(i + 1)))    # creates new process that will call fileCreate() function
    spawn.start()                                                                     # starts process
    spawn.join()                                                                      # halts the program until the process is finished
    print("Process finished executing, processSpawn" + str(i) + ".txt written.")      # lets user know that the file write is complete
