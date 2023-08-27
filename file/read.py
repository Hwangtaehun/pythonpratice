# score_file = open("score.txt", "r", encoding="utf8")
# print(score_file.read())
# score_file.close()

# score_file = open("score.txt", "r", encoding="utf8")
# print(score_file.readline(), end="")
# print(score_file.readline(), end="")
# print(score_file.readline(), end="")
# print(score_file.readline(), end="")
# score_file.close()

# score_file = open("score.txt", "r", encoding="utf8")

# while True:
#     line = score_file.readline()
#     if not line:
#         break
#     print(line, end="")

# score_file.close()

score_file = open("score.txt", "r", encoding="utf8")

lines = score_file.readlines() # 파일에서 모든 줄을 읽어와 리스트 형태로 저장
for line in lines: # lines에 내용이 있을 때까지
    print(line, end="")

score_file.close()