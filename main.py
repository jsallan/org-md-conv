import os, re, linecache
org_dir = "org_files/"

files = os.listdir(org_dir)

patterns = [
    ("^:[\w]*:[\s\w-]*\\n", ""),    #  :PROPERTIES:\n or :id:
    ("^\*\s\#[\w]*\\n", ""),        #  * #Tag
    ("^\*{1}\s", "- "),             #  * Heading1
    ("^\*{2}\s", "\t- "),           #  * Heading2
    ("^\*{3}\s", "\t\t- "),         #  * Heading3
    ("^\*{4}\s", "\t\t\t- "),       #  * Heading3
]

with os.scandir(org_dir) as files:
    for file in files:
        if file.name[-3:] == "org":
            with open(file, 'r') as opened_file:
                output_file = ""
                for line_num, line_contents in enumerate(opened_file):
                    # first, search for unordered lists
                    if line_contents[0] == "-":  # turn this into some \t at the same level as the previous heading
                        for line_search_num in range(line_num, -1, -1):  # find the header level
                            line_search = linecache.getline(org_dir + file.name, line_search_num)
                            header_level = len(line_search) - len(line_search.strip("*"))
                            if header_level > 0:
                                line_contents = line_contents.replace("-", "\t"*(header_level-1)+" ")
                                break
                    else:
                        for pattern in patterns:
                            line_contents = re.sub(pattern[0], pattern[1], line_contents)
                    output_file = f"{output_file}{line_contents}"
            with open(file.name[:-3]+"md", 'w') as f:
                f.write(output_file)
            x = 1
