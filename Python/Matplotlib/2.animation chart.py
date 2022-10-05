import pandas as pd
import bar_chart_race as bcr
df = pd.read_csv(r'H:\MyGitCodes\Python\Matplotlib\population.csv')
# data without','
df = pd.DataFrame(df)
# df=df.apply(pd.to_numeric)
print(df.dtypes)
bcr.bar_chart_race(df.set_index('year'), 'population.mp4', n_bars=10, title='Population by Country', bar_kwargs={'alpha': 1.0}, filter_column_colors=True)
# bar_chart_race.line_chart_race()
# bar_chart_race.bar_chart_race()
# bcr.bar_chart_race(
#     df=df,    # 第一个参数就是数据，这个数据格式必须是 pandas.DataFrame 格式,同时满足数据准备中所说的条件；
#     filename='bar_chart.mp4',   # 这个参数是生成文件的名字，一般为.mp4 & .gif；
#     orientation='h',    # 方向
#     sort='desc', # 排序
#     n_bars=6, # 限制条形图数量
#     fixed_order=False,  # 固定标签
#     fixed_max=True, # 固定轴的最大值
#     steps_per_period=10,   # 帧数设置
#     interpolate_period=False,  # 插入时间
#     # label_bars=True,   # 是否有label
#     bar_size=.95,   # 设置bar宽度 取值 0~1 之间；
#     period_label={'x': .99, 'y': .25, 'ha': 'right', 'va': 'center'},
#     # period_fmt='%B %d, %Y',  # 日期的格式设置
#     period_summary_func=lambda v, r: {'x': .99, 'y': .18,
#                                       's': r'Total weigth: {v.sum():,.0f}',
#                                       'ha': 'right', 'size': 8, 'family': 'Courier New'},
#     perpendicular_bar_func='median',
#     period_length=500,
#     # figsize=(5, 3),
#     # dpi=144,
#     # cmap='dark12',
#     title='COVID-19 Deaths by Country',
#     # title_size='',
#     # bar_label_size=7,
#     # tick_label_size=7,
#     shared_fontdict={'family' : 'DejaVu Sans', 'color' : '.1'},
#     scale='linear',
#     writer=None,
#     fig=None,
#     bar_kwargs={'alpha': .7},
#     filter_column_colors=False)
