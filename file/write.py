# score.txt 파일에 이어 쓰기 모드로 열기
score_file = open("score.txt", "a", encoding="utf8")
# write() 함수는 줄 바꿈이 없으므로 \n 추가
score_file.write("과학 : 80\n")
score_file.write("코딩 : 100\n")
score_file.close()