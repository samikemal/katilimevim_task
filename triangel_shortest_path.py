
def howMuchSumInLine(depth) : # üçgen ilerledikçe her satırda birikerek yeni toplamlar elde edilir.
                              # Her satırda kaç adet toplam olacağını binom açılım algoritması yardımıyla
                              # hesaplamak için kullanılan fonksiyon.
    sum_piece=0  
    for i in range(depth):
        sum_piece += binomialCoeff(depth-1,i)
    return sum_piece
    
def binomialCoeff(n, k) : # Verilen üçgenin bağlantıları incelendiğinde bir Pascal üçgeni olduğu anlaşılıyor.
                          # Bu Pascal üçgeninin matematiksel dönüşümünü elde etmek için binom açılımı
                          # algoritmasını diğer fonksiyonlarda yardım amaçlı kullanmak için oluşturuldu.
    res = 1
    if (k > n - k) : 
        k = n - k 
    for i in range(0 , k) : 
        res = res * (n - i) 
        res = res // (i + 1)  
    return res

def sumListMaker(depth): # Üçgenin her adımındaki toplamları bir sonraki adımı hesaplamak için tuttuğumuz
                         # listeyi oluşturan fonksiyon.
    sum_List=[]
    for i in range(1,len(lines)+1):
        temp=[]
        for j in range(howMuchSumInLine(i)):
            temp.append(0)
        sum_List.append(temp)
    return sum_List

def makePascalList(depth): # Asıl algoritmamızın çalışabilmesi için verilen üçgende tekrar eden elemanların
                           # kontrolünü sağlamak için kullanılacak Pascal üçgeni listesini oluşturan fonksiyon 
    pascal_list=[]
    for line in range(0, depth) : 
        temp=[]
        # Every line has number of  
        # integers equal to line 
        # number 
        for i in range(0, line + 1) : 
            temp.append(binomialCoeff(line, i)) 
        pascal_list.append(temp)
    return pascal_list

file1 = open("triangle.txt") # Dosya programa eklendi.
lines = file1.readlines() # İleride kullanılacağı için dossyada veriler satır satır okundu ve bir değişkene atandı.
file1.close() # Dosya donanım tasarrufu açısından kapatıldı.

for i in range(len(lines)): # Dosya Python list veri tipine dönüştürülebilecek hale hazırlanmak üzere
                            # yer değiştirme ve parçalama işlemleri uygulandı.
    lines[i] = lines[i].replace("\n","")
    lines[i] = lines[i].replace(" ",",")
    lines[i] = lines[i].split(',')    
        
sums = sumListMaker(len(lines)) #toplamların tutulacağı liste oluşturuldu.
pascal_list = makePascalList(len(lines)) # kontrol sağlamak için gereken Pascal listesi oluşturuldu.

for i in range(len(lines)-1): # Üçgenin son basamağına kadar (sonuncu hariç) tüm basamaklarda ilerleniyor.
    for j in range(len(lines[i])): # Üçgenin her basamağının içindeki elemanlar içerisinde geziliyor. 
        if i==0 and j==0: # Toplam listesine başlangıç değeri ataması için kontrol yapılıyor.
            sums[i][j]=int(lines[i][j]) # Kontrol sağlandığında başlangıç değeri ataması yapılıyor.
        for k in range(pascal_list[i+1][j]): # Başlangıç değeri sonrası basamaklardaki değerler önceki basamakta
                                             # kendisine bağlı olan sayılarla tekrar tekrar toplanabilmek adına
                                             # döngü içerisine ekleniyor.
            a=j
            sums[i+1][j+a]=sums[i][j]+int(lines[i+1][j]) # Gezilen her düğüm bir sonraki adımda kullanılmak üzere
                                                         # toplam listesine eklenerek liste hazırlanıyor.
            sums[i+1][j+1+a]=sums[i][j]+int(lines[i+1][j+1]) # Bir üst adımdaki işlemin aynısı üçgenin diğer kolu
                                                             # içinde uygulanıyor.
            a += 1
            

Answer = min(sums[len(sums)-1]) # toplamların arasında en küçüğü hesaplanıyor.  
    
    
    