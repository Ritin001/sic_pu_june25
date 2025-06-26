each_part=80//5
crops = {
    "Tomatoes": {
        "land": each_part,
        "yield_30": 10,
        "yield_70": 12,
        "price_per_tonne": 7000
    },
    "Potatoes": {
        "land": each_part,
        "yield": 10,
        "price_per_tonne": 20000
    },
    "Cabbage": {
        "land": each_part,
        "yield": 14,
        "price_per_tonne": 24000
    },
    "Sunflower": {
        "land": each_part,
        "yield": 0.7,
        "price_per_tonne": 200000
    },
    "Sugarcane": {
        "land": each_part,
        "yield": 45,
        "price_per_tonne": 4000
    }
}
#tomatoes
tomatoees_yield_30 = crops["Tomatoes"]["yield_30"] * crops["Tomatoes"]["land"] * 0.3
tomatoees_yield_70 = crops["Tomatoes"]["yield_70"] * crops["Tomatoes"]["land"] * 0.7
tomatoees_yield_total = tomatoees_yield_30 + tomatoees_yield_70
tomatoees_price = tomatoees_yield_total * crops["Tomatoes"]["price_per_tonne"]

#potatoes
potatoes_yield = crops["Potatoes"]["yield"] * crops["Potatoes"]["land"]
potatoes_price = potatoes_yield * crops["Potatoes"]["price_per_tonne"]

#cabbage
cabbage_yield = crops["Cabbage"]["yield"] * crops["Cabbage"]["land"]
cabbage_price = cabbage_yield * crops["Cabbage"]["price_per_tonne"]

#sunflower
sunflower_yield = crops["Sunflower"]["yield"] * crops["Sunflower"]["land"]
sunflower_price = sunflower_yield * crops["Sunflower"]["price_per_tonne"]   

#sugarcane
sugarcane_yield = crops["Sugarcane"]["yield"] * crops["Sugarcane"]["land"]
sugarcane_price = sugarcane_yield * crops["Sugarcane"]["price_per_tonne"]

#part a
total_yield_price = tomatoees_price + potatoes_price + cabbage_price + sunflower_price + sugarcane_price
print("Total yield price is:", total_yield_price)


#part b
total_chemical_free_at_end_of_11_months = tomatoees_price + potatoes_price + cabbage_price + sunflower_price 
print("Total chemical free at the end of 11 months is:", total_chemical_free_at_end_of_11_months)