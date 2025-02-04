# 코드 1.1a: 스택을 위한 데이터
capacity = 10
array = [None] * capacity
top = -1

# 코드 1.1b: 스택의 공백 상태와 포화 상태 검사
def isEmpty() :
    if top == -1 : return True
    else : return False

def isFull() : return top == capacity - 1

# 코드 1.1c: 스택의 삽입 연산
def push(e) :
    # global top
    if not isFull() :
        top += 1
        array[top] = e
    else :
        print("stack overflow")
        exit()

# 코드 1.1d: 스택의 삭제 연산
def pop() :
    # global top
    if not isEmpty():
        top -= 1
        return array[top + 1]
    else :
        print("stack underflow")
        exit()

# 코드 1.1e: 스택의 peek() 연산
def peek() :
    if not isEmpty() :
        return array[top]
    else : pass

# 코드 1.1f: 스택의 size() 연산
def size() : return top+1