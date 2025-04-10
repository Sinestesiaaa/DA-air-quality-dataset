import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st
import numpy as np

sns.set(style="whitegrid", font_scale=1.0)

def sort_by_pollutants(df, pollutants):
    return df.groupby('station')[pollutants].mean()

def plot_monthly_trend(df, pollutant, year=""):
    month_label = ['Jan','Feb','Mar','Apr','Mei','Jun','Jul','Agu','Sept','Okt','Nov','Des']
    plt.figure(figsize=(8, 4))
    if year:
        sns.lineplot(x='month', y=pollutant, data=df, marker='o')
    else:
        sns.lineplot(x='month', y=pollutant, hue='year', data=df, marker='o', palette='viridis')
        plt.legend(title='Tahun', bbox_to_anchor=(1, 1), loc='upper right')
    plt.title(f'Tren Bulanan {pollutant} {year if year else "2013–2017"}')
    plt.xlabel('Bulan')
    plt.ylabel(f'{pollutant} \u03BCg/m\u00B3')
    plt.xticks(range(1, 13), month_label)
    plt.grid(True)
    plt.tight_layout()
    return plt

all_df = pd.read_csv("./data/imputed_df.csv")

if 'datetime' not in all_df.columns:
    all_df["datetime"] = pd.to_datetime(all_df[["year", "month", "day"]])

all_df.sort_values(by="datetime", inplace=True)

pollutants = ['PM2.5', 'PM10', 'SO2', 'NO2', 'CO', 'O3']
env_vars = ['TEMP', 'PRES', 'DEWP', 'RAIN', 'WSPM']
col_interest = pollutants + env_vars

colors = {
    'PM2.5': 'Reds_r',
    'PM10': 'Oranges_r',
    'SO2': 'Purples_r',
    'NO2': 'Greens_r',
    'CO': 'Blues_r',
    'O3': 'Greys_r'
}

st.set_page_config(layout="wide")
st.header('Dashboard Monitoring Kualitas Udara Tiongkok :cn: :foggy:')

min_date = all_df["datetime"].min()
max_date = all_df["datetime"].max()

st.subheader('Peringkat Rata-rata Polusi per Stasiun')

start_date, end_date = st.date_input(
    label="Pilih Periode Data",
    value=[min_date, max_date],
    min_value=min_date,
    max_value=max_date
)

main_df = all_df[(all_df["datetime"] >= str(start_date)) & (all_df["datetime"] <= str(end_date))]
rank_df = sort_by_pollutants(main_df, pollutants)
monthly_df = all_df.groupby(['year', 'month'])[pollutants].mean().reset_index()

pollutant_list = st.selectbox("Pilih jenis polutan", options=pollutants)
df_sorted = rank_df.sort_values(by=pollutant_list, ascending=False)

col1, col2 = st.columns(2)
with col1:
    highest_stat = df_sorted.index[0]
    highest_val = df_sorted[pollutant_list].iloc[0]
    st.metric(f'Tertinggi ({highest_stat})', f'{highest_val:.3f} \u03BCg/m\u00B3')
with col2:
    lowest_stat = df_sorted.index[-1]
    lowest_val = df_sorted[pollutant_list].iloc[-1]
    st.metric(f'Terendah ({lowest_stat})', f'{lowest_val:.3f} \u03BCg/m\u00B3')

fig, ax = plt.subplots(figsize=(18, 10))
station_rank = df_sorted[pollutant_list]
plot_df = pd.DataFrame({
    'station': station_rank.index,
    'value': station_rank.values,
    'hue': station_rank.index
})

sns.barplot(
    data=plot_df,
    x='value', y='station', hue='hue',
    palette=colors.get(pollutant_list, 'Reds_r'),
    dodge=False, legend=False, ax=ax
)

for j, value in enumerate(plot_df['value']):
    ax.text(value + 0.01 * value, j, f"{value:.1f}", va='center', fontsize=9)

ax.set_title(f"{pollutant_list} - Rata-rata per Stasiun", fontsize=14, weight='bold')
ax.set_xlabel(f'{pollutant_list} (\u03BCg/m\u00B3)', fontsize=12)
ax.set_ylabel('')
st.pyplot(fig)

st.subheader("Tren Rerata Polusi Bulanan")
years = st.selectbox("Pilih Tahun", options=all_df['year'].unique())
tren_df = monthly_df[monthly_df['year'] == years]
all_years = st.checkbox("Lihat Semua Tahun")

for i in pollutants:
    if all_years:
        chart = plot_monthly_trend(monthly_df, i)
    else:
        chart = plot_monthly_trend(tren_df, i, years)
    st.pyplot(plt)

st.subheader("Korelasi Kondisi Lingkungan dengan Polutan Udara")

correlation_df = all_df[col_interest]
correlation_matrix = correlation_df.corr()

plt.figure(figsize=(12, 10))
mask = np.triu(np.ones_like(correlation_matrix, dtype=bool))
cmap = sns.diverging_palette(220, 20, as_cmap=True)

sns.heatmap(
    correlation_matrix,
    mask=mask,
    cmap=cmap,
    annot=True,
    fmt=".2f",
    square=True,
    linewidths=.5,
    cbar_kws={"shrink": .75},
    annot_kws={"size": 9}
)

plt.title('Korelasi Antara Variabel Cuaca dan Polusi Udara', fontsize=14, fontweight='bold')
plt.xticks(rotation=45, ha='right')
plt.yticks(rotation=0)
plt.tight_layout()
st.pyplot(plt)
