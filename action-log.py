import os
import csv
import datetime


# 入力
def input_text():
    input_overview = input("やったことを教えてください：")
    input_time = input("何分作業しましたか？：")
    input_comment = input("メモしたいことがあれば書いてください：")
    return input_overview, input_time, input_comment


# csv読み込み
def csv_read(dst_path, write_overview, write_time, write_comment):
    now = datetime.datetime.now()
    now_date = now.strftime("%Y-%m-%d")
    now_time = now.strftime("%H:%M")
    with open(dst_path, mode="a", encoding='utf8', newline='') as f:
        csvwriter = csv.writer(f)
        if os.stat(dst_path).st_size == 0:
            columns = ["date","time","overview","time","comment"]
            csvwriter.writerow(columns)
        new_data = [[now_date, now_time, write_overview, write_time, write_comment]]
        csvwriter.writerows(new_data)


root_dir = "I:\\09_ジャンクボックス\\094_ナレッジ・体調ログ\\行動ログ"
date_base = datetime.datetime.today()
month_file = f"{date_base:%Y-%m}.csv"
full_path = os.path.join(root_dir, month_file)

overview, time, comment = input_text()
csv_read(full_path, overview, time, comment)
