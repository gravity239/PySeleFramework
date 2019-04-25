from selenpy.helper import conditions


# *** WebDriver conditions ***
def title(exact_value):
    return conditions.Title(exact_value)


# *** Web Element conditions ***
def value(exact_value):
    return conditions.Value(exact_value)
