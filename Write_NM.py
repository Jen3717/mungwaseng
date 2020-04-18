# Print N lines M datas
# Each datas on the line should have a blank between
# datas on each line N = from (N-2)*M+1 to N*M
# go to the next line by "\n"


N = int(input("write the number of line (N) : "))
M = int(input("Write the number of int (M) : "))

for i in range(1, N+1):  # line N
    result = []
    result.clear()

    start_num = (i-1) * M + 1
    last_num = i * M
    for j in range (start_num, last_num+1):
        result.append(j)

    print(result,"\n") # 출력하고 다음줄



