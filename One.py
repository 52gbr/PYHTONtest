import requests

# 1.从链接页面获取公开数据
data = requests.get("https://iftp.chinamoney.com.cn/english/bdInfo/").content.decode('utf-8')
# 2. 需要获取数据的条件: Bond Type=Treasury Bond, Issue Year=2023
get_bond_type = "Treasury Bond"
get_issue_year = "2023"
# 4. 保存成有效csv文件
csv_filename = "filtered_bonds.csv"