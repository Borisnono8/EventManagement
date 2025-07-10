# 🎯 Event Management System

<div align="center">

![Python](https://img.shields.io/badge/Python-3.11-blue?style=for-the-badge&logo=python)
![Flask](https://img.shields.io/badge/Flask-2.3.3-green?style=for-the-badge&logo=flask)
![PostgreSQL](https://img.shields.io/badge/PostgreSQL-15-blue?style=for-the-badge&logo=postgresql)
![Bootstrap](https://img.shields.io/badge/Bootstrap-5.3-purple?style=for-the-badge&logo=bootstrap)
![License](https://img.shields.io/badge/License-MIT-yellow?style=for-the-badge)

**Sistema completo per la gestione eventi con autenticazione utenti, permessi basati sui ruoli e architettura MVC**

[📋 Caratteristiche](#-caratteristiche) • [🚀 Installazione](#-installazione) • [📁 Struttura](#-struttura-del-progetto) • [💻 Tecnologie](#-tecnologie-utilizzate) • [🎨 Design](#-design-e-ui)

</div>

---

## 📋 Caratteristiche

### 🔐 **Sistema di Autenticazione**
- ✅ Registrazione e login utenti
- ✅ Hash sicuro delle password con Werkzeug
- ✅ Gestione sessioni con Flask-Login
- ✅ Protezione CSRF su tutti i form

### 👥 **Gestione Ruoli Utente**
- 🎫 **Partecipanti (Attendee)**: Visualizzazione e registrazione agli eventi
- 🎯 **Organizzatori (Organizer)**: Creazione e gestione eventi completa
- 🔒 Controllo accessi con decoratori personalizzati

### 📅 **Gestione Eventi**
- ➕ Creazione, modifica ed eliminazione eventi
- 📊 Tracciamento partecipazioni e capacità
- 🔍 Ricerca e filtri per tipologia evento
- 📝 Registrazione/annullamento registrazione
- 📈 Dashboard organizzatori con statistiche

### 🎨 **Interfaccia Utente**
- 📱 Design responsive con Bootstrap 5
- 🌙 Tema scuro elegante
- 🎯 Navigazione intuitiva
- ⚡ Feedback immediato con toast notifications

---

## 🚀 Installazione

### 📋 **Prerequisiti**
```bash
# Assicurati di avere installato:
- Python 3.11+
- PostgreSQL 15+
- Git
```

### 📦 **Setup del Progetto**

1. **Clona il repository**
```bash
git clone https://github.com/Borisnono8/EventManagement.git
cd EventManagement
```

2. **Installa le dipendenze**
```bash
pip install -r requirements.txt
```

3. **Configura le variabili d'ambiente**
```bash
# Crea un file .env nella root del progetto
DATABASE_URL=postgresql://user:password@localhost/eventdb
SESSION_SECRET=your_secret_key_here
```

4. **Inizializza il database**
```bash
python init_db.py
```

5. **Avvia l'applicazione**
```bash
# Sviluppo
python main.py

# Produzione
gunicorn --bind 0.0.0.0:5000 main:app
```

6. **Accedi all'app**
```
http://localhost:5000
```

---

## 📁 Struttura del Progetto

```
📦 event-management-system/
┣ 📂 events/                    # 🎪 Modulo gestione eventi
┃ ┣ 📄 __init__.py             # Inizializzazione blueprint
┃ ┣ 📄 routes.py               # Route per eventi
┃ ┗ 📄 views.py                # Viste class-based
┣ 📂 users/                     # 👤 Modulo gestione utenti
┃ ┣ 📄 __init__.py             # Inizializzazione blueprint
┃ ┣ 📄 routes.py               # Route per utenti
┃ ┗ 📄 views.py                # Viste class-based
┣ 📂 static/                    # 🎨 Asset statici
┃ ┣ 📂 css/
┃ ┃ ┗ 📄 style.css             # Stili personalizzati
┃ ┗ 📂 js/
┃   ┗ 📄 main.js               # JavaScript interattivo
┣ 📂 templates/                 # 🖼️ Template HTML
┃ ┣ 📂 auth/                   # Template autenticazione
┃ ┣ 📂 events/                 # Template eventi
┃ ┣ 📂 users/                  # Template utenti
┃ ┣ 📄 base.html               # Template base
┃ ┣ 📄 index.html              # Homepage
┃ ┣ 📄 404.html                # Pagina errore 404
┃ ┗ 📄 403.html                # Pagina errore 403
┣ 📄 app.py                     # ⚙️ Configurazione Flask
┣ 📄 main.py                    # 🚀 Entry point applicazione
┣ 📄 models.py                  # 🗄️ Modelli database
┣ 📄 forms.py                   # 📝 Form WTForms
┣ 📄 decorators.py              # 🔐 Decoratori autorizzazione
┣ 📄 init_db.py                 # 🗂️ Inizializzazione database
┣ 📄 requirements.txt           # 📋 Dipendenze Python
┗ 📄 README.md                  # 📖 Documentazione
```

---

## 💻 Tecnologie Utilizzate

### 🐍 **Backend**
| Tecnologia | Versione | Descrizione |
|------------|----------|-------------|
| ![Python](https://img.shields.io/badge/Python-3.11-blue?logo=python) | 3.11+ | Linguaggio principale |
| ![Flask](https://img.shields.io/badge/Flask-2.3.3-green?logo=flask) | 2.3.3 | Framework web |
| ![SQLAlchemy](https://img.shields.io/badge/SQLAlchemy-2.0-red?logo=sqlalchemy) | 2.0+ | ORM database |
| ![PostgreSQL](https://img.shields.io/badge/PostgreSQL-15-blue?logo=postgresql) | 15+ | Database relazionale |

### 🎨 **Frontend**
| Tecnologia | Versione | Descrizione |
|------------|----------|-------------|
| ![Bootstrap](https://img.shields.io/badge/Bootstrap-5.3-purple?logo=bootstrap) | 5.3 | Framework CSS |
| ![JavaScript](https://img.shields.io/badge/JavaScript-ES6-yellow?logo=javascript) | ES6+ | Interattività client |
| ![HTML5](https://img.shields.io/badge/HTML5-orange?logo=html5) | 5 | Markup semantico |
| ![CSS3](https://img.shields.io/badge/CSS3-blue?logo=css3) | 3 | Styling avanzato |

### 🔧 **Strumenti e Librerie**
```python
# Autenticazione e Sicurezza
Flask-Login==0.6.2          # Gestione sessioni
Flask-WTF==1.1.1            # Form e protezione CSRF
Werkzeug==2.3.6             # Utilità di sicurezza

# Database
Flask-SQLAlchemy==3.0.5     # ORM Flask
psycopg2-binary==2.9.7      # Driver PostgreSQL

# Validazione
WTForms==3.0.1              # Validazione form
email-validator==2.0.0      # Validazione email

# Deployment
Gunicorn==21.2.0            # Server WSGI
```

---

## 🎨 Design e UI

### 🌈 **Palette Colori**
- 🎯 **Primario**: `#6f42c1` (Viola)
- 🎨 **Secondario**: `#6c757d` (Grigio)
- ✅ **Successo**: `#198754` (Verde)
- ⚠️ **Warning**: `#ffc107` (Giallo)
- ❌ **Errore**: `#dc3545` (Rosso)

### 📱 **Responsive Design**
- 📋 Layout ottimizzato per mobile-first
- 🖥️ Adattamento automatico desktop/tablet
- 🎯 Navigazione touch-friendly
- ⚡ Caricamento veloce con CDN

### 🎭 **Componenti UI**
- 🔘 **Bottoni**: Stili Bootstrap personalizzati
- 📋 **Form**: Validazione in tempo reale
- 🔔 **Notifiche**: Toast notifications
- 📊 **Card**: Layout eventi responsive
- 🎯 **Modal**: Conferme azioni critiche

---

## 🗄️ Schema Database

### 📊 **Modelli Principali**

#### 👤 **User**
```python
- id: Integer (PK)
- username: String (unique)
- email: String (unique)
- password_hash: String
- first_name, last_name: String
- phone, organization, bio: String (optional)
- role: String (attendee|organizer)
- created_at, updated_at: DateTime
```

#### 🎪 **Event**
```python
- id: Integer (PK)
- title: String
- description: Text
- start_datetime, end_datetime: DateTime
- location, venue_details: String
- max_attendees: Integer
- registration_deadline: DateTime
- event_type: String
- organizer_id: Integer (FK → User)
```

#### 📝 **Registration**
```python
- id: Integer (PK)
- user_id: Integer (FK → User)
- event_id: Integer (FK → Event)
- registered_at: DateTime
- status: String (registered|cancelled|attended)
- notes: Text
```

---

## 🚀 API Endpoints

### 🔐 **Autenticazione**
```http
GET  /auth/login           # Pagina login
POST /auth/login           # Processo login
GET  /auth/register        # Pagina registrazione
POST /auth/register        # Processo registrazione
GET  /auth/logout          # Logout utente
```

### 🎪 **Eventi**
```http
GET  /events/              # Lista eventi
GET  /events/<id>          # Dettaglio evento
GET  /events/create        # Form creazione (organizer)
POST /events/create        # Creazione evento
GET  /events/<id>/edit     # Form modifica (owner)
POST /events/<id>/edit     # Modifica evento
POST /events/<id>/delete   # Eliminazione evento
POST /events/<id>/register # Registrazione evento
```

### 👤 **Utenti**
```http
GET  /users/dashboard      # Dashboard utente
GET  /users/profile        # Profilo utente
POST /users/profile        # Aggiorna profilo
GET  /users/organizer      # Dashboard organizzatore
```

---

## 📄 Licenza

Questo progetto è rilasciato sotto licenza **MIT**.

```
MIT License

Copyright (c) 2025 Event Management System

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.
```

---

## 📞 Contatti

- 📧 **Email**: boisnono8@gmail.com
- 🐙 **GitHub**: [@Borisnono8](https://github.com/Borisnono8/EventManagement)

---

<div align="center">

**Made with ❤️ and Flask**

</div>