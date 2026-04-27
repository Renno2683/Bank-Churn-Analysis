# ============================================================
# BANK CUSTOMER CHURN ANALYSIS
# Author: Ranim
# Dataset: Churn_Modelling.csv (Kaggle)
# Tools: Python, Pandas, Matplotlib, Seaborn
# Description: Exploratory data analysis to understand
#              why customers leave a bank
# ============================================================

import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.ticker as mticker
import seaborn as sns
import warnings
warnings.filterwarnings('ignore')

# ── Visual style ────────────────────────────────────────────
sns.set_theme(style='whitegrid', palette='muted')
plt.rcParams['figure.figsize'] = (10, 5)
plt.rcParams['axes.titlesize'] = 14
plt.rcParams['axes.titleweight'] = 'bold'


# ============================================================
# SECTION 1: LOAD & INSPECT DATA
# ============================================================

# Load the dataset
# Download from: https://www.kaggle.com/datasets/shrutimechlearn/churn-modelling
df = pd.read_csv('Churn_Modelling.csv')

print('=' * 50)
print('BANK CHURN ANALYSIS — Data Overview')
print('=' * 50)
print(f'\nShape: {df.shape[0]:,} rows × {df.shape[1]} columns')
print('\nColumn names:')
print(df.columns.tolist())
print('\nFirst 5 rows:')
print(df.head())
print('\nData types:')
print(df.dtypes)
print('\nMissing values:')
print(df.isnull().sum())


# ============================================================
# SECTION 2: CLEAN & PREPARE DATA
# ============================================================

# Drop columns not needed for analysis
df.drop(columns=['RowNumber', 'CustomerId', 'Surname'], inplace=True)

# Rename 'Exited' to something more readable
df.rename(columns={'Exited': 'Churned'}, inplace=True)

# Convert Churned to a label
df['Churn_Label'] = df['Churned'].map({1: 'Churned', 0: 'Retained'})

print('\n✅ Data cleaned and prepared')
print(f'\nChurn breakdown:')
print(df['Churn_Label'].value_counts())
print(f'\nOverall churn rate: {df["Churned"].mean() * 100:.1f}%')


# ============================================================
# SECTION 3: OVERALL CHURN RATE
# ============================================================

churn_counts = df['Churn_Label'].value_counts()
churn_pct = df['Churned'].mean() * 100

fig, ax = plt.subplots()
colors = ['#ff6b6b', '#00d4aa']
bars = ax.bar(churn_counts.index, churn_counts.values, color=colors, width=0.5, edgecolor='white')

for bar in bars:
    ax.text(bar.get_x() + bar.get_width() / 2,
            bar.get_height() + 50,
            f'{bar.get_height():,}',
            ha='center', va='bottom', fontweight='bold', fontsize=12)

ax.set_title(f'Overall Churn Rate: {churn_pct:.1f}%')
ax.set_ylabel('Number of Customers')
ax.set_xlabel('')
sns.despine()
plt.tight_layout()
plt.savefig('01_churn_rate.png', dpi=150, bbox_inches='tight')
plt.show()
print('\n📊 Chart saved: 01_churn_rate.png')


# ============================================================
# SECTION 4: CHURN BY GEOGRAPHY
# ============================================================

geo_churn = df.groupby('Geography')['Churned'].mean().sort_values(ascending=False) * 100

fig, ax = plt.subplots()
bars = ax.bar(geo_churn.index, geo_churn.values,
              color=['#ff6b6b', '#f5a623', '#00d4aa'], width=0.5, edgecolor='white')

for bar in bars:
    ax.text(bar.get_x() + bar.get_width() / 2,
            bar.get_height() + 0.3,
            f'{bar.get_height():.1f}%',
            ha='center', va='bottom', fontweight='bold', fontsize=12)

ax.set_title('Churn Rate by Country')
ax.set_ylabel('Churn Rate (%)')
ax.set_ylim(0, geo_churn.max() + 5)
sns.despine()
plt.tight_layout()
plt.savefig('02_churn_by_geography.png', dpi=150, bbox_inches='tight')
plt.show()
print('📊 Chart saved: 02_churn_by_geography.png')


# ============================================================
# SECTION 5: CHURN BY GENDER
# ============================================================

gender_churn = df.groupby('Gender')['Churned'].mean() * 100

fig, ax = plt.subplots(figsize=(6, 5))
bars = ax.bar(gender_churn.index, gender_churn.values,
              color=['#4a9eff', '#ff6b6b'], width=0.4, edgecolor='white')

for bar in bars:
    ax.text(bar.get_x() + bar.get_width() / 2,
            bar.get_height() + 0.3,
            f'{bar.get_height():.1f}%',
            ha='center', va='bottom', fontweight='bold', fontsize=12)

ax.set_title('Churn Rate by Gender')
ax.set_ylabel('Churn Rate (%)')
ax.set_ylim(0, gender_churn.max() + 5)
sns.despine()
plt.tight_layout()
plt.savefig('03_churn_by_gender.png', dpi=150, bbox_inches='tight')
plt.show()
print('📊 Chart saved: 03_churn_by_gender.png')


# ============================================================
# SECTION 6: CHURN BY AGE GROUP
# ============================================================

