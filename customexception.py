"""
カスタムの例外を定義したモジュール

"""

class CustBaseException(Exception):
    """
    カスタム例外の基底となる例外

    Attributes
    ----------
    arg : str
        例外の引数を文字列で保持
    """
    def __init__(self, arg=""):
        """
        初期化処理
        例外の引数を例外のクラス変数に保持
        """
        self.arg = arg

class CustArgNoFilePathNoFilePathException(CustBaseException):
    """
    引数に指定された文字列がファイルパスでない場合の例外
    """
    def __str__(self):
        """
        例外を文字列で出力するメッセージを下記のような形に変更
        引数に指定された[{引数}]は正しいファイルのパスではありません
        """
        return (
            f"引数に指定された[{self.arg}]は正しいファイルのパスではありません"
        )
