# coding: utf-8

import json
import openai
from openai import OpenAI
import datetime

openai.api_key = "XXX"

class gpt:
    def __init__(self):
        self.JST = datetime.timezone(datetime.timedelta(hours=+9), 'JST')
        self.res = {"datetime": "", "message": ""}

    def __call__(self):
        print("gpt access modules.")
    
    def get_json(self, df):
        client = OpenAI()

        completion = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "user", "content": f"""
                    ユーザーのTodoを管理するツールにおいて、次のデータから特徴と今後の利用予測を多角的にまとめてください。
                    ・日付：{df.date}
                    ・ユーザー上限：{df.user_limit}
                    ・有効なユーザー：{df.enable_user}
                    ・ログイン回数：{df.login_num}
                    ・ストレージ利用状況：{df.usage}
                    ・登録済みタスク：{df.tasks}
                """}
            ]
        )

        return completion