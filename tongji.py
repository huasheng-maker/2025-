import pandas as pd

# # 读取Excel文件
# file_path = 'test1.xlsx'  # 替换为你的实际文件路径
# df = pd.read_excel(file_path)
#
# # 将销售日期列转换为datetime类型
# df['销售日期'] = pd.to_datetime(df['销售日期'])
#
# # 提取年份和月份
# df['年份'] = df['销售日期'].dt.year
# df['月份'] = df['销售日期'].dt.month
#
# # 按蔬菜种类、年份和月份分组，并计算销量总和
# monthly_sales = df.groupby(['分类名称', '年份', '月份'])['销量(千克)'].sum().reset_index()
#
# # 重命名列以便更清晰
# monthly_sales.rename(columns={'销量': '月销量'}, inplace=True)
#
# # 查看结果
# print(monthly_sales)
#
# # 如果需要将结果保存为新的Excel文件
# output_file_path = 'test_month_sales.xlsx'
# monthly_sales.to_excel(output_file_path, index=False)

# 读取excel文件
file_path='test1.xlsx'
df=pd.read_excel(file_path)

# 转换日期格式
df['销售日期']=pd.to_datetime(df['销售日期'],format='%Y-%m-%d')

# 获取年份与月份
df['年份']=df['销售日期'].dt.year
df['月份']=df['销售日期'].dt.month
df['日份']=df['销售日期'].dt.day

#按照【分类名称】、【年份】、【月份】、【日份】分组,得到每种品类的日销量
dayly_sales=df.groupby(['分类名称','年份','月份','日份']).agg({'销量(千克)':'sum'}).reset_index()
print(dayly_sales)

#将日销量的文件以csv/xlsx格式保存起来
dayly_output_file_path = 'test_day_sales.xlsx'
dayly_sales.to_excel(dayly_output_file_path,index=False)

#计算月销量的统计值
monthly_sales=dayly_sales.groupby(['分类名称','年份','月份']).agg({'销量(千克)':['sum','mean','median','max','min','std']}).reset_index()
print(monthly_sales)

#保存到test_month_sales文件
monthly_output_file_path = 'test_monthly_sales.xlsx'
monthly_sales.to_excel(monthly_output_file_path,index=True)