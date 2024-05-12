"""
Bu, kamu malı olarak yayınlanan ücretsiz ve ipoteksiz bir yazılımdır.
Herkes kopyalamak, değiştirmek, yayınlamak, kullanmak, derlemek, satmak veya satmakta özgürdür.
bu yazılımı kaynak kodu biçiminde veya derlenmiş olarak dağıtın
ikili, herhangi bir amaç için, ticari veya ticari olmayan ve herhangi bir şekilde
araç.
Telif hakkı yasalarını tanıyan yargı bölgelerinde, yazar veya yazarlar
Bu yazılımın her türlü ve tüm telif hakkı menfaatini
yazılımın kamu malı olması. Bu özveriyi fayda için yapıyoruz
genel olarak kamunun ve mirasçılarımızın zararına
halefler. Bu bağlılığın açık bir eylem olmasını amaçlıyoruz.
bu haklara ilişkin mevcut ve gelecekteki tüm haklardan kalıcı olarak feragat
telif hakkı yasası kapsamındaki yazılım.
YAZILIM, HERHANGİ BİR GARANTİ OLMAKSIZIN "OLDUĞU GİBİ" SAĞLANIR,
GARANTİLERİ DAHİL ANCAK BUNLARLA SINIRLI OLMAMAK ÜZERE AÇIK VEYA ZIMNİ
TİCARİ ELVERİŞLİLİK, BELİRLİ BİR AMACA UYGUNLUK VE İHLAL ETMEME.
YAZARLAR HİÇBİR DURUMDA HERHANGİ BİR İDDİA, ZARAR VEYA ZARARDAN SORUMLU OLMAYACAKTIR.
BİR SÖZLEŞME DAVASINDAN, HAKSIZ FİİLDEN VEYA BAŞKA BİR ŞEKİLDE DİĞER SORUMLULUK,
YAZILIM VEYA KULLANIMDAN VEYA KULLANIMDAN KAYNAKLANAN VEYA BUNLARLA BAĞLANTILI OLANLAR
YAZILIMDAKİ DİĞER İŞLEMLER.
Daha fazla bilgi için lütfen <http://unlicense.org/> adresine bakın.
"""

# ba_meta API 8 gerektirir

içe aktarma Listesi, Dikt, Herhangi biri yazarak

ithalat babase
bauiv1'i bui olarak içe aktar

orijinal_get_store_layout = bui.app.classic.store.get_store_layout


def add_special_characters(düzen:
                           Dict[str, List[Dict[str, Any]]]) -> Dict[str, List[Dict[str, Any]]]:
    özel_karakterler = [
        'karakterler.tavşan',
        'karakterler.taobaomascot',
        'karakterler.santa'
    ]
    özel_karakterlerdeki karakter için:
        karakter düzende değilse['karakterler'][0]['öğeler']:
            düzen['karakterler'][0]['öğeler'].append(karakter)


def add_special_minigames(düzen:
                          Dict[str, List[Dict[str, Any]]]) -> Dict[str, List[Dict[str, Any]]]:
    özel_minioyunlar = [
        'games.easter_egg_hunt',
    ]
    Special_minigames'teki mini oyun için:
        eğer mini oyun düzende değilse['minioyunlar'][0]['öğeler']:
            düzen['minioyunlar'][0]['öğeler'].append(minioyun)


def değiştirilmiş_get_store_layout() -> Dict[str, List[Dict[str, Any]]]:
    düzen = orijinal_get_store_layout()
    add_special_characters(düzen)
    add_special_minigames(düzen)
    dönüş düzeni


# ba_meta dışa aktarma eklentisi
sınıf Ana(babase.Plugin):
    def on_app_running(self) -> Yok:
        bui.app.classic.store.get_store_layout = değiştirilmiş_get_store_layout
