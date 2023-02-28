from pkg.modul1 import *
from pkg.modul2 import *
from pkg.hitungnilai import hitung_nilai

def main():
    #memanggil fungsi fungsi dalam modul 1
    f1()
    f2()
    #memanggil fungsi fungsi dalam modul 2
    f3()
    f4()
    print("nilai akhir  :",hitung_nilai(30))
main()
