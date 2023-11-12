import sys
from email import utils
from email.parser import BytesParser
from email.parser import Parser
from email import policy


##メイン処理
if __name__ == '__main__':
##    print('main実行')
    email_file = open(r'C:\Users\lawin_envncw5\OneDrive\デスクトップ\お客様のApple IDがWebブラウザからiCloudへのサインインに使用されました。.eml')
    msg = BytesParser(policy=policy.default).parse(email_file)

    print('Date:', msg['date'])
