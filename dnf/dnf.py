class DNF:
    def __init__(self):
        self.file = open("demofile2.txt", "r")

    def main(self):
        line1 = self.file.readline()
        vars = []
        vars = line1.split(' ')
        numVars = len(vars) - 1
        self.file.readline()

        last = ''

        for i in range(0, 2**numVars):
            row = self.file.readline()

            rows = []
            rows = row.split(' ')
            out = int(rows[numVars])
            output = ''

            if (out == 1):
                for i in range(0, numVars):
                    varname = vars[i]
                    number = int(rows[i])
                    if (number == 0):
                        varname = varname + "'"
                    else:
                        varname = varname
                    output = output + varname
                last = last + output + ' + '

        last = last[0:len(last) - 2]
        print(last)

dnf = DNF()
dnf.main()
