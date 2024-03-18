def main():
    months=[
            'January','February','March','April','May','June',
            'July','August','September','October','November','December']
    max_days=[31,28,31,30,31,30,31,31,30,31,30,31]

    for x in range(12):
        for y in range(max_days[x]):
            print(f"{months[x]} {y+1}")

if __name__=="__main__":
    main()