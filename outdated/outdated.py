def main():

    months = [
        "January",
        "February",
        "March",
        "April",
        "May",
        "June",
        "July",
        "August",
        "September",
        "October",
        "November",
        "December" ]

    while True:
        try:
            date = input("enter date(in m/d/y format): ").strip()
            if "/" in date:
                m,d,y = date.split("/")
            else:
                month_name, rest = date.split(" ",1)
                d,y = rest.split(",")
                m = months.index(month_name) + 1
            m = int(m)
            d = int(d)
            y = int(y)
            if m<=12 and d<=31:
                pass
            else:
                continue

        except ValueError:
            continue
        else:
            print(f"{y}-{m:02}-{d:02}")
            break

main()
