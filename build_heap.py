# python3
import heapq

def build_heap(data):
    swaps = []
    n = len(data)

    def heapsort(i):
        nonlocal swaps
        small = i
        left = 2*i + 1
        right = 2*i + 2

        if left < n and data[left] < data[small]:
            small = left

        if right < n and data[right] < data[small]:
            small = right

        if small != i:
            data[i], data[small] = data[small], data[i]
            swaps.append((i, small))
            heapsort(small)

    for i in range(n//2, -1, -1):
        heapsort(i)

    return swaps




    # TODO: Creat heap and heap sort
    # try to achieve  O(n) and not O(n2)

   # return swaps


def main():
    
    # TODO : add input and corresponding checks
    # add another input for I or F 
    # first two tests are from keyboard, third test is from a file
    # input from keyboard
    
    mode = input()
    if "F" in mode:
        filename = input()
        if "a" not in filename:
            with open(str("test/"+filename), mode = "r") as f:
                n = int(f.readline())
                data = list(map(int, f.readline().split()))
        else:
            print("error")
    elif "I" in mode:
        n = int(input())
        data = list(map(int, input().split()))
    else:
        print("invalid data")

    # checks if lenght of data is the same as the said lenght
    assert len(data) == n

    # calls function to assess the data 
    # and give back all swaps
    swaps = build_heap(data)

    # TODO: output how many swaps were made, 
    # this number should be less than 4n (less than 4*len(data))


    # output all swaps
    print(len(swaps))
    for i, j in swaps:
        print(i, j)


if __name__ == "__main__":
    main()
