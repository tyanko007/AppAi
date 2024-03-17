# coding: utf8

import sys
import os
import pandas as pd


sys.path.append("/workspace")
from src import search

class main:
    def __init__(self):
        self.args = sys.argv
    
    def __call__(self):
        i = 0
        for char in self.args:
            print(f"args_{i}", char)
            i += 1
    
    def fin(self, message):
        print("script exit. becouse message :", message)
        sys.exit()

    def search(self):
        if len(self.args) > 3:
            print("this script given 2 keywords. has 3 given.")
        else:
            users_df = pd.read_csv("/workspace/data/user.csv", encoding="utf-8") if os.path.isfile("/workspace/data/user.csv") else self.fin("users.csv not found")
            state_df = pd.read_csv("/workspace/data/state.csv", encoding="utf-8") if os.path.isfile("/workspace/data/state.csv") else self.fin("state.csv not found")

            if self.args[1] == "佐藤 一郎":
                id = users_df.groupby("name").get_group(self.args[1])
                gpt = search.gpt()
                gpt()
                # gpt_json = gpt.get_json(state_df.groupby("id").get_group(id["id"][0]))

                # return gpt_json

if __name__ == "__main__":
    app = main()
    app()
    app.search()

                
