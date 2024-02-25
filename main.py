import pandas as pd
lst = ['robot'] * 10
lst += ['human'] * 10
random.shuffle(lst)
data = pd.DataFrame({'whoAmI': lst})
data.head()


unique_values = data['whoAmI'].uique() #Получаем уникальное значение из столбца 'whoAmI'
one_hot_data = pd.DataFrame()          #Создаем пустой DataFrame
#Для каждого уникального значения создаем новый столбец и заполняем его значениями 0 или 1 
for value in unique_values:
    one_hot_data[value] = (data['whoAmI'] == value).astype(int)

one_hot_data.head()