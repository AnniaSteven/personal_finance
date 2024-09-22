import csv
from datetime import datetime

# 定义常量
INCOME_CATEGORIES = ["工资", "奖金", "投资收益", "其他"]
EXPENSE_CATEGORIES = ["餐饮", "交通", "购物", "娱乐", "住房", "其他"]

# 文件名
FILENAME = 'personal_finance.csv'

# 初始化文件
def init_file():
    try:
        with open(FILENAME, mode='r', newline='', encoding='utf-8'):
            pass
    except FileNotFoundError:
        with open(FILENAME, mode='w', newline='', encoding='utf-8') as file:
            writer = csv.writer(file)
            writer.writerow(["类型", "日期", "金额", "类别", "备注"])

# 记录收入
def record_income():
    date = input("请输入日期（格式YYYY-MM-DD）：")
    amount = float(input("请输入收入金额："))
    if amount <= 0:
        print("收入金额必须为正数！")
        return
    print("收入类别选项：", INCOME_CATEGORIES)
    category = input("请输入收入类别：")
    if category not in INCOME_CATEGORIES:
        print("无效的收入类别！")
        return
    note = input("请输入备注：")

    with open(FILENAME, mode='a', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        writer.writerow(["收入", date, amount, category, note])

    print("收入记录成功！")

# 记录支出
def record_expense():
    date = input("请输入日期（格式YYYY-MM-DD）：")
    amount = float(input("请输入支出金额："))
    if amount <= 0:
        print("支出金额必须为正数！")
        return
    print("支出类别选项：", EXPENSE_CATEGORIES)
    category = input("请输入支出类别：")
    if category not in EXPENSE_CATEGORIES:
        print("无效的支出类别！")
        return
    note = input("请输入备注：")

    with open(FILENAME, mode='a', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        writer.writerow(["支出", date, amount, category, note])

    print("支出记录成功！")

# 查询记录
def query_records():
    print("1. 查询所有记录")
    print("2. 按日期查询")
    print("3. 按类别查询")
    choice = input("请选择查询方式：")

    with open(FILENAME, mode='r', newline='', encoding='utf-8') as file:
        reader = csv.reader(file)
        records = list(reader)

    if choice == "1":
        for record in records[1:]:
            print(record)

    elif choice == "2":
        query_date = input("请输入要查询的日期（格式YYYY-MM-DD）：")
        for record in records[1:]:
            if record[1] == query_date:
                print(record)

    elif choice == "3":
        query_category = input("请输入要查询的类别：")
        for record in records[1:]:
            if record[3] == query_category:
                print(record)

    else:
        print("无效的查询方式！")

# 统计功能
def show_statistics():
    income_total = 0
    expense_total = 0

    with open(FILENAME, mode='r', newline='', encoding='utf-8') as file:
        reader = csv.reader(file)
        next(reader)  # 跳过标题行

        for record in reader:
            amount = float(record[2])
            if record[0] == "收入":
                income_total += amount
            elif record[0] == "支出":
                expense_total += amount

    print(f"总收入：{income_total} 元")
    print(f"总支出：{expense_total} 元")
    print(f"结余：{income_total - expense_total} 元")

# 主菜单
def main_menu():
    init_file()  # 初始化文件

    while True:
        print("\n------ 个人账单管理系统 ------")
        print("1. 记录收入")
        print("2. 记录支出")
        print("3. 查询记录")
        print("4. 显示统计")
        print("5. 退出")
        choice = input("请选择操作：")

        if choice == "1":
            record_income()
        elif choice == "2":
            record_expense()
        elif choice == "3":
            query_records()
        elif choice == "4":
            show_statistics()
        elif choice == "5":
            print("感谢使用，再见！")
            break
        else:
            print("无效选择，请重新输入。")

if __name__ == '__main__':
    main_menu()
