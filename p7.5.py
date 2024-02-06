capital_state = {
    "gujarat": "ghandhinagar",
    "rajasthan": "jaiselamer",
    "maharashtra": "mumbai",
    "madhyapradesh": "bhopal",
    "uttarpradesh": "lucknow",
    "jharkhand": "ranchi",
    "goa": "panaji",
    "himachalpradesh": "shimla",
}
for i in capital_state:
    flag = 1
    count = 0
    while flag == 1:
        if count != 0:
            guess = input(f"you guessed wrong guess again the capital of {i} : ")
        if count == 0:
            guess = input(f"guess the capital of {i} : ")
        if guess == capital_state[i]:
            flag = 0
            count = 0
        else:
            count = count + 1
