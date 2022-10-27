def range_date_time(time):
    if time.hour < 12:
        return 'ertalab'
    elif time.hour < 18:
        return 'kunduzi'
    else:
        return 'kechki payt'


def re_week(re_df):
    re_df["Week"] = "week"
    weeks = ['Dushanba','Seshanba','Chorshanba','Payshanba','Juma','Shanba','Yakshanba']
    n = 0
    for i in range(len(re_df.index)):
        if i == 0:
            re_df["Week"][i] = weeks[1]
            n += 1
        elif n == 7:
            n = 0
            re_df["Week"][i] = weeks[n]
        else:
            re_df["Week"][i] = weeks[n]
        n += 1
    return re_df