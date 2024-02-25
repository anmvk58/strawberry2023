SHIP_PATH = "C:\\Users\\AnMV\\Desktop\\Dâu\\input_sl.txt"

if __name__ == '__main__':
    f = open(SHIP_PATH, mode="r", encoding="utf-8")
    lines = f.readlines()

    list_sl = []

    for line in lines:
        line = line.replace("cb bi nhỡ", "combo_bi_nho")
        line = line.replace("cb bi", "combo_bi")
        temp = line.replace("\"","").replace("hộp quà ","").replace("  ", " ").split(" ")
        obj_temp = [temp[1].replace("\n", "").lower(), temp[0]]
        list_sl.append(obj_temp)
        # print(obj_temp)

    svip = 0
    vip = 0
    nho = 0
    bi = 0
    ve = 0
    combo_bi_nho = 0
    combo_bi = 0

    for obj in list_sl:
        if obj[0].lower() == "svip":
            svip += float(obj[1])
        if obj[0].lower() == "vip":
            vip += float(obj[1])
        if obj[0].lower() == "nhỡ":
            nho += float(obj[1])
        if obj[0].lower() == "bi":
            bi += float(obj[1])
        if obj[0].lower() == "ve":
            ve += float(obj[1])
        if obj[0].lower() == "combo_bi_nho":
            combo_bi_nho += float(obj[1])
        if obj[0].lower() == "combo_bi":
            combo_bi += float(obj[1])

    print("Svip: " + str(svip))
    print("Vip: " + str(vip))
    print("Nhỡ: " + str(nho + combo_bi_nho/2))
    print("Bi: " + str(bi + combo_bi_nho/2 + combo_bi*1.5))
    print("Ve: " + str(ve))
    # print("Combo bi nhỡ: " + str(combo_bi_nho))
    # print("Combo bi: " + str(combo_bi))
    print("Total: " + str(svip + vip + nho + bi + ve + combo_bi_nho/2 + combo_bi_nho/2 + combo_bi*1.5))
