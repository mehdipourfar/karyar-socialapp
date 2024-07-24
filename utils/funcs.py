from datetime import datetime



def datetime_to_unixtime(d: datetime) -> int:
    return int(d.timestamp() * 1000)

def unixtime_to_datetime(unix_time: int) -> datetime:
    return datetime.fromtimestamp(unix_time // 1000)
