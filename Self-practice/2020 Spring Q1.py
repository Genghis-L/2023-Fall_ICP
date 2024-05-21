def anagram(param1, param2):
    flag = 1
    for i in param2:
        # if ord(i) in (range(ord("A"), ord("Z") + 1) or range(ord("a"), ord("z") + 1)):
        if "A" <= i <= "Z" or "a" <= i <= "z":
            if i not in param1:
                flag = 0
    if flag == 1:
        return True
    else:
        return False


print(anagram("software", "swear oft"))
