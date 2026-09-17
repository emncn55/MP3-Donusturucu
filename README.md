# MP3 Dönüştürücü

Python ile geliştirilmiş, video bağlantılarındaki sesleri MP3 formatında kaydetmeye yarayan basit bir Windows masaüstü uygulamasıdır.

Uygulama, indirme işlemleri için `yt-dlp`, ses dönüştürme işlemleri için FFmpeg ve masaüstü arayüzü için Tkinter kullanır.

## Özellikler

* Basit masaüstü arayüzü
* Video bağlantısından MP3 oluşturma
* 192 kbps MP3 çıktısı
* İndirme durumu ve ilerleme göstergesi
* Dosyaları otomatik olarak Downloads klasörüne kaydetme
* Oynatma listelerinde yalnızca girilen videoyu indirme
* Windows ile uyumlu dosya adları
* Arayüz donmadan arka planda indirme

## Kullanılan Teknolojiler

* Python
* Tkinter
* yt-dlp
* FFmpeg
* Deno
* PyInstaller

## Gereksinimler

* Python 3.10 veya üzeri
* FFmpeg
* Deno

Windows üzerinde FFmpeg ve Deno kurulumu:

```powershell
winget install --id Gyan.FFmpeg --exact
winget install --id DenoLand.Deno --exact
```

Kurulumları kontrol etmek için:

```powershell
ffmpeg -version
deno --version
```

## Projeyi Kurma

Projeyi bilgisayarınıza klonlayın:

```powershell
git clone REPOSITORY_ADRESINIZ
cd MP3-Donusturucu
```

Sanal ortam oluşturun:

```powershell
py -m venv .venv
```

Sanal ortamı etkinleştirin:

```powershell
.\.venv\Scripts\Activate.ps1
```

Gerekli Python paketlerini yükleyin:

```powershell
python -m pip install --upgrade pip
python -m pip install -r requirements.txt
```

## Uygulamayı Çalıştırma

```powershell
python app.py
```

Açılan pencerede video bağlantısını girin ve **MP3 Olarak İndir** düğmesine basın.

Oluşturulan MP3 dosyaları varsayılan olarak kullanıcının `Downloads` klasörüne kaydedilir.

## Windows EXE Oluşturma

PyInstaller'ı yükleyin:

```powershell
python -m pip install pyinstaller
```

Uygulamayı EXE dosyasına dönüştürün:

```powershell
python -m PyInstaller --onefile --windowed --name "MP3-Donusturucu" --collect-all yt_dlp app.py
```

Oluşturulan uygulama aşağıdaki klasörde bulunur:

```text
dist/MP3-Donusturucu.exe
```

FFmpeg ve Deno'nun uygulamanın çalıştırılacağı bilgisayarda kurulu olması gerekir.

## Proje Yapısı

```text
MP3-Donusturucu/
├── app.py
├── requirements.txt
├── README.md
└── .gitignore
```

## Yasal Kullanım

Bu proje yalnızca eğitim amaçlı geliştirilmiştir.

Uygulama sadece kullanıcının sahip olduğu, kamu malı olan veya indirme izni bulunan içeriklerde kullanılmalıdır. Kullanıcılar, kullandıkları platformun hizmet şartlarına ve yürürlükteki telif hakkı kurallarına uymaktan kendileri sorumludur.

Bu proje herhangi bir içerik platformuyla bağlantılı veya onlar tarafından desteklenen resmî bir uygulama değildir.
