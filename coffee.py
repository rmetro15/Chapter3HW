def coffee(pounds):
    order = (pounds * 10.50) + (0.86 * pounds) + 1.50
    return "The order costs $" + str(order)
