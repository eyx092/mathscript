import sys

file = open(sys.argv[1], "r")
code = file.read()
file.close()

raw = code.split("\n")

for i in range(len(raw)):
    if raw[i] == "init":
        ans = 0
        index = []
        values = []
        for j in range(i+1, len(raw)):
            try:
                line = raw[j].split(" ")

                line_number = str(i + j + i)

                if len(line) == 1:
                    if line[0].lower() == "reset":
                        ans = 0
                        index = []
                        values = []

                if len(line) == 2:
                    if line[0].lower() == "get":
                        if line[1] == "ans":
                            print(ans)
                        else:
                            variable = line[1]
                            for i in range(len(index)):
                                if variable == index[i]:
                                    print(values[i])
                                    break

                if len(line) == 3:
                    if line[1].lower() == "ans":
                        line[1] = ans
                    if line[2].lower() == "ans":
                        line[2] = ans
                    if line[0].lower() == "add":
                        if line[1].isnumeric() == False:
                            for i in range(len(index)):
                                if line[1] == index[i]:
                                    line[1] = values[i]
                                    break

                        if line[2].isnumeric() == False:
                            for i in range(len(index)):
                                if line[2] == index[i]:
                                    line[2] = values[i]
                                    break
                        ans = float(line[1]) + float(line[2])
                        print(ans)
                    if line[0].lower() == "sub":
                        if line[1].isnumeric() == False:
                            for i in range(len(index)):
                                if line[1] == index[i]:
                                    line[1] = values[i]
                                    break

                        if line[2].isnumeric() == False:
                            for i in range(len(index)):
                                if line[2] == index[i]:
                                    line[2] = values[i]
                                    break
                        ans = float(line[1])-float(line[2])
                        print(ans)
                    if line[0].lower() == "mul":
                        if line[1].isnumeric() == False:
                            for i in range(len(index)):
                                if line[1] == index[i]:
                                    line[1] = values[i]
                                    break

                        if line[2].isnumeric() == False:
                            for i in range(len(index)):
                                if line[2] == index[i]:
                                    line[2] = values[i]
                                    break
                        ans = float(line[1])*float(line[2])
                        print(ans)
                    if line[0].lower() == "div":
                        if line[1].isnumeric() == False:
                            for i in range(len(index)):
                                if line[1] == index[i]:
                                    line[1] = values[i]
                                    break

                        if line[2].isnumeric() == False:
                            for i in range(len(index)):
                                if line[2] == index[i]:
                                    line[2] = values[i]
                                    break
                        ans = float(line[1])/float(line[2])
                        print(ans)
                    if line[0].lower() == "var":
                        if line[1] == "ans":
                            pass
                        else:
                            try:
                                float(line[1])
                            except:
                                index.append(line[1])
                                values.append(float(line[2]))
                    if line[0].lower() == "set":
                        if line[1] == "ans":
                            pass
                        else:
                            try:
                                float(line[1])
                            except:
                                for i in range(len(index)):
                                    if line[1] == index[i]:
                                        values[i] = float(line[2])
                                        break

            except:
                pass
