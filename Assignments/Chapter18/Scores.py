import pandas as pd
import matplotlib.pyplot as plt

data = {
    'Week': ['Week1', 'Week2', 'Week3', 'Week4', 'Week5'],
    'Assmt': [90, 98, 80, 85, 93],
    'Quiz': [89, 85, 89, 94, 78]
}

df = pd.DataFrame(data)

df['Quiz'] = (df['Quiz'] / 20) * 100

file_name = 'sanju.xlsx'
df.to_excel(file_name, index=False)

df = pd.read_excel(file_name, index_col='Week')

plt.figure(figsize=(10, 6))
plt.plot(df.index, df['Assmt'], marker='o', label='Assignment Score')
plt.plot(df.index, df['Quiz'], marker='o', label='Quiz Score')
plt.title('srinivas muniganti')
plt.xlabel('Week')
plt.ylabel('Score')
plt.legend()
plt.grid(True)
plt.xticks(rotation=45)
plt.tight_layout()

plt.show()