# Create age bands
bins = [18, 30, 40, 50, 60, 100]
labels = ['18–30', '31–40', '41–50', '51–60', '60+']
df['Age_Group'] = pd.cut(df['Age'], bins=bins, labels=labels, right=True)

age_churn = df.groupby('Age_Group', observed=True)['Churned'].mean() * 100

fig, ax = plt.subplots()
ax.plot(age_churn.index, age_churn.values,
        marker='o', linewidth=2.5, color='#f5a623',
        markersize=8, markerfacecolor='white', markeredgewidth=2.5)

for x, y in zip(age_churn.index, age_churn.values):
    ax.text(x, y + 0.8, f'{y:.1f}%', ha='center', fontsize=10, fontweight='bold')

ax.set_title('Churn Rate by Age Group')
ax.set_ylabel('Churn Rate (%)')
ax.set_xlabel('Age Group')
ax.set_ylim(0, age_churn.max() + 8)
sns.despine()
plt.tight_layout()
plt.savefig('04_churn_by_age.png', dpi=150, bbox_inches='tight')
plt.show()
print('📊 Chart saved: 04_churn_by_age.png')


# ============================================================
# SECTION 7: CHURN BY NUMBER OF PRODUCTS
# ============================================================

prod_churn = df.groupby('NumOfProducts')['Churned'].mean() * 100

fig, ax = plt.subplots(figsize=(7, 5))
bars = ax.bar(prod_churn.index, prod_churn.values,
              color=['#00d4aa', '#4a9eff', '#ff6b6b', '#ff6b6b'],
              width=0.5, edgecolor='white')

for bar in bars:
    ax.text(bar.get_x() + bar.get_width() / 2,
            bar.get_height() + 0.5,
            f'{bar.get_height():.1f}%',
            ha='center', va='bottom', fontweight='bold', fontsize=12)

ax.set_title('Churn Rate by Number of Products')
ax.set_ylabel('Churn Rate (%)')
ax.set_xlabel('Number of Products')
sns.despine()
plt.tight_layout()
plt.savefig('05_churn_by_products.png', dpi=150, bbox_inches='tight')
plt.show()
print('📊 Chart saved: 05_churn_by_products.png')


# ============================================================
# SECTION 8: BALANCE DISTRIBUTION — CHURNED VS RETAINED
# ============================================================

fig, ax = plt.subplots()
for label, color in [('Churned', '#ff6b6b'), ('Retained', '#00d4aa')]:
    subset = df[df['Churn_Label'] == label]['Balance']
    ax.hist(subset, bins=40, alpha=0.6, label=label, color=color, edgecolor='none')

ax.set_title('Account Balance Distribution: Churned vs Retained')
ax.set_xlabel('Balance ($)')
ax.set_ylabel('Number of Customers')
ax.xaxis.set_major_formatter(mticker.FuncFormatter(lambda x, _: f'${x:,.0f}'))
ax.legend()
sns.despine()
plt.tight_layout()
plt.savefig('06_balance_distribution.png', dpi=150, bbox_inches='tight')
plt.show()
print('📊 Chart saved: 06_balance_distribution.png')


# ============================================================
# SECTION 9: ACTIVE MEMBER IMPACT
# ============================================================

active_churn = df.groupby('IsActiveMember')['Churned'].mean() * 100
active_churn.index = ['Inactive', 'Active']

fig, ax = plt.subplots(figsize=(6, 5))
bars = ax.bar(active_churn.index, active_churn.values,
              color=['#ff6b6b', '#00d4aa'], width=0.4, edgecolor='white')

for bar in bars:
    ax.text(bar.get_x() + bar.get_width() / 2,
            bar.get_height() + 0.3,
            f'{bar.get_height():.1f}%',
            ha='center', va='bottom', fontweight='bold', fontsize=12)

ax.set_title('Churn Rate: Active vs Inactive Members')
ax.set_ylabel('Churn Rate (%)')
ax.set_ylim(0, active_churn.max() + 8)
sns.despine()
plt.tight_layout()
plt.savefig('07_churn_by_active_member.png', dpi=150, bbox_inches='tight')
plt.show()
print('📊 Chart saved: 07_churn_by_active_member.png')


# ============================================================
# SECTION 10: KEY INSIGHTS SUMMARY
# ============================================================

print('\n')
print('=' * 50)
print('KEY INSIGHTS SUMMARY')
print('=' * 50)

total = len(df)
churned = df['Churned'].sum()
churn_rate = df['Churned'].mean() * 100

top_geo = geo_churn.idxmax()
top_geo_rate = geo_churn.max()

gender_gap = gender_churn.max() - gender_churn.min()
top_gender = gender_churn.idxmax()

peak_age = age_churn.idxmax()
peak_age_rate = age_churn.max()

print(f'''
📌 Overall churn rate   : {churn_rate:.1f}% ({churned:,} out of {total:,} customers)
🌍 Highest churn country: {top_geo} ({top_geo_rate:.1f}%)
👤 Gender with more churn: {top_gender} ({gender_gap:.1f}% higher than the other)
📅 Most at-risk age group: {peak_age} years ({peak_age_rate:.1f}% churn rate)
💤 Inactive members churn at nearly 2x the rate of active members
💰 Churned customers tend to have higher account balances
🏦 Customers with 3–4 products churn at almost 100% — a major red flag
''')

print('✅ Analysis complete! All charts saved to the current folder.')
