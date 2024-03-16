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
logs = {}
for user in user_df["id"]:
    logs[user] = {}

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
        user_vector = np.linspace(1, param["contract_enable_user"], report_between.days)
        storage_vector = np.linspace(0.1, param["contract_storage"]*0.9, report_between.days)
        task_vector = np.linspace(1, param["max_tasks"], report_between.days)
        for i in range(report_between.days):
            user_limit = param["contract_user"]
            enable_user = np.ceil(user_vector[i])
            login_num = random.randint(0, enable_user)
            use_storage = np.round(storage_vector[i],1)
            created_task = np.ceil(task_vector[i])
            
            logs["dates"].append(param["contract_start_date"]+datetime.timedelta(days=(i)))
            logs["users"].append(user_limit)
            logs["en_users"].append(enable_user)
            logs["login_num"].append(login_num)
            logs["usage"].append(use_storage)
            logs["tasks"].append(created_task)
        
        return logs, 0
    except Exception as e:
        return e


logs[1], id_1_fb = usage_log(logs[1], id_1, current_date)
logs[2], id_2_fb = usage_log(logs[2], id_2, current_date)
logs[3], id_3_fb = usage_log(logs[3], id_3, current_date)
logs[4], id_4_fb = usage_log(logs[4], id_4, current_date)
logs[5], id_5_fb = usage_log(logs[5], id_5, current_date)

try:
    if os.path.isfile("/workspace/data/state.csv"):
        with open("/workspace/data/state.csv", "w", encoding="utf-8") as f:
            writer = csv.writer(f)
            writer.writerow(["date", "userid", "user_limit", "enable_user", "login_num", "usage", "tasks"])
            indexes = np.zeros(5, dtype=int)
            start_flag = [False, False, False, False, False]
            
            for i in range((current_date - id_1["contract_start_date"]).days):
                log_date = id_1["contract_start_date"] + datetime.timedelta(days=i)
                start_flag[0] = True if logs[1]["dates"][0] <= log_date else False
                start_flag[1] = True if logs[2]["dates"][0] <= log_date else False
                start_flag[2] = True if logs[3]["dates"][0] <= log_date else False
                start_flag[3] = True if logs[4]["dates"][0] <= log_date else False
                start_flag[4] = True if logs[5]["dates"][0] <= log_date else False
  
                if start_flag[0]:
                    writer.writerow([log_date, 1, logs[1]["users"][indexes[0]], logs[1]["en_users"][indexes[0]], logs[1]["login_num"][indexes[0]], logs[1]["usage"][indexes[0]], logs[1]["tasks"][indexes[0]]])
                    indexes[0] = indexes[0] + 1

                if start_flag[1]:
                    writer.writerow([log_date, 2, logs[2]["users"][indexes[1]], logs[2]["en_users"][indexes[1]], logs[2]["login_num"][indexes[1]], logs[2]["usage"][indexes[1]], logs[2]["tasks"][indexes[1]]])
                    indexes[1] = indexes[1] + 1

                if start_flag[2]:
                    writer.writerow([log_date, 3, logs[3]["users"][indexes[2]], logs[3]["en_users"][indexes[2]], logs[3]["login_num"][indexes[2]], logs[3]["usage"][indexes[2]], logs[3]["tasks"][indexes[2]]])
                    indexes[2] = indexes[2] + 1

                if start_flag[3]:
                    writer.writerow([log_date, 4, logs[4]["users"][indexes[3]], logs[4]["en_users"][indexes[3]], logs[4]["login_num"][indexes[3]], logs[4]["usage"][indexes[3]], logs[4]["tasks"][indexes[3]]])
                    indexes[3] = indexes[3] + 1

                if start_flag[4]:
                    writer.writerow([log_date, 5, logs[5]["users"][indexes[4]], logs[5]["en_users"][indexes[4]], logs[5]["login_num"][indexes[4]], logs[5]["usage"][indexes[4]], logs[5]["tasks"][indexes[4]]])
                    indexes[4] = indexes[4] + 1
except Exception as e:
    print(e)


