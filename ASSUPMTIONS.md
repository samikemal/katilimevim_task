## Algoritma geliştirirken karşılaştığım varsayımlar.
###
Bir ağaç yapısı gibi olduğunu varsayarak başladığım algoritmanın öyle olmadığını bir dalın iki kökü olduğunu
fark ettim. Ardından Bir graph yapısı olarak tanımlayıp çözüm üretmek istedim ağırlıksız graphlar üzerinde
minimum maksimum yolları hesaplamak için önce yolları bulup ağaca dökmem ve bu ağaçlardan en kısasını bulmam
gerektiğini düşündüm. Dijkstra gibi bu tip işlemlerde kullanılan algoritmaları temel alarak bir kaç algoritma
geliştirdim fakat başarılı sonuçlar elde edemeyince verilen üçgenin kendi yapısı üzerinde bir matematiksel örüntü
aramaya başladım. Toplamlara ulaşmak için uğranan düğümler incelendiğinde tıpkı bir Pascal üçgeni gibi tekrar
ettiğini fark ettim ve bu matematiksel kurallara dayalı bir algoritma geliştirdim. Fakat bu algoritmanın önemli
bir eksiği olarak döngüler arasındaki her bir düğümün sahip olduğu binom değeri kadar tekrar ederken aynı zamanda
toplamların tutulduğu listenin de tekrar etmeden birikimli olarak ilerlemesini sağlamak için farklı iki döngü veya
yapı kurmalıydım. Bu yapılar da oluşturulduğunda verilen tüm üçgenler için doğru sonucu vereceğini düşünüyorum.
###