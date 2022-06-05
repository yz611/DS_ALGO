"""
sorting algorithms
"""

from heapq import merge


def BubbleSort(customList):
    i = 0
    for i in range(len(customList) - 1):
        for j in range(len(customList) - i - 1):
            if customList[j] > customList[j+1]:
                customList[j], customList[j+1] = customList[j+1], customList[j]
    return customList                

def SelectionSort(customList):
    for i in range(len(customList) - 1):
        min = customList[i]
        for j in range(i + 1, len(customList)):
            if min > customList[j]:
                min = customList[j]
                min_index = j
        customList[i], customList[min_index] = customList[min_index], customList[i]
    return customList

def InsertionSort(customList):
    for i in range(1, len(customList)):
        j = i - 1
        while customList[j + 1] < customList[j] and j >= 0:
            customList[j + 1], customList[j] = customList[j], customList[j + 1]
            j -= 1
    return customList


def Merge(lList, rList):
    l = r = 0
    mergedList = []
    searchLenth = 2 * min(len(lList), len(rList))
    for i in range(searchLenth):
        try:    
            if lList[l] < rList[r]:
                mergedList.append(lList[l])
                l += 1
            else: 
                mergedList.append(rList[r])
                r += 1
        except:
            break
    for i in range(l, len(lList)):
        mergedList.append(lList[i])
    for i in range(r, len(rList)):
        mergedList.append(rList[i])
    return mergedList
    
            
            
def MergeSort(customList):
    l = 0
    r = len(customList)
    if r - l == 1:
        return customList
    m = len(customList) // 2
    lList = customList[l: m]
    rList = customList[m: r]
    sortedlList = MergeSort(lList)
    sortedrList = MergeSort(rList)
    sortedList = Merge(sortedlList, sortedrList)
    
    return sortedList

def getMid(customList):
    try:
        p = customList[-1]
    except IndexError:
        return 0
    j = 0
    for i in range(len(customList) - 1):
        if customList[i] < p:
            customList[j], customList[i] = customList[i], customList[j]
            j+= 1
    customList[j], customList[-1] = customList[-1], customList[j]
    return j
        

def QuickSort(customList):
    l = 0
    r = len(customList)
    m = getMid(customList)
    lList = customList[l: m]
    rList = customList[m + 1: r]
    if r - l == 1:
        return customList
    if r - l == 0:
        return []
    pivot = customList[m]
    sortedlList = QuickSort(lList)
    sortedrList = QuickSort(rList)
    sortedlList.append(pivot)
    sortedList = sortedlList + sortedrList
    return sortedList
    
    

    

    

def main():
    customList = [3,0,5,9,1,0,8]
    print(QuickSort(customList))
    

if __name__ == "__main__":
    main()
                