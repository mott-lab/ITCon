import numpy as np # linear algebra
import pandas as pd # data processing, CSV file I/O (e.g. pd.read_csv)
import matplotlib.pyplot as plt
import seaborn as sns
from collections import Counter

director_critic_counts = df_copy.groupby(df_copy['director_name'])['num_critic_for_reviews'].sum()
director_critic_indx = director_critic_counts.sort_values(ascending=False)[:20].index
director_critic_values = director_critic_counts.sort_values(ascending=False)[:20].values

fig,ax = plt.subplots(figsize=(8,6))
sns.barplot(x = director_critic_indx,
            y = director_critic_values,
            color='#90caf9',
            ax=ax)
ticks = plt.setp(ax.get_xticklabels(),rotation=90)
plt.title('Director vs critic')
plt.ylabel('Counter')
plt.xlabel('Director')
del fig,ax,ticks
