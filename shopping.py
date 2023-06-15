budget = float(input())
video_cards = int(input())
processors = int(input())
ram_memory = int(input())

discount = 0
if video_cards > processors:
    discount = 0.15

sum_video_cards = video_cards * 250
sum_processors = processors * sum_video_cards * 0.35
sum_ram_memory = ram_memory * sum_video_cards * 0.10

total_sum = sum_video_cards + sum_processors + sum_ram_memory

total_sum_with_discount = total_sum * 0.85

if total_sum_with_discount <= budget:
    print(f"You have {budget - total_sum_with_discount :.2f} leva left!")
else:
    print(f"Not enough money! You need {total_sum_with_discount - budget :.2f} leva more!")
    

