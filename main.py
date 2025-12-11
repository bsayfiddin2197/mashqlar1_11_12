# 1
juft_kvadratlar = tuple(x*x for x in range(1, 21) if x % 2 == 0)
print("1) juft sonlar kvadratlari:", juft_kvadratlar)

# 2
uch_karrali = tuple(x for x in range(1, 51) if x % 3 == 0)
print("2) 3 ga karrali sonlar:", uch_karrali)

# 3
sample_list = ["hello", "123", "world", "456"]
uzunliklar = tuple(len(s) for s in sample_list)
print("3) satr uzunliklari (misol):", uzunliklar)

# 4
raqamlar_yigindi_juft = tuple(n for n in range(1, 101) if sum(int(d) for d in str(n)) % 2 == 0)
print("4) raqamlar yig'indisi juft bo'lganlar (tuple):")
print(raqamlar_yigindi_juft)
print("   bunday sonlar soni:", len(raqamlar_yigindi_juft))

# 5
sozlar = ["python", "tuple", "set", "loop"]
birinchi_harflar = tuple(s[0] for s in sozlar)
print("5) birinchi harflar:", birinchi_harflar)
