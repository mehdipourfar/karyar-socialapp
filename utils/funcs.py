from datetime import datetime
from django.utils import timezone



def datetime_to_unixtime(d: datetime) -> int:
    return int(d.timestamp() * 1000)

def unixtime_to_datetime(unix_time: int) -> datetime:
    dt = datetime.fromtimestamp(unix_time // 1000)
    return timezone.make_aware(dt)


def int_or_default(value: str, default: int) -> int:
    try:
        value = int(value)
        if value < 0:
            return default
        return value
    except (ValueError, TypeError):
        return default
