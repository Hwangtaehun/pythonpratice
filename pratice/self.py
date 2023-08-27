with open("class.txt", "r", encoding="utf8") as f:
    txt = f.read() # 파일 내용 읽어 오기
    words = txt.split() # 내용을 띄어쓰기로 구분해 리스트로 반환
    for word in words:
        print(word, end=" ")
        if word.endswith("명"): # 명으로 끝나면 줄 바꿈
            print()