# 📹 Real-Time Video Call Platform (WebRTC + Django Channels)

This is a **technical demo** of a professional video conferencing solution. It demonstrates the integration of **WebRTC** for peer-to-peer media streaming and **Django Channels (WebSockets)** for real-time signaling.

The system is designed to provide low-latency video and audio communication directly in the browser without requiring external plugins.

> 🛡️ **Note:** This repository showcases the signaling architecture and frontend integration. Production security layers and STUN/TURN configurations are kept private.

---

## 📌 Project Features

- 🎥 **HD Video & Audio**: High-quality peer-to-peer streaming using WebRTC.
- ⚡ **Instant Signaling**: Real-time connection handling via WebSockets and Django Channels.
- 🔒 **Secure Rooms**: Unique room IDs for private meetings.
- 📱 **Fully Responsive**: Works seamlessly on mobile, tablet, and desktop browsers.
- 🎙️ **Media Controls**: Toggle camera and microphone during the call.

---

## 🛠️ Technical Stack

| Layer          | Technology                                             |
|----------------|--------------------------------------------------------|
| **Backend** | Python 3.13, Django 5.x                                |
| **Real-Time** | Django Channels (WebSockets), Redis                    |
| **Streaming** | WebRTC (Signaling, ICE Candidates, SDP)                |
| **Frontend** | JavaScript (Vanilla/React), HTML5 Media API, CSS3      |
| **Environment**| Docker-ready, Daphne/Uvicorn (ASGI)                    |

---

## 🧠 Architectural Workflow

1. **Signaling**: Django Channels acts as the "middleman" to exchange connection metadata (SDP offers/answers) between peers.
2. **Peer-to-Peer**: Once the handshake is complete, video/audio data flows directly between users via WebRTC.
3. **STUN/TURN**: Integrated support for NAT traversal to ensure connectivity across different networks.

---

## 📂 Project Structure

```bash
Django-RealTime-VideoChat/
├── ontokproject/        # Global Django settings & ASGI/WSGI configuration
├── stream/              # Core WebRTC signaling, consumers, and video logic
├── saskenv/             # Local virtual environment (Dependencies)
├── .vscode/             # Development environment settings
├── .gitignore           # File exclusion rules for clean version control
├── README.md            # Project documentation and technical guide
├── db.sqlite3           # Local development database
└── manage.py            # Django administrative command-line utility
```

---

## 🔐 License & Usage

This project is released under a **Custom Proprietary License** for portfolio and technical demonstration purposes only.

### ❌ Strict Prohibitions:
- **Commercial Redistribution:** Selling or redistributing the signaling logic as a standalone product.
- **Service Hosting:** Using this codebase to host a commercial video conferencing service without authorization.
- **Reverse Engineering:** Replicating the core STUN/TURN integration patterns for commercial gain.

### ✅ Permitted Actions:
- **Architecture Review:** In-depth analysis of WebRTC and Django Channels integration.
- **Personal Learning:** Understanding peer-to-peer signaling and WebSocket consumers.
- **Employment Evaluation:** Reviewing the code for hiring and professional assessment.

> 🛡️ **Business Inquiries:**
> For full production implementation, custom WebRTC solutions, or licensing, please contact:  
> **📧 sultanelsultan4@gmail.com**

---

# 👤 Author

## Sultan Abdelkareem
### Lead Full-Stack Developer | Founder of SASKE Company
**Expertise:** Real-Time Systems, Django Channels, WebRTC, Enterprise ERP (8+ Yrs)

- 🔗 [LinkedIn](https://www.linkedin.com/in/sultan-abd-alkareem/)
- 🌐 [Portfolio](https://effulgent-shortbread-2bf423.netlify.app)
- 🏢 [SASKE Company](https://saske-eg.com)
