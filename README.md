# 🏆 Employee Point Rewards - Premium HR Control Center

![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Django](https://img.shields.io/badge/Django-092E20?style=for-the-badge&logo=django&logoColor=white)
![TailwindCSS](https://img.shields.io/badge/Tailwind_CSS-38B2AC?style=for-the-badge&logo=tailwind-css&logoColor=white)
![AlpineJS](https://img.shields.io/badge/Alpine.js-8BC0D0?style=for-the-badge&logo=alpine.js&logoColor=white)

**BPS Point Reward** adalah platform gamifikasi manajemen SDM tingkat lanjut yang dirancang untuk mengintegrasikan performa karyawan dengan sistem penghargaan secara transparan dan aman. Mengusung konsep *Luxury UI*, sistem ini memberikan pengalaman manajerial yang intuitif bagi Tim HR dan pengalaman progresif yang memotivasi bagi Karyawan.

---

## 🚀 Fitur Utama & Arsitektur Teknis

Sistem ini dibangun dengan 3 pilar utama untuk mendukung operasional perusahaan skala besar:

### ⚡ 1. High-Concurrency & Performance Engine
* **Scalable Architecture:** Dioptimalkan untuk menangani lebih dari **300 pengguna aktif bersamaan** tanpa degradasi performa (High-Concurrency).
* **Asynchronous Processing:** Mengelola kalkulasi poin dan *logging* aktivitas secara efisien.

### 🔒 2. Security & Data Isolation
* **Multi-tenant Ecosystem:** Setiap karyawan memiliki isolasi data mandiri. Pengguna hanya dapat mengakses ekosistem dan riwayat poin milik mereka sendiri.
* **Intelligent Session Security:** Dilengkapi dengan fitur *auto-close session* setelah 5 menit tidak aktif (*idle*) untuk mencegah akses tidak sah pada terminal kerja.
* **Centralized Access Control:** Registrasi dan manajemen akun sepenuhnya dikendalikan oleh HR menggunakan kredensial NIK dan ID Karyawan yang terpusat.

### 📊 3. Audit Trail & Strategic Control
* **Financial Budget Monitoring:** Dashboard HR yang mampu memantau total liabilitas anggaran hadiah secara *real-time* untuk menjaga efisiensi biaya perusahaan.
* **KPI Adjustment Transparency:** Setiap perubahan poin dapat ditelusuri kembali ke Master KPI, memberikan transparansi penuh antara HR dan karyawan untuk menghindari sengketa data.
* **Tiering & Milestone Tracker:** Sistem pelacakan progres otomatis yang memetakan posisi level (*Silver, Gold, Platinum*) karyawan secara interaktif.

---

## 🎨 User Experience & Interface
* **Luxury Interactive UI:** Tampilan modern dengan palet warna premium (Charcoal & Gold) serta efek *glassmorphism*.
* **Sequential Motion Fade-In:** Animasi pemuatan komponen yang mengalir (Sequential Fade-In Up) menggunakan *Cubic-Bezier transition*.
* **Responsive Design:** Optimal diakses melalui Desktop maupun perangkat seluler dengan pengalaman navigasi yang mulus.

---

## 🛠️ Stack Teknologi

| Komponen | Teknologi |
| :--- | :--- |
| **Backend** | Python, Django Framework |
| **Frontend** | Tailwind CSS (Styling), Alpine.js (Reactivity) |
| **Database** | MySQL / SQLite (Development) |
| **Animation** | Custom CSS Keyframes & Luxury Transitions |

---

## ⚙️ Instalasi

1.  **Clone Repositori:**
    ```bash
    git clone [https://github.com/username/bps-point-reward.git](https://github.com/username/bps-point-reward.git)
    cd bps-point-reward
    ```

2.  **Environment Setup:**
    ```bash
    python -m venv venv
    source venv/bin/activate  # Windows: venv\Scripts\activate
    pip install -r requirements.txt
    ```

3.  **Database Migration:**
    ```bash
    python manage.py migrate
    ```

4.  **Running Server:**
    ```bash
    python manage.py runserver
    ```

---

## 👨‍💻 Kontributor
* **Ahmad Sutiawan** - *Lead Developer & Architect*  | Linkedin: https://www.linkedin.com/in/ahmadsutiawan/

---

> **Note:** Proyek ini dikembangkan dengan standar keamanan tinggi untuk memastikan integritas data reward dan kepuasan pengalaman pengguna bagi seluruh stakeholder perusahaan.
