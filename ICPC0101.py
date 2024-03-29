def shrink_array(n, A):
    stack = []
    for num in A:
        if len(stack) == 0 or (stack[-1] + num) % 2 != 0:
            stack.append(num)
        else:
            stack.pop()
    length=len(stack)
    return length

def solve():
    # Đọc input
    
    n = int(input())
    A = list(map(int, input().split()))

    # Gọi hàm tính số phần tử còn lại
    result = shrink_array(n, A)

    # In kết quả
    print(result)
    
if __name__ == "__main__":
    solve()