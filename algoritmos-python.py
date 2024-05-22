def ord_burbuja(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n-i-1):
            
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr

def ord_insercion(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i-1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
    return arr

def ord_seleccion(arr):
    for i in range(len(arr)):
        min_idx = i
        for j in range(i+1, len(arr)):
            if arr[j] < arr[min_idx]:
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]
    return arr

def ord_rapido(arr):
    if len(arr) <= 1:
        return arr
    else:
        pivot = arr[len(arr) // 2]
        left = [x for x in arr if x < pivot]
        middle = [x for x in arr if x == pivot]
        right = [x for x in arr if x > pivot]
        return ordenamiento_rapido(left) + middle + ordenamiento_rapido(right)

def ord_mezcla(arr):
    if len(arr) > 1:
        mid = len(arr) // 2
        left_half = arr[:mid]
        right_half = arr[mid:]

        ordenamiento_mezcla(left_half)
        ordenamiento_mezcla(right_half)

        i = j = k = 0

        while i < len(left_half) and j < len(right_half):
            if left_half[i] < right_half[j]:
                arr[k] = left_half[i]
                i += 1
            else:
                arr[k] = right_half[j]
                j += 1
            k += 1

        while i < len(left_half):
            arr[k] = left_half[i]
            i += 1
            k += 1

        while j < len(right_half):
            arr[k] = right_half[j]
            j += 1
            k += 1

    return arr

def auxi(arr, n, i):
    largest = i
    left = 2 * i + 1
    right = 2 * i + 2

    if left < n and arr[i] < arr[left]:
        largest = left

    if right < n and arr[largest] < arr[right]:
        largest = right

    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]
        auxi(arr, n, largest)

def ord_monticulo(arr):
    n = len(arr)

    for i in range(n//2 - 1, -1, -1):
        auxi(arr, n, i)

    for i in range(n-1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i]
        auxi(arr, i, 0)

    return arr

arr = [64, 34, 25, 12, 22, 11, 90]

print("Ordenamiento Burbuja:", ord_burbuja(arr.copy()))
print("Ordenamiento Inserción:", ord_insercion(arr.copy()))
print("Ordenamiento Selección:", ord_seleccion(arr.copy()))
print("Ordenamiento Rápido:", ord_rapido(arr.copy()))
print("Ordenamiento Mezcla:", ord_mezcla(arr.copy()))
print("Ordenamiento Montículo:", ord_monticulo(arr.copy()))