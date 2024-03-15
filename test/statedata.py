# coding: utf-8

# state情報となるログデータのサンプルを作成
# ToDo管理を目的としたクラウドサービスのログイン数、タスク作成数、有効ユーザー数、ストレージ利用数のデータを日次で記録

import numpy as np
import numpy.random as random
import pandas as pd
import csv
import os
import datetime

# ユーザー情報を取得
user_df = pd.read_csv("/workspace/data/user.csv", encoding="utf8")
# ユーザーごとに作成したログを一時的に保管する変数を作成
for user in user_df["id"]:
    logs = {user: {}}

# 最終取得日を設定
current_date = datetime.date(2024, 2, 29)

# 個人ごとの環境条件の設定
id_1 = {
    "contract_start_date": datetime.date(2023, 4, 1),
    "contract_user": 10,
    "contract_enable_user": 7,
    "contract_storage": 50,
    "max_tasks": 500
}
id_2 = {
    "contract_start_date": datetime.date(2023, 5, 1),
    "contract_user": 10,
    "contract_enable_user": 10,
    "contract_storage": 10,
    "max_tasks": 250
}
id_3 = {
    "contract_start_date": datetime.date(2023, 6, 1),
    "contract_user": 15,
    "contract_enable_user": 12,
    "contract_storage": 20,
    "max_tasks": 700
}
id_4 = {
    "contract_start_date": datetime.date(2023, 7, 1),
    "contract_user": 20,
    "contract_enable_user": 20,
    "contract_storage": 50,
    "max_tasks": 1300
}
id_5 = {
    "contract_start_date": datetime.date(2023, 8, 1),
    "contract_user": 10,
    "contract_enable_user": 3,
    "contract_storage": 30,
    "max_tasks": 550
}

def usage_log(logs, param, current_date):
    logs = {
        "dates": [],
        "users": [],
        "en_users": [],
        "login_num": [],
        "usage": [],
        "tasks": []
    }
    try:
        report_between = current_date - param["contract_start_date"]
        user_vector = np.linespace(1, param["contract_enable_user"], report_between.days)
        storage_vector = np.linespace(0.1, param["contract_storage"]*0.9, report_between.days)
        task_vector = np.linespace(1, param["max_tasks"], report_between.days)
        for i in range(report_between.days):
            user_limit = param["contract_user"]
            enable_user = np.ceil(user_vector[i])
            login_num = random.randint(0, enable_user)
            use_storage = storage_vector[i]
            created_task = task_vector[i]
            
            logs["dates"].append(param["contranct_start_date"]+(i+1))
            logs["users"].append(user_limit)
            logs["en_users"].append(enable_user)
            logs["login_num"].append(login_num)
            logs["usage"].append(use_storage)
            logs["tasks"].append(created_task)
        
        return 0
    except Exception as e:
        return e


id_1_fb = usage_log(logs["1"], id_1, current_date)
id_2_fb = usage_log(logs["2"], id_2, current_date)
id_3_fb = usage_log(logs["3"], id_3, current_date)
id_4_fb = usage_log(logs["4"], id_4, current_date)
id_5_fb = usage_log(logs["5"], id_5, current_date)


if os.path.isfile("/workspace/data/state.csv"):
    with open("/workspace/data/state.csv", "w", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerow = ["date", "userid", "user_limit", "enable_user", "login_num", "usage", "tasks"]
        for i in range((current_date - id_1["contract_start_date"]).days):
            aaa




