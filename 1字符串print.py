print('HELLO')
print("hello")

year = "虎"
print('龙' + year)
print('龙', year)

year = "虎"
print("龙" + year + "年")
print("龙", year, "年")

# format方法格式化字符串?怎么赋值？
contacts = ['老林', '老余', '老张']
year = '虎'
for name in contacts:
    print('''
    律回春渐，新元肇启。
    新岁甫至，福气东来。
    金''' + year + '''贺岁，欢乐祥瑞。
    金''' + year + '''敲门，五福临门。
    给''' + name + '''及家人拜年啦！
    新春快乐，''' + year + '''年大吉！
    '''.format(year, name))

for name in contacts:
    print(f'''
    律回春渐，新元肇启。
    新岁甫至，福气东来。
    金{year}贺岁，欢乐祥瑞。
    金{year}敲门，五福临门。
    给{name}及家人拜年啦！
    新春快乐，{year}年大吉！
    ''')
