# Health Hackers – AI Healthcare Chatbot

> **Guarding minds, coding hearts.**

![CI](https://img.shields.io/badge/CI-GitHub_Actions-blue) ![License](https://img.shields.io/badge/License-MIT-green)

Health Hackers is a production-demo AI chatbot for mental health support. This repository contains a production-ready prototype with a safety-first design.

## Quick start (development)
1. Backend: `cd backend && pip install -r requirements.txt && uvicorn app.main:app --reload --port 8000`
2. Frontend: `cd frontend && npm install && npm start`
3. Use the app at `http://localhost:3000` (frontend) and ensure backend at `http://localhost:8000`

## OpenAI Integration
Set `OPENAI_API_KEY` in `backend/.env.production` or in your deployment environment to enable GPT-powered responses. The code falls back to safe canned replies if the key is missing or fails.

## Team
Health Hackers - Team focused on AI for accessible mental health.
