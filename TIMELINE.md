# MeetScribe Development Timeline
## April 10 - May 10, 2026 (30 Days to Launch)

---

## WEEK 1: Foundation + Sarvam Integration (Apr 10-16)

### Day 1-2: Sarvam POC + Environment Setup
- ✅ Project structure created (Django + DRF + Celery)
- [-] Get Sarvam API key from dashboard.sarvam.ai
- [ ] Set up PostgreSQL locally
- [ ] Set up Redis locally
- [ ] Create .env file from .env.example
- [ ] Write standalone POC script: upload audio → Sarvam Batch API → print transcript
- [ ] Test with 2-3 sample meetings in Hindi/Hinglish

**Deliverable:** Working Python script that transcribes a local audio file

### Day 3-4: Database Models + Admin
- [ ] Create User model (extend Django User)
- [ ] Create Meeting model (audio file, status, metadata)
- [ ] Create Transcript model (raw JSON, summary, action items)
- [ ] Create Subscription model (plan, status, quota)
- [ ] Register all models in Django admin
- [ ] Run migrations: `python manage.py makemigrations && python manage.py migrate`
- [ ] Create superuser and test admin interface

**Deliverable:** Complete database schema with admin interface

### Day 5-7: Celery + Sarvam Integration
- [ ] Configure Celery in config/celery.py
- [ ] Create transcripts/tasks.py with process_meeting task
- [ ] Task 1: Upload to Sarvam Batch API
- [ ] Task 2: Poll for job completion (or use webhook)
- [ ] Task 3: Call Sarvam-M for summary generation
- [ ] Test locally with Celery worker running
- [ ] Use ngrok to expose webhook endpoint

**Deliverable:** End-to-end async pipeline working locally

---

## WEEK 2: REST API + File Storage (Apr 17-23)

### Day 8-10: REST API Endpoints
- [ ] Create serializers for Meeting, Transcript models
- [ ] `POST /api/meetings/upload/` - file upload + validation
- [ ] `GET /api/meetings/` - list user's meetings with pagination
- [ ] `GET /api/meetings/<id>/` - get meeting detail with transcript
- [ ] `POST /api/webhooks/sarvam/` - webhook receiver
- [ ] Add proper error handling and logging
- [ ] Test all endpoints with Postman/HTTPie

**Deliverable:** Fully functional REST API

### Day 11-12: File Storage (S3/R2)
- [ ] Sign up for Cloudflare R2 (or AWS S3)
- [ ] Install and configure django-storages
- [ ] Update settings.py with storage backend
- [ ] Test file upload → R2 → retrieval
- [ ] Add file size validation (max 100MB)
- [ ] Support multiple audio formats (MP3, WAV, MP4, M4A)

**Deliverable:** Audio files stored in cloud storage

### Day 13-14: Testing + Refinement
- [ ] Test with 10 real meeting recordings
- [ ] Test different languages: Hindi, Tamil, Hinglish, English
- [ ] Test edge cases: large files, corrupted audio, wrong format
- [ ] Fix bugs discovered during testing
- [ ] Add rate limiting to API endpoints
- [ ] Write API documentation

**Deliverable:** Stable, tested API ready for frontend

---

## WEEK 3: Frontend + Authentication (Apr 24-30)

### Day 15-17: Frontend with Django Templates + HTMX
- [ ] Find and download free Tailwind CSS template (Flowbite/TailwindUI)
- [ ] Create base.html template with navigation
- [ ] Create landing page (/) with hero, features, pricing
- [ ] Create dashboard.html - list of meetings
- [ ] Create upload.html - file upload form with progress bar
- [ ] Create meeting_detail.html - transcript display with speaker colors
- [ ] Add HTMX for dynamic updates (upload progress, status polling)

**Deliverable:** Working frontend UI

### Day 18-19: Authentication with Django Allauth
- [ ] Configure django-allauth in settings.py
- [ ] Create login/signup pages
- [ ] Add Google OAuth provider
- [ ] Create password reset flow
- [ ] Test email verification (use console backend for dev)
- [ ] Add login_required decorators to views
- [ ] Create user profile page

**Deliverable:** Complete auth system

### Day 20-21: Polish Frontend
- [ ] Add loading states and error messages
- [ ] Make UI responsive for mobile
- [ ] Add transcript export (copy to clipboard, download as .txt)
- [ ] Add speaker name editing feature
- [ ] Show timestamps in transcript
- [ ] Add "share via WhatsApp" button
- [ ] Test entire user flow end-to-end

