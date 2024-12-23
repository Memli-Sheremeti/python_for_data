import datetime

x = datetime.datetime.now()


print("Seconds since January 1, 1970:" , f"{x.timestamp():,}", "or",
f"{x.timestamp():.2}", "in scientific notaion\n",
x.strftime("%b"), x.strftime("%d"), x.strftime("%Y"))
