for waiting_no in range(1, 6):
  print("대기 번호 : {0}".format(waiting_no))

menu = {"커피", "우유", "주스"}
print(menu)
print(type(menu))

menu = list(menu)
print(menu, type(menu))

menu = tuple(menu)
print(menu, type(menu))

menu = set(menu)
print(menu, type(menu))