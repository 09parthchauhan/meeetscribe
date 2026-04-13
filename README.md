# MeetScribe

AI-powered meeting transcription for Indian languages, built on Sarvam AI.

## Features

- 🎙️ Transcribe meetings in 22 Indian languages
- 👥 Automatic speaker diarization
- 🤖 AI-generated summaries and action items
- 🌐 Hinglish and code-mixed conversation support
- ⚡ Fast processing with async job queues
- 💳 Subscription-based pricing with Razorpay

## Tech Stack

- **Backend:** Django 5.0 + Django REST Framework
- **Database:** PostgreSQL
- **Task Queue:** Celery + Redis
- **AI:** Sarvam AI (STT + LLM)
- **Payments:** Razorpay
- **Storage:** AWS S3 / Cloudflare R2
- **Frontend:** Django Templates + HTMX

## Project Structure

```
meetscribe/
├── accounts/           # User authentication and profiles
├── transcripts/        # Core transcription logic
├── payments/           # Subscription and billing
├── config/            # Django settings and configuration
├── templates/         # HTML templates
├── static/           # CSS, JS, images
├── media/            # User uploaded files (local dev)
└── manage.py
```

## Quick Start

### Prerequisites

- Python 3.11+
- PostgreSQL
- Redis
- Sarvam AI API key

### Installation

1. **Clone and setup virtual environment:**
```bash
git clone <your-repo>
cd meetscribe
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

2. **Install dependencies:**
```bash
pip install -r requirements.txt
```

3. **Environment variables:**
```bash
cp .env.example .env
# Edit .env with your actual credentials
```

4. **Database setup:**
```bash
python manage.py migrate
python manage.py createsuperuser
```

5. **Create required directories:**
```bash
mkdir -p static staticfiles media templates
```

### Running the Development Server

**Terminal 1 - Django:**
```bash
python manage.py runserver
```

**Terminal 2 - Celery Worker:**
```bash
celery -A config worker -l info
```

**Terminal 3 - Celery Beat (optional, for scheduled tasks):**
```bash
celery -A config beat -l info
```

**Terminal 4 - Redis:**
```bash
redis-server
```

Visit `http://localhost:8000`

## API Endpoints

### Authentication
- `POST /api/auth/register/` - User registration
- `POST /api/auth/login/` - User login
- `POST /api/auth/logout/` - User logout

### Transcriptions
- `POST /api/meetings/upload/` - Upload audio file
- `GET /api/meetings/` - List user's meetings
- `GET /api/meetings/<id>/` - Get meeting details
- `POST /api/webhooks/sarvam/` - Sarvam callback webhook

### Payments
- `POST /api/payments/create-subscription/` - Start subscription
- `POST /api/webhooks/razorpay/` - Razorpay payment webhook

## Testing

```bash
# Run all tests
pytest

# Run with coverage
pytest --cov=.

# Run specific app tests
pytest transcripts/tests.py
```

## Contributing

1. Fork the repository
2. Create feature branch (`git checkout -b feature/amazing-feature`)
3. Commit changes (`git commit -m 'Add amazing feature'`)
4. Push to branch (`git push origin feature/amazing-feature`)
5. Open Pull Request

## License

Proprietary - All rights reserved

## Support

For issues and questions:
- Email: support@meetscribe.in
- GitHub Issues: [Create an issue]

---

Built with ❤️ in India using Sarvam AI