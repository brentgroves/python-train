  # Yesterday date
  yesterday = today - timedelta(days = 1)
  start_end_date=yesterday.strftime("%m/%d/%Y")

  report_date=yesterday.strftime("%m/%d/%Y/%m/%d")+'00:00:00'
