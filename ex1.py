def search_match(arrayl, n):
    for i in range(len(arrayl)):
        for j in range(i+1, len(arrayl)):
            if arrayl[i]+ arrayl[j] == n:
                return [array[i], array[j]]
    return None

inputarray = input("Enter array with at least 3-4 numbers(comma separated): ")
array = [int(x) for x in inputarray.split(",")]
target = int(input("Enter the target sum: "))
print(f"the integer pair for the target is: ", search_match(array,target))
