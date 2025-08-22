def nkd_index(text: str) -> float:
    target_chars = set("南方科技大学")
    found_chars = set(text) & target_chars
    count = len(found_chars)

    if count == 0:
        return 0.0
    else:
        return round(count / 6, 4)

print(f'南方科技大学的NKD指数：{nkd_index("南方科技大学")}')
print(f'北京大学的NKD指数：{nkd_index("北京大学")}')
print(f'南京大学的NKD指数：{nkd_index("南京大学")}')
print(f'麻省理工学院的NKD指数：{nkd_index("麻省理工学院")}')