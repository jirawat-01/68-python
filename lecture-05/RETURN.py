def calculate_stats(numbers):
    total_sum = sum(numbers)
    average = total_sum / len(numbers)
    maximum = max(numbers)
    manimum = min(numbers)
    return total_sum, average , maximum, manimum

numbers = [5,10,15,20,25]
total, avg, max_num , min_num = calculate_stats(numbers)
print(f"Total sum: {total}")
print(f"Average : {avg}")
print(f"maximum:{max_num}")
print(f"minimum: {min_num}")