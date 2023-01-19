import pandas as pd

data = pd.read_csv("adult.data.csv")
data.head()

# print(data["sex"].value_counts())
#
# print(data[data['sex'] == "Female"]["age"].mean())

# a = data['native-country'].value_counts(normalize=TrueS)
# print(a[4])

# age1 = data[data['salary'] == '>50K']['age']
# age2 = data[data['salary'] == '<=50K']['age']
# print("Средний возраст : {0} (>50K) , {1} (<=50K); среднеквадратичные отклонения - {2} (>50K), {3} (<=50K)".format(
#     round(age1.mean()), round(age2.mean()),
#     round(age1.std(), 1), round(age2.std(), 1)))

# sp1 = data[data['salary'] == '>50K']['education'].unique()
# sp2 = ["Bachelors", "Prof-school", "Assoc-acdm", "Assoc-voc", "Masters", "Doctorate"]
# a = 0
# b = 0
# for i in range(len(sp1)):
#     for n in range(len(sp2)):
#         if (sp1[i] != sp2[n]):
#             a +=1
#     if (a > 5):
#         print("Утверждение неверное")
#         b +=1
#         breakЫ
#     a = 0
# if (b == 0):
#     print("Утверждение верное")

# print(data.groupby(['race', 'sex'])['age'].describe())
# print("Максимальный возраст мужчин расы Amer-Indian-Eskimo")
# print(data.groupby(['race', 'sex'])['age'].describe().loc['Amer-Indian-Eskimo'].loc['Male']['max'])

# mar_status = [ word for word in data['marital-status'].unique() if word.startswith('Married') ]
# arr_marr = data[(data['sex'] == 'Male') &
#      (data['marital-status'].isin(mar_status))]['salary'].value_counts()
# print("Женатые")
# print(arr_marr)
# arr_not_marr = data[(data['sex'] == 'Male') &
#      (~data['marital-status'].isin(mar_status))]['salary'].value_counts()
# print("Холостые")
# print(arr_not_marr)
# print("Богатых среди женатых {0}%".format(round(100 * arr_marr[1]/(arr_marr[0]+arr_marr[1]), 2)))
# print("Богатых среди холостых {0}%".format(round(100 * arr_not_marr[1]/(arr_not_marr[0]+arr_not_marr[1]), 2)))

# max_work = data['hours-per-week'].max()
# print("Макс. число часов - {0} час./нед.".format(max_work))
#
# num_workers = data[data['hours-per-week'] == max_work].shape[0]
# print("Всего людей с таким кол-ом часов {0}".format(num_workers))
#
# per_rich = data[(data['hours-per-week'] == max_work) & (data['salary'] == '>50K')].shape[0] / num_workers
# print("Из них богатых {0}%".format(round(100 * per_rich, 2)))

print(data.groupby(['native-country', 'salary'])['hours-per-week'].mean())