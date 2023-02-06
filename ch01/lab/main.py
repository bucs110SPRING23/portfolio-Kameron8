import random

#Part A
weeks = 16
print(weeks, type(weeks))
classes = 10
print(classes, type(classes))
tuition = 6000
print(tuition, type(tuition))
cost_per_week = ((tuition / classes) / weeks)
print(cost_per_week, type(cost_per_week))
print("Cost per week:", cost_per_week)
classes_per_week = 3
print(classes_per_week, type (classes_per_week))
cost_per_class = cost_per_week / classes_per_week
print(cost_per_class, type(cost_per_class)) 
print("How much you are paying per class;", cost_per_class)

#Part B
random_list = ["Dog", "Cat", "Fox", "Elephant", "Snake"]
random_animal = random.choice(random_list)
print(random_animal)