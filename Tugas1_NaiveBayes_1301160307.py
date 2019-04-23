import pandas as pd
test=pd.read_csv('TestsetTugas1ML.csv',delimiter=',',header=None) #data dalam file testset ditampung dalam array test
train=pd.read_csv('TrainsetTugas1ML.csv',delimiter=',',header=None) #data dalam file trainset ditampung dalam array train
def cari_semua(a): #untuk menghitung didalam data train ada berapa yang '>50K' atau '<=50K'
    hasil=0
    i=0
    while i<=160:
        if train[8][i] == a:
            hasil=hasil+1
        i=i+1
    return hasil

def cari(a,b,c): #untuk mencari data yang sesuai dengan datatest didalam datatrain, a merupakan nilai dataTest, b merupakan kelas, dan c untuk kolom
    hasil=0
    i=0
    while i<=160:
        if train[c][i]== a and train[8][i]==b :
            hasil= hasil+1
        i=i+1
    return hasil

def check_atribut(a): #fungsi untuk mengecheck didalam kolom ada berapa unique atribut
    list_atribut = set([atribut for atribut in train[1:][a]])
    return len(list_atribut)
#MAIN PROGRAM
len_train=len(train)-1 #untuk menyimpan banyaknya isi dataTrain
len_test=len(test)-1 #untuk menyimpan banyaknya isi dataTest
a='>50K'
b='<=50K'
income1= cari_semua(a)
income2= cari_semua(b)
item=1
x,y= 0,0
result=[]
z=0
while item<=len_test:
    x = cari(test[1][item],a,1)/income1*cari(test[2][item],a,2)/income1*cari(test[3][item],a,3)/income1*cari(test[4][item],a,4)/income1*cari(test[5][item],a,5)/income1*cari(test[6][item],a,6)/income1*cari(test[7][item],a,7)/income1*income1/len_train
    y = cari(test[1][item],b,1)/income2*cari(test[2][item],b,2)/income2*cari(test[3][item],b,3)/income2*cari(test[4][item],b,4)/income2*cari(test[5][item],b,5)/income2*cari(test[6][item],b,6)/income2*cari(test[7][item],b,7)/income2*income2/len_train
    if x==0 or y==0:
        #pakai laplace smoothing
        x= (cari(test[1][item],a,1)+1)/(income1+check_atribut(1))*(cari(test[2][item],a,2)+1)/(income1+check_atribut(2))*(cari(test[3][item],a,3)+1)/(income1+check_atribut(3))*(cari(test[4][item],a,4)+1)/(income1+check_atribut(4))*(cari(test[5][item],a,5)+1)/(income1+check_atribut(5))*(cari(test[6][item],a,6)+1)/(income1+check_atribut(6))*(cari(test[7][item],a,7)+1)/(income1+check_atribut(7))*(income1+1)/(len_train+check_atribut(8))
        y= (cari(test[1][item],b,1)+1)/(income2+check_atribut(1))*(cari(test[2][item],b,2)+1)/(income2+check_atribut(2))*(cari(test[3][item],b,3)+1)/(income2+check_atribut(3))*(cari(test[4][item],b,4)+1)/(income2+check_atribut(4))*(cari(test[5][item],b,5)+1)/(income2+check_atribut(5))*(cari(test[6][item],b,6)+1)/(income2+check_atribut(6))*(cari(test[7][item],b,7)+1)/(income2+check_atribut(7))*(income2+1)/(len_train+check_atribut(8))
    if x > y :
        result.append(a)
    else:
        result.append(b)
    item=item+1
df= pd.DataFrame(result)
df.to_csv('TebakanTugas1ML.csv',sep='\t',index=False,header=None)