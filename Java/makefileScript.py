import sys

for i in range(1, len(sys.argv)):
    try:
        f_name = sys.argv[i]
        f_name = f_name.replace('.', '')
        f_name = f_name.replace(' ', '_')
        f_name += ".java"
        f = open(f_name, "w")
        print(f_name)
    except IOError as e:
        print (e)
    finally:
        f.close()

