import clipboard


def make_for_one_ship(str):
    str = str.lower()
    str = str.replace("chuyển khoản", "/")
    str = str.replace(" ", "")
    str = str.replace("một", "1")
    str = str.replace("hai", "2")
    str = str.replace("ba", "3")
    str = str.replace("bốn", "4")
    str = str.replace("năm", "5")
    str = str.replace("sáu", "6")
    str = str.replace("bảy", "7")
    str = str.replace("tám", "8")
    str = str.replace("chín", "9")
    str = str.replace("không", "0")

    result = str.replace(",", "*")
    return result


if __name__ == '__main__':
    list_data = [
        {'Khải': '16296,1 6356,1 6243,16328 chuyển khoản, 16274,1 6263,1 6311,1 6269,1 6251,16 ba ba 9,16359 chuyển khoản, 16358,1 6283,1 6291,1 6288,1 6258,16218.01,16295 , 16336,1 6341,1 6304,1 6343,1 6250,16323 chuyển khoản'},
        {'Đoàn ': '16264.01,1 6231,16267 chuyển khoản, 16254,1 6281,1 6270,1 6238,1 6237,1 6230,1 6287,1 6285,1 6284,1 6345,1 6310,1 6305,1 6275, 16347 chuyển khoản, 163 năm ba, 16357,16337.01,1 6282,16314.01,1 6317,1 6302,1 6303,1 6215,1 6312,16257, 16327 chuyển khoản, 16322,16297.01,1 6299,16326'},
        {'Hiếu': '16344,1 6319,1 6272,1 6278,1 6338,1 6313,1 6321,16309 chuyển khoản, 16227.01,1 6352,1 6351,1 6350,1 6329,1 6355,1 6308,1 6232,1 6246,1 6245,16273 , 16256,1 6219,1 6289,1 6286,1 6241,16265'},
        {'Chiến': '16334,1 6293,1 6346,1 6307,1 6324,16342 chuyển khoản, 16298,1 6330,1 6335,1 6301,1 6271,1 6236,16249 chuyển khoản, 16234,1 6247,1 6221,1 6223,1 6266,1 6222,16224 , 16259,16276'},
        {'Thành': '16332,1 6294,1 6292,1 6306,1 6325,1 6300,1 6340,1 6354,1 6280,1 6320,1 6235,1 6279,1 6255,1 6253,16225.01,1 6216,1 6277,16233.01,1 6261,16220'},
        {'Thanh': '16290 chuyển khoản, 16244,16262'},
        {'Khách lẻ': '16331 chuyển khoản, 16318 chuyển khoản, 16316,1 6333,16315 chuyển khoản, 16348 chuyển khoản'}
    ]

    for item in list_data:
        shipper = list(item.keys())[0]
        value = list(item.values())[0]
        print('{}\n{}\n'.format(shipper, make_for_one_ship(value)))



    # print(result)
    # clipboard.copy(result)
