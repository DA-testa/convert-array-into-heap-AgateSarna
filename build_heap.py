# python3

def build_heap(data):
    swaps = []
    n = len(data)

    for i in range(n // 2, -1, -1):
        small = i
        left = 2 * i + 1
        right = 2 * i + 2

        while left < n:
            if data[left] < data[small]:
                small = left
            if right < n and data[right] < data[small]:
                small = right
            if small != i:
                data[i], data[small] = data[small], data[i]
                swaps.append((i, small))
                i = small
                left = 2 * i + 1
                right = 2 * i + 2
            else:
                break

    return swaps




    # TODO: Creat heap and heap sort
    # try to achieve  O(n) and not O(n2)


def main():
    
    # TODO : add input and corresponding checks
    # add another input for I or F 
    # first two tests are from keyboard, third test is from a file
    # input from keyboard
    
    mode = input().strip()
    if "F" in mode:
        filename = input()
        if "a" in filename:
            return
        filename = 'tests/' + filename
        with open(filename, 'r') as f:
            n = int(f.readline().strip())
            data = list(map(int, f.readline().split()))
    elif "I" in mode:
        n = int(input())
        data = list(map(int, input().split()))
    else:
        print("invalid data")

    assert len(data) == n

    swaps = build_heap(data)

    print(len(swaps))
    for i, j in swaps:
        print(i, j)


if __name__ == "__main__":
    main()