**Deliverable:** Polished, user-ready interface

---

## WEEK 4: Payments + Deployment + Launch (May 1-7)

### Day 22-24: Razorpay Integration
- [ ] Sign up for Razorpay account
- [ ] Create two subscription plans: Free (₹0), Pro (₹299/month)
- [ ] Install razorpay Python SDK
- [ ] Create payments/views.py with subscription endpoints
- [ ] Implement subscription creation flow
- [ ] Add webhook receiver for payment confirmation
- [ ] Create middleware to check meeting quota before upload
- [ ] Add "Upgrade to Pro" prompts in UI
- [ ] Test payment flow with Razorpay test mode

**Deliverable:** Working payment system

### Day 25-26: Email + Notifications
- [ ] Set up AWS SES or Resend for email
- [ ] Create email templates:
  - Welcome email
  - Email verification
  - Transcript ready notification
  - Payment confirmation
  - Subscription expiry reminder
- [ ] Send email when transcript is ready
- [ ] Test all email flows

**Deliverable:** Complete notification system

### Day 27-28: Production Deployment
- [ ] Sign up for Railway account
- [ ] Create new project on Railway
- [ ] Add PostgreSQL service
- [ ] Add Redis service
- [ ] Configure environment variables
- [ ] Set up Celery worker as separate service
- [ ] Deploy via GitHub integration
- [ ] Add custom domain (buy from Hostinger/GoDaddy)
- [ ] Test production deployment thoroughly
- [ ] Set up error monitoring (Sentry optional)

**Deliverable:** Live production site

### Day 29-30: Beta Testing + Launch Prep
- [ ] Invite 10 beta testers (friends, LinkedIn connections)
- [ ] Create Google Form for feedback collection
- [ ] Monitor logs and fix critical bugs
- [ ] Create launch content:
  - LinkedIn post with demo video
  - Twitter thread
  - IndieHackers post
  - ProductHunt submission draft
- [ ] Test payment flow with real money (small amount)
- [ ] Create FAQ page
- [ ] Add Terms of Service and Privacy Policy pages

**Deliverable:** Ready for public launch

---

## POST-LAUNCH: May 8-10

### Day 31: Launch Day
- [ ] Post on LinkedIn with real before/after demo
- [ ] Post on IndieHackers
- [ ] Submit to ProductHunt
- [ ] Share in relevant WhatsApp/Slack groups
- [ ] Monitor signups and respond to questions
- [ ] Fix any critical issues immediately

### Day 32-33: Iterate Based on Feedback
- [ ] Analyze user behavior (which features are used most?)
- [ ] Fix top 3 issues reported by users
- [ ] Start planning v1.1 features based on feedback
- [ ] Begin outreach to first 10 paying customers

---

## Success Metrics

### Week 1 Success:
- POC script works with Sarvam API
- Celery task processes meeting successfully
- Can see transcript in database

### Week 2 Success:
- Can upload file via API
- File stored in R2/S3
- Webhook receives transcript
- Summary generated by Sarvam-M

### Week 3 Success:
- Can sign up and log in
- Can upload file via web UI
- Can see transcript in dashboard
- UI looks professional

### Week 4 Success:
- Site live on custom domain
- Can make a real payment
- 10 beta users testing
- Zero critical bugs

### Launch Success (May 10):
- 50+ signups
- 3-5 paying customers
- Stable, bug-free experience
- Positive feedback from users

---

## Daily Commitment

- **4-5 hours/day** (adjust based on your availability)
- Code in focused 2-hour blocks
- Don't skip days - momentum is everything
- When stuck >30 minutes, ask for help in communities

## Common Pitfalls to Avoid

1. **Scope creep** - Don't add features not in this plan
2. **Perfectionism** - Ship the boring version first
3. **Infrastructure rabbit holes** - Use managed services
4. **Over-engineering** - Simple solutions work
5. **Design paralysis** - Use pre-made templates

## Resources

- Sarvam AI Docs: https://docs.sarvam.ai/
- Django Celery: https://docs.celeryq.dev/en/stable/django/
- HTMX: https://htmx.org/docs/
- Razorpay: https://razorpay.com/docs/
- Django Allauth: https://django-allauth.readthedocs.io/

---

**Remember:** Done is better than perfect. Ship by May 10! 🚀
