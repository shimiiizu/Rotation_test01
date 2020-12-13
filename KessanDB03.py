"""
KessanProのxlsファイルをもとに、決算情報のDBを作成する
KessanModuleを使用する

"""

import KessanModule03 as kessan
import pandas as pd

List = pd.read_excel('./xls/Tickers.xls', encoding="SHIFT-JIS") # 全銘柄
Tics = List['コード'][:] # リスト化

print(Tics[0])

for code in Tics:
    print(type(code))
    if code == Tics[0]: # 始めにベースとあるデータフレームを用意する
        df_concat = kessan.dbmaker(code)
        # データフレーム全体を表示する
        pd.set_option('display.max_rows', None)
        pd.set_option('display.max_columns', None)
        pd.set_option('display.width', None)
        pd.set_option('display.max_colwidth', -1)
        print(df_concat)
    else:
        print(code)
        try:
            df_concat = pd.concat([df_concat,kessan.dbmaker(code)])
            print(df_concat)
            df_concat.to_csv('F:/XBRL/DB/kessanDB3.csv')
        except:
            print("Error")

