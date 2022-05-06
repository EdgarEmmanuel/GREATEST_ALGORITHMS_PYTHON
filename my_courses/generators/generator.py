def warnings_filter(file):
    for line in file:
        if "WARNING" in line:
            yield line.replace("WARNING", " ")


with open("log.txt") as input:
    with open("output.txt", "w") as output:
        warnings = warnings_filter(input)
        for line in warnings:
            output.write(line)