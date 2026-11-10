import pandas as pd
import matplotlib.pyplot as plt
import os

# 设置中文字体
plt.rcParams['font.sans-serif'] = ['SimHei', 'Microsoft YaHei', 'SimSun']
plt.rcParams['axes.unicode_minus'] = False

files = {
    '一中北': '初一一中北排行榜.xlsx',
    '三中': '初一三中排行榜(1).xlsx',
    '康一中': '初一康一中排行榜.xlsx'
}

bins = [0, 184, 230, 276, 322, 368, 414, float('inf')]
labels = [
    'F   184-',
    'E   184-229',
    'D   230-275',
    'C   276-321',
    'B   322-367',
    'A   368-413',
    'S   414+'
]

os.makedirs('charts', exist_ok=True)

for school_name, file_path in files.items():
    print(f"Processing {school_name}...")
    df = pd.read_excel(file_path, header=1)

    # 确保 '总分' 是数值类型
    df['总分'] = pd.to_numeric(df['总分'], errors='coerce')
    df = df.dropna(subset=['总分'])

    total_students = len(df)

    # 根据分数划分等级
    # right=False 表示区间为 [bins[i], bins[i+1])，这样 414 分会被划分到 S
    df['score_level'] = pd.cut(df['总分'], bins=bins, labels=labels, right=False)

    counts = df['score_level'].value_counts().reindex(labels)
    percentages = (counts / total_students * 100).round(2)

    fig, ax = plt.subplots(figsize=(10, 6))
    fig.patch.set_facecolor('#f8f9fa')
    ax.set_facecolor('#f8f9fa')

    # 绘制水平柱状图
    bars = ax.barh(labels, counts, color='#1f2937', height=0.6)

    # 添加数据标签
    for bar, count, pct in zip(bars, counts, percentages):
        width = bar.get_width()
        if pd.isna(count): count = 0
        if pd.isna(pct): pct = 0
        ax.text(width + total_students * 0.01, bar.get_y() + bar.get_height()/2,
                f'{int(count)}人 ({pct}%)',
                va='center', ha='left', fontsize=12, color='#374151')

    ax.set_xlim(0, max(counts) * 1.3)

    # 隐藏边框
    for spine in ax.spines.values():
        spine.set_visible(False)

    # 隐藏 x 轴刻度
    ax.xaxis.set_visible(False)
    ax.yaxis.set_tick_params(length=0)

    plt.title(f'{school_name} 分数段分布统计 (总人数: {total_students})', fontsize=16, pad=20)
    plt.tight_layout()

    save_path = f'charts/{school_name}_score_distribution.png'
    plt.savefig(save_path, dpi=300)
    plt.close()
    print(f"Saved {save_path}")

print("All done!")
