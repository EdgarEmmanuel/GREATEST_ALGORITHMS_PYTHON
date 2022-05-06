with open("log.txt") as firstFile:
    lines = firstFile.readlines()
    with open("warnings.txt", "w") as warning_file:
        warnings = (l for l in lines if "WARNING" in l)
        for warning in warnings:
            warning_file.write(warning)
    print("Ecriture Effectuee !")
