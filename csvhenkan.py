import csv
import sys
import os
import customexception as cex

# メイン処理実行
def main_run():
    print("メイン処理を実行します。")
    try:
        # print(sys.argv[0])
        # print(sys.argv[1])

        try:
            args1 = sys.argv[1]
        except IndexError as e:
            print("ファイルのパスが指定されていません。")
        except Exception as e:
            print(e)
    
        if os.path.isfile(args1):
            print("ファイルが存在します。")
            csvfile_path = args1
        elif os.path.isfile(os.getcwd() + "\\" + args1):
            print("ファイル名のファイルは、カレントディレクトリに存在します。")
            csvfile_path = os.getcwd() + "\\" + args1
        else:
            print("ファイルが存在しません。")
            raise cex.CustArgNoFilePathNoFilePathException(args1)
    except Exception as e:
        print(e)
        raise Exception

if __name__ == '__main__':
    print('処理を開始します。')
    main_run()
    
    