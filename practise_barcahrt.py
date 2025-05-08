import matplotlib.pyplot as plt

# Population of 5 countries
countries = ['USA', 'Nigeria', 'Kenya', 'India', 'China']
population = [331, 206, 54, 1393, 1441]  # in millions
plt.figure(figsize=(8, 5))
plt.bar(countries, population, color='skyblue')  # corrected color spelling
plt.title("Population of 5 Countries")
plt.xlabel("Countries")
plt.ylabel("Population (in millions)")
plt.show()