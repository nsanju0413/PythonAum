import pandas as pd
import matplotlib.pyplot as plt


data = {
    'Label': ['USA', 'UK', 'China', 'Russia', 'Germany'],
    'Value': [46, 27, 26, 19, 17]
}

df = pd.DataFrame(data)


file_name = 'gold-olympics23.xlsx'
df.to_excel(file_name, index=False)


df = pd.read_excel(file_name)


plt.figure(figsize=(8, 8))
plt.pie(df['Value'], labels=df['Label'], autopct='%1.1f%%', startangle=140)
plt.title('Prgm-B1')
plt.axis('equal')

plt.show()
