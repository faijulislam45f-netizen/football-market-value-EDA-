import pandas as pd
import plotly.express as px

df = pd.read_csv('player_market_values.csv')
print(f"data loaded: {df.shape}")

# 1. Messi vs Ronaldo Comparison 
mvr = df[df['player_name'].isin(['Lionel Messi', 'Cristiano Ronaldo'])]
fig1 = px.line(mvr, x='year', y='market_value_eur_m', color='player_name', 
               title='Messi vs Ronaldo Market Value (2010-2026)', 
               labels={'market_value_eur_m': 'Market Value (€M)', 'year': 'Year'})
fig1.write_image('fig1_messi_ronaldo.png')
print("Fig1 Done")

 # 2. Position wise average market value
pos = df.groupby('position')['market_value_eur_m'].mean().reset_index()
fig2 = px.bar(pos, x='position', y='market_value_eur_m', 
              title='Average Market Value By Position', 
              labels={'market_value_eur_m': 'Avg Value (€M)', 'position': 'Position'})
fig2.write_image('fig2_position.png')
print("Fig2 Done")

# 3. Peak Age Distribution
peak = df[df['is_peak_year'] == 1]
print(f"Peak year avg age: {peak['age'].mean().round(1)}")
print(f"Total peak year players: {len(peak)}")
fig3 = px.histogram(peak, x='age', nbins=10, 
                    title='Age Distribution at Peak Market Value', 
                    labels={'age': 'Age', 'count': 'Number of players'}) 
fig3.write_image('fig3_peak_age.png')
print("fig3 Done")

# 4. Value declined after age 28
age_val = df[df['age']>= 28].groupby('age')['market_value_eur_m'].mean().reset_index()
fig4 = px.line(age_val, x='age', y='market_value_eur_m', 
             title='Average Market value by Age (28+)', 
             labels={'market_value_eur_m': 'Average Value (€M)', 'age': 'Age'})
fig4.write_image('fig4_peak_age.png')
print("fig4 Done")

# 5. Top 10 peak values
top10 = df.groupby('player_name')['market_value_eur_m'].max().reset_index()
top10 = top10.sort_values('market_value_eur_m', ascending=False).head(10)
fig5 = px.bar(top10, x='player_name', y='market_value_eur_m', 
              title='Top 10 Plyers by Peak Market Values', 
              labels={'market_value_eur_m': 'Peak Value (€M)', 'player_name': 'Player'})
fig5.write_image('fig5_top10.png')
print("fig5 Done") 

print("\nALL 5 CHARTS SAVED AS PNG")
