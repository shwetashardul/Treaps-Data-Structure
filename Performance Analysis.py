
from treapsf import Treaps
import random
import time
import timeit

inputSize = [1000,10000,15000,20000,30000]
cumTimes = [[0 for n in range(6)] for m in range(len(inputSize))]
numTrials = 100
sizeIndex = 0
insertIndex = 1
deleteIndex = 2
findIndex = 3
splitIndex = 4
joinIndex = 5
keys = []

def populate(treap,nextInputSize):
    if treap is None:
        treap= Treaps()
    for i in range(treap.size(), nextInputSize):
        treap.insert(keys[i])
    return treap

def keysForSuccessfulFind(sortedKey,sampleSize):
    sKey = []
    i = 1
    while i <= sampleSize:
        index = random.randint(0,sampleSize-1)
        key = sortedKey[index]
        if key in sKey:
            continue
        sKey.append(key)
        i = i + 1
    return sKey

def keysForUnsuccesfulFind(sortedKey,sampleSize):
    uKey = []
    i = 1
    while i <= sampleSize:
        index = random.randint(0,sampleSize)
        if index == len(sortedKey):
            key = sortedKey[len(sortedKey) - 1] + 1
        else:
            key = sortedKey[index] - 1
        if key in uKey:
            continue
        uKey.append(key)
        i = i + 1
    return uKey

def measurePerformance():
    treap=Treaps()
    i = 1
    root = None

    while i <= inputSize[len(inputSize) - 1] + numTrials:
        keys.append(2*i)
        i = i + 1
    random.shuffle(keys)

    for i in range(len(inputSize)):

        treap= populate(treap,inputSize[i])
        subKeys = []

        if i == 0:
            subKeys = keys[0:inputSize[i]]
        else:
            subKeys = keys[inputSize[i-1]:inputSize[i]]

        subKeys.sort()
        sKey = keysForSuccessfulFind(subKeys,numTrials)
        uKey = keysForUnsuccesfulFind(subKeys,numTrials)
        startTimerForSFind = timeit.default_timer()

        #for find operation
        for j in range(numTrials):
            Node_returned = treap.find(sKey[j])

        endTimerForSFind = timeit.default_timer() - startTimerForSFind
        startTimerForUFind = timeit.default_timer()

        for j in range(numTrials):
            Node_returned = treap.find(uKey[j])

        endTimerForUFind = timeit.default_timer() - startTimerForUFind
        cumTimerForSSplit = 0
        cumTimerForSJoin = 0
        '''key=input("Enter key for split: ")
      left_root,right_root=treap.split(key)
      print("Split is done.\nNew treap with keys smaller than or equal to the given key is: ")
      treap.root=left_root
      treap.print_treap()
      print("\nNew treap with keys larger than the given key:")
      larger_treap= Treaps()
      larger_treap.root=right_root
      larger_treap.print_treap()'''
        #For split and join of Successfull findings
        for j in range(numTrials):
            startTimerForSSplit = timeit.default_timer()
            left_root,right_root=treap.split(sKey[j])
            ##if isinstance(left_root,tuple):
                #left_root=left_root[1]
                #smaller_root,larger_root=larger_root[1]
            cumTimerForSSplit +=timeit.default_timer() - startTimerForSSplit

            startTimerForSJoin = timeit.default_timer()
            new_treap= Treaps()
            new_treap.root=left_root
            treap.join(new_treap)
            cumTimerForSJoin += timeit.default_timer() - startTimerForSJoin

        cumTimerForUSplit = 0
        cumTimerForUJoin = 0

        #For split and join of Unsuccessfull findings
        for j in range(numTrials):
            startTimerForUSplit = timeit.default_timer()
            left_root,right_root=treap.split(uKey[j])
            #if isinstance(left_root,tuple):
                #left_root=left_root[1]
            cumTimerForUSplit += timeit.default_timer() - startTimerForUSplit

            startTimerForUJoin = timeit.default_timer()
            new_treap.root=left_root
            treap.join(new_treap)
            cumTimerForUJoin =timeit.default_timer() - startTimerForUJoin

        subKeys = keys[inputSize[i]:inputSize[i]+numTrials]

        #For insertion
        startTimerForInsert = timeit.default_timer()
        for j in range(numTrials):
            treap.insert(subKeys[j])
        endTimerForInsert = timeit.default_timer() - startTimerForInsert

        #For deletion
        startTimerForDelete = timeit.default_timer()
        for j in range(numTrials):
            treap.remove(subKeys[j])
        endTimerForDelete = timeit.default_timer() - startTimerForDelete

        #Calculation of cumulative times
        cumTimes[i][sizeIndex] = inputSize[i]
        cumTimes[i][insertIndex] = round(endTimerForInsert * (10**3),4)
        cumTimes[i][findIndex] = round(((endTimerForSFind + endTimerForUFind) / 2) * (10**3),4)
        cumTimes[i][splitIndex] = round(((cumTimerForSSplit + cumTimerForUSplit) / 2) * (10**3),4)
        cumTimes[i][joinIndex] = round(((cumTimerForSJoin + cumTimerForUJoin) / 2) * (10**3),4)
        cumTimes[i][deleteIndex] = round(endTimerForDelete * (10**3),4)

def dumpPerformanceStats(cumTime):
    print("\nThe time taken in milliseconds for each {} operations is:\n".format(numTrials))
    print("{:<12} {:<10} {:<10} {:<12} {:<11} {:<12}\n".format("Size","Insert","Delete","Find","Split","Join"))
    for i in range(5):
        InputSize = cumTime[i][sizeIndex]
        Insert_time= cumTime[i][insertIndex]
        Find_time = cumTime[i][findIndex]
        Split_time = cumTime[i][splitIndex]
        Join_time = cumTime[i][joinIndex]
        Delete_time = cumTime[i][deleteIndex]

        print("{:<12} {:<10} {:<10} {:<12} {:<11} {:<12}".format(InputSize, Insert_time,Delete_time,Find_time,Split_time,Join_time))

if __name__ == "__main__":

    measurePerformance()
    dumpPerformanceStats(cumTimes)