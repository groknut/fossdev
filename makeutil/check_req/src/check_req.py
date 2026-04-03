import sys

def _check(file_req, file_lib):
    req_map = {}
    lib_vec = []
    with open(file_req, "r", encoding = "utf-8") as req:
        for r in req:
            r = r.strip()
            req_map[r] = True
    
    with open(file_lib, "r", encoding = "utf-8") as lib:
        for l in lib:
            l = l.strip().split(" ")
            imp_idx = l.index("import")
            if not req_map.get(l[imp_idx+1],False):
                print("Error. Txt file don't have library")
            lib_vec.append(l[imp_idx+1])

if __name__ == "__main__":
    _check(sys.argv[1], sys.argv[2])