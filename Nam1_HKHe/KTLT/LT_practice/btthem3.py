def chep_file(copyfile, pastefile):
    import shutil
    try:
        shutil.copyfile(copyfile, pastefile+"_dest.txt")
    except:
        print("Don't have this file")
    finally:
        print("Done")

chep_file(input("Path of copy file: "), input("Path and name of paste file: "))