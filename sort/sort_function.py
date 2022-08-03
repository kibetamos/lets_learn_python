# A function without a name is called an anonymous function.
#  And this syntax is called a lambda expression.
companies = [('Google', 2019, 134.81),
             ('Apple', 2019, 260.2),
             ('Facebook', 2019, 70.7)]


# define a sort key
def sort_key(company):
    return company[2]



# sort the companies by revenue
companies.sort(key=sort_key, reverse=True)

# show the sorted companies
print(companies)
