def sort(arr):
    for i in range(1, len(arr)):
        cle = arr[i]
        j = i - 1
        while j >= 0 and cle < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = cle   
    

liste = [12, 11, 13, 5, 6]

sort(liste)
print(liste)



