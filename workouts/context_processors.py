from django.utils import timezone
from datetime import datetime, timedelta

def current_datetime(request):
    current_date = datetime.today().date()  # Corrected to get today's date
    current_time = datetime.now()  # Set current time to the beginning of the day
    added_time = current_time + timedelta(minutes=5)  # Add 5 minutes, you can change to seconds as needed
    stored_time = datetime.now().strftime('%Y-%m-%d %H:%M:%S')

    return {
        'current_time': current_time.strftime('%Y-%m-%d %H:%M:%S'),
        'current_date': current_date,
        'added_time': added_time.strftime('%Y-%m-%d %H:%M:%S'), 
        'stored_time': stored_time,
    }
