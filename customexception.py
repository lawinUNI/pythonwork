"""
カスタムの例外を定義したモジュール

"""

class CustBaseException(Exception):
    """
    カスタム例外の基底となる例外

    Attributes
    ----------
    arg1 : str
        例外の原因となった要因（文字列や数値など）を第１引数として受け取ったもの
    arg2 : str
        例外が発生した場所を第２引数として受け取ったもの
    """
    def __init__(self, arg1="", arg2=""):
        """
        初期化処理
        例外の引数を例外のクラス変数に保持
        """
        self.arg1 = arg1
        self.arg2 = arg2

class CustArgNoFilePathNoFilePathException(CustBaseException):
    """
    引数に指定された文字列がファイルパスでない場合の例外
    """
    def __str__(self):
        """
        例外を文字列で出力するメッセージを下記のような形にする。
        発生原因：引数に指定された[引数１]は正しいファイルのパスではありません。\n発生場所：[引数２]
        """
        return (
            f"\n発生原因：引数に指定された[{self.arg1}]は正しいファイルのパスではありません。\n発生場所：[{self.arg2}]"
        )

class CustArgNoSetException(CustBaseException):
    """
    必要な引数が指定されていない場合の例外
    """
    def __str__(self):
        """
        例外を文字列で出力するメッセージを下記のような形にする。
        発生原因：引数に[引数１]がセットされていません。\n発生場所：[引数２]
        """
        return (
            f"\n発生原因：引数に[{self.arg1}]がセットされていません。\n発生場所：[{self.arg2}]"
        )
