def chep_file(copyfile, pastefile):
    import shutil
    try:
        shutil.copyfile(copyfile, pastefile)
    except:
        print("Don't have this file")
    finally:
        print("Done")

chep_file(input("Path of copy file: "), input("Path of paste file: "))