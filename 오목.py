#오목

black_stones = []
white_stones = []

#오목에서 그림을 그리는 함수입니다.
def draw_board():
    print()
    for y in range(15):
        for x in range(15):
            if (x, y) in black_stones:
                print("●", end=" ")
            elif (x, y) in white_stones:
                print("○", end=" ")
            else:
                print("┼", end=" ")
        print()
    print()

#오목에서 특정방향으로 5개의 돌이 연속되어 있는지 확인하는 함수입니다.
def check_five_in_a_row(stone, stones, direction, count):
    if count == 5:
        return True
    else:
        next_stone = (stone[0] + direction[0], stone[1] + direction[1])
        if next_stone in stones:
            return check_five_in_a_row(next_stone, stones, direction, count + 1)
        else:
            return False


#오목에서 승리여부를 확인하는 함수입니다.
def check_win(stones):
    last_stone = stones[-1]
    directions = [(1, 0), (0, 1), (1, 1), (1, -1), (-1, 0), (0, -1), (-1, -1), (-1, 1)]
    for direction in directions:
        if check_five_in_a_row(last_stone, stones, direction, 1):
            return True
        else:
            return False


#main

draw_board()
while True:
    black_stones.append(tuple(map(int, input("검은 돌의 좌표를 입력하세요: ").split(","))))
    draw_board()
    if check_win(black_stones):
        print("검은 돌이 이겼습니다!")
        break
    
    white_stones.append(tuple(map(int, input("흰 돌의 좌표를 입력하세요: ").split(","))))
    draw_board()
    if check_win(white_stones):
        print("흰 돌이 이겼습니다!")
        break