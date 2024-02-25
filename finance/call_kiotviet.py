import os

import openpyxl
import pandas as pd
from datetime import datetime
import dataframe_image as dfi

import xlsxwriter

from make_df_shipper import make_shipper
import numpy as np

filename = datetime.today().strftime('%Y%m%d')
# filename = "20240205"

BASE_PATH = "C:\\Users\\AnMV\\Desktop\\Dâu"
KIOT_PATH = "{}\\{}.xlsx".format(BASE_PATH, filename)
SHIP_PATH = "{}\\input_ship.txt".format(BASE_PATH)


def calculate_for_one_ship(df, shipper_name):
    df_notchuyenkhoan = df.loc[df['CK'] != 'C']
    tong_tien = sum(df_notchuyenkhoan['Tổng tiền hàng'])
    tong_don = df.shape[0]
    tien_ship = tong_don * 25000
    phai_thu = tong_tien - tien_ship

    data = [['Tổng tiền', tong_tien], ['Tiền ship', tien_ship], ['Cắt ship', 0], ['Phải thu', phai_thu]]
    df_result = pd.DataFrame(data, columns=['Shipper', shipper_name])
    return df_result, tong_tien, tien_ship, phai_thu


if __name__ == '__main__':
    df_shipper = make_shipper(SHIP_PATH)

    df_kiotviet = pd.read_excel(KIOT_PATH)

    df_total = pd.merge(df_kiotviet, df_shipper, left_on=['Mã hóa đơn'], right_on=['Code'], how="left")

    list_shipper = df_shipper['Shipper'].unique()

    # Duplicate column
    df_total['Total money'] = df_total.loc[:, 'Tổng tiền hàng']
    # Reorder column
    df_total = df_total[
        ['Mã hóa đơn', 'Khách hàng', 'Điện thoại', 'Địa chỉ (Khách hàng)', 'Shipper', 'CK', 'Tổng tiền hàng',
         'Total money']]

    df_total["Tổng tiền hàng"] = np.where(df_total["CK"] == "C", 0, df_total["Tổng tiền hàng"])

    writer = pd.ExcelWriter(f"{BASE_PATH}\\{filename}_result.xlsx", engine='xlsxwriter')
    df_total.to_excel(writer, sheet_name='Invoices', index=False)

    total_shipper_df = pd.DataFrame()
    # export images
    try:
        os.mkdir(f"{BASE_PATH}\\{filename}")
    except:
        print("Thư mục đã tồn tại")

    for ship in list_shipper:
        df_ship = df_total.loc[df_total['Shipper'] == ship]
        df_cal, tong_tien, tien_ship, phai_thu = calculate_for_one_ship(df_ship, ship)

        total_shipper_df = pd.concat([total_shipper_df, df_cal], axis=1)

        df_ship = df_ship.astype({"Điện thoại": str})

        df_cal.to_excel(writer, sheet_name=ship, index=False, startrow=0, startcol=0)
        df_ship.to_excel(writer, sheet_name=ship, index=False, startrow=df_cal.shape[0] + 2, startcol=0)

        data = [
            ['', '', '', '', '', 'Tổng tiền', tong_tien, ''],
            ['', '', '', '', '', 'Tiền ship', tien_ship, ''],
            ['', '', '', '', '', 'Phải thu', phai_thu, '']
        ]

        # Create the pandas DataFrame
        temp_df = pd.DataFrame(data,
                               columns=['Mã hóa đơn', 'Khách hàng', 'Điện thoại', 'Địa chỉ (Khách hàng)', 'Shipper',
                                        'CK', 'Tổng tiền hàng', 'Total money'])

        # format width
        sheet = writer.sheets[ship]
        sheet.set_column(0, 0, 13)
        sheet.set_column(1, 1, 20)
        sheet.set_column(2, 2, 12)
        sheet.set_column(3, 3, 70)
        sheet.set_column(4, 4, 8)
        sheet.set_column(5, 5, 5)
        sheet.set_column(6, 6, 10)

        # ship_df = df_ship.append(temp_df, ignore_index=True)
        ship_df = pd.concat([df_ship, temp_df], ignore_index=True)
        dfi.export(ship_df, "{}\\{}\\{}.png".format(BASE_PATH, filename, ship), dpi=150)

        # print(df_cal)
        print("---")

    total_shipper_df.to_excel(writer, sheet_name="Total", index=False, startrow=df_cal.shape[0] + 2, startcol=0)
    writer.close()

    # workbook = xlsxwriter.Workbook.(f"{BASE_PATH}\\{filename}_result.xlsx")
    # for ship in list_shipper:
    #     print(ship)
    #     ws = workbook.get_worksheet_by_name(ship)
    #     ws.set_column(1, 1, 25)
    #
    # workbook.close()
    print('a')
