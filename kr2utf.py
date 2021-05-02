import os
import chardet
import re

workdir = r"V:\work\Src_Vector\101-Working\"

if __name__ == "__main__":
    rexp = re.compile('\.[hc]$', re.IGNORECASE) # 소스 파일 찾음
    failstr = ""
    for root, dirs, files in os.walk(workdir):
        for fname in files:
            re_res = rexp.search(fname)
            fpath = os.path.join(root, fname)
            if re_res:
                with open(fpath, 'rb') as fobj:
                    fdata = fobj.read()
                
                chde = chardet.detect(fdata)
                if chde['encoding'] == 'EUC-KR' and chde['confidence'] > 0.9:
                    with open(fpath, 'r', encoding=chde['encoding']) as f:
                        txt = f.read()
                    with open(fpath, 'w', encoding='UTF-8') as f:
                        f.write(txt)
                    print(f"{fpath} :: {chde['encoding']} => UTF-8")
                elif chde['encoding'] == 'EUC-KR' and chde['confidence'] > 0.6:
                    failstr.join(f"{fpath} :: 알쏭달쏭\n")
                    
                    pass
    print(failstr)
