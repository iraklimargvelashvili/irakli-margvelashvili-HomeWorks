from datetime import datetime, timezone

# Create datetime - ჩავთვალე, რომ ასე ხელით შეყვანით მრავალფეროვან მაგალითებს დააგენერირებდით
custom_time = datetime(2024, 3, 22, 12, 7, 2, 956376, tzinfo=timezone.utc)

# Convert to ISO 8601 format
time = custom_time.isoformat()

#print(time)

hour = int(time[11:13])
if hour > 12 :
    hour = hour - 12

t_zone = int(time[-5:-3])

print(time[8:10]+'-'+time[5:7]+'-'+time[0:4]+' '+f'{hour}'+time[13:19]+' '+time[-6]+f'{t_zone}')


