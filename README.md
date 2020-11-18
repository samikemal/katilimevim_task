# Bağlantılı üçgen graph üzerinde en kısa yolu bulmak
###
Üçgen graph bağlantıları Pascal üçgenine benzer bir yapıyla oluşuyorlar bu yüzdende bu yapı
yardımıyla algoritma geliştirdi. Geliştirlen algoritmadan önce alınan verilerin kullanılan
programlardaki veri yapılarıyla uyumlu olabilmesi için küçük veri önişleme işlemlerine tabii
tutuldu.
Ardından Pascal üçgenini kullanabilmek için gerekli çeşitli fonksiyonlar oluşturuldu:
- Binom açılımı 
- Toplaların tutulacağı listeyi, yine binom destekli oluşturan algoritma
- Ana döngü içerisinde kullanılması gereken  Pascal üçgenini içinde barındıran Pascal listesini oluşturan algoritma
- ve yine ana döngü içerisinde kontrol amaçlı kullanılan her adımda kaç adet toplam elde edilmesi gerektiğini hesaplayan algoritma
###
###
Ana döngü olarak bahsattiğimiz iç içe döngü üzerinde gerçekleşen ve kontrollerini binom serilerindeki elemanları
tekrar sayısı olarak ele alan ve bu tekrarları bir sonraki adıma kullanılması için toplam listesi oluşturmak adına
kullanan basit bir algoritmadır.