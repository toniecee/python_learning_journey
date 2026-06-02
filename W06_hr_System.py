# open the file

with open("hr_system.txt") as hr_file:
    next(hr_file)
    # read through the file line by line
    for line in hr_file:
        # get the various parts of the record into variables
        parts = line.split(" ")

        name = parts[0].strip()
        id = int(parts[1].strip())
        title = parts[2].strip()
        salary = int(parts[3].strip())

        paycheck_amount = salary/24
        if title.lower == "Engineer":
            paycheck_amount += 1000

        # print out the values
        print(f"{name} (ID: {id}), {title} - ${paycheck_amount:.2f}")