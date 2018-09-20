def pretty_price(basePrice, formatPrice):
    basePrice_breakdown = str(basePrice).split(".")
    prefix = basePrice_breakdown[0]
    formatPrice_breakdown = str(formatPrice).split(".")
    suffix = formatPrice_breakdown[-1]
    return (float(prefix + "." + suffix))   
    

print(pretty_price(3.21, .95))
print(pretty_price(3.21, 95))

