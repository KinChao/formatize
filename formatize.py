def splitter(line):
    line_splitted = []
    x = ""
    for i in line:
        if i != '\t':
            x += i
        else:
            line_splitted.append(x)
            x = ''
    line_splitted.append(x)
    return line_splitted


def formatter(line):
    final_line=""

    index = 0
    for i in line:
        if index == 0:
            final_line += str(i)
        elif index == 1:
            if len (i)==1:
                final_line += "      "
                final_line += str(i)
            elif len(i)==2:
                final_line += "     "
                final_line += str(i)
            elif len(i)==3:
                final_line += "    "
                final_line += str(i)
            elif len(i)==4:
                final_line += "   "
                final_line += str(i)
            elif len(i)==5:
                final_line += "  "
                final_line += str(i)
        elif index == 2:
            if len(i) != 4:
                final_line += "  "
                final_line += i
                if len(i) == 1:
                    final_line += "   "
                elif len(i) == 2:
                    final_line += "  "
                elif len(i) == 3:
                    final_line += " "
            elif len(i) == 4:
                final_line += " "
                final_line += i
                final_line += " "
        elif index ==3:
            final_line += i
            if len(i) ==1:
                index2 = 1
            elif len(i) == 2:
                index2 = 2
            elif len(i) == 3:
                index2 = 3
            elif len(i) == 4:
                index2 = 4
        elif index ==4:
            if index2 == 3 and len(i)==1:
                final_line += "     "
                final_line += str(i)
            elif index2 == 3 and len(i)==2:
                final_line += "    "
                final_line += str(i)
            elif index2 == 3 and len(i)==3:
                final_line += "   "
                final_line += str(i)
            elif index2 == 4 and len(i)==1:
                final_line += "    "
                final_line += str(i)
            elif index2 == 4 and len(i)==2:
                final_line += "   "
                final_line += str(i)
            elif index2 ==4 and len(i)==3:
                final_line += "  "
                final_line += str(i)
            elif index2 ==4 and len(i)==4:
                final_line += " "
                final_line += str(i)
            elif index2 ==1 and len(i)==1:
                final_line += "       "
                final_line += str(i)
            elif index2 ==1 and len(i)==2:
                final_line += "      "
                final_line += str(i)
            elif index2 ==1 and len(i)==3:
                final_line += "     "
                final_line += str(i)
            elif index2 ==1 and len(i)==4:
                final_line += "    "
                final_line += str(i)
            elif index2 ==1 and len(i)==5:
                final_line += "   "
                final_line += str(i)
        elif index ==5:
            if len(i) == 5:
                final_line += "      "
                final_line += str(i)
            elif len(i) == 6:
                final_line += "     "
                final_line += str(i)
            elif len(i) == 7:
                final_line += "    "
                final_line += str(i)
        elif index ==6:
            if len(i) == 5:
                final_line += "   "
                final_line += str(i)
            elif len(i) == 6:
                final_line += "  "
                final_line += str(i)
            elif len(i) == 7:
                final_line += " "
                final_line += str(i)
        elif index ==7:
            if len(i) == 5:
                final_line += "   "
                final_line += str(i)
            elif len(i) == 6:
                final_line += "  "
                final_line += str(i)
            elif len(i) == 7:
                final_line += " "
                final_line += str(i)
        elif index ==8:
            final_line += "  "
            final_line += str(i)
        elif index ==9:
            final_line += "  "
            final_line += str(i)
        elif index ==10:
            final_line +="      "
            final_line += str(i)
        index +=1
    return (final_line)

txt = []

with open("input.txt","r") as f:
    for x in f:
        lines = f.readline()
        x = x.replace('\n','')
        lines = lines.replace('\n','')
        if lines != "":
            txt.append(x)
            txt.append(lines)


txt2 = txt[0:-1]

with open('step5_charmm2gmx.txt','w') as f:
    for i in txt2:
        g = formatter(splitter(i))
        f.write(g)
        f.write("\n")
    f.write(txt[-1])
    f.write("\n")
    f.write("END")
