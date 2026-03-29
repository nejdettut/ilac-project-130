# 💊 İlaç Analiz Asistanı

Fotoğraf veya kamera ile ilaç kutusunu tara, AI ile detaylı analiz al.

## Özellikler
- 📷 Kamera veya dosya yükleme ile ilaç kutusu okuma
- 🖼️ Gemini Vision ile akıllı görsel analiz
- 🔡 EasyOCR ile yedek metin okuma
- 🌐 DuckDuckGo ile gerçek zamanlı web araması
- 🤖 Groq LLaMA ile hızlı ve detaylı analiz
- 📱 Mobil uyumlu Streamlit arayüzü
- 📄 PDF ve metin raporu indirme

## Kurulum

### 1. Repo'yu klonla
```bash
git clone https://github.com/KULLANICI_ADIN/ilac-analiz.git
cd ilac-analiz
```

### 2. Sanal ortam oluştur
```bash
python -m venv venv
source venv/bin/activate   # Windows: venv\Scripts\activate
```

### 3. Bağımlılıkları yükle
```bash
pip install -r requirements.txt
```

### 4. API anahtarlarını ayarla
```bash
cp .env.example .env
# .env dosyasını düzenle, API anahtarlarını gir
```

### 5. Uygulamayı başlat
```bash
streamlit run app.py
```

## API Anahtarları Nereden Alınır?
| Servis | Link | Ücretsiz mi? |
|--------|------|--------------|
| Groq | https://console.groq.com | ✅ Ücretsiz |
| Gemini | https://aistudio.google.com | ✅ Ücretsiz |
| SerpAPI | https://serpapi.com | ⚠️ Sınırlı ücretsiz |

## GitHub'a Deploy
```bash
git add .
git commit -m "İlk sürüm"
git push origin main
```

## Streamlit Cloud Deployment 🚀
Uygulamanızı **Streamlit Cloud** platformunda yayınlamak için şu adımları izleyin:

1. [Streamlit Cloud](https://share.streamlit.io/) sitesine gidin ve GitHub hesabınızla giriş yapın.
2. **"Create app"** butonuna tıklayın.
3. Repository olarak `nejdettut/ilac-project-130` seçin.
4. "Main file path" kısmına `app.py` yazın.
5. **ÖNEMLİ:** Deployment başlamadan önce **"Advanced settings..."** kısmına tıklayın.
6. **"Secrets"** bölümüne `.env` dosyanızdaki anahtarları şu formatta yapıştırın:

```toml
GROQ_API_KEY = "SİZİN_GROQ_ANAHTARINIZ"
GEMINI_API_KEY = "SİZİN_GEMINI_ANAHTARINIZ"
# Opsiyonel:
# SERPAPI_KEY = "SİZİN_SERPAPI_ANAHTARINIZ"
```

7. **"Deploy!"** butonuna basın.

## ⚠️ Yasal Uyarı
Bu uygulama eğitim amaçlıdır. Tıbbi tavsiye vermez.
