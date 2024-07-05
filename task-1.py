def find_equilibrium_index(arr: list) -> int | None:
    for i in range(len(arr)):
        left_sum = sum(arr[:i])
        right_sum = sum(arr[i + 1:])

        if left_sum == right_sum:
            return i

    return None


array = [1, 7, 3, 6, 5, 6]
index = find_equilibrium_index(array)
print(f"Equilibrium index is:{index}")
