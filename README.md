This is a simple local AI-powered file organizer that automatically scans your Downloads folder, understands file content, and organizes files into structured folders using a locally running LLM via Ollama.

## The goal of this project is to build a lightweight **local AI agent** that can:

- Monitor files in the Downloads folder
- Extract text from images (optional OCR)
- Use a local LLM to understand file content
- Generate meaningful filenames
- Categorize and organize files automatically
- Maintain simple memory for consistency

## The system follows a simple flow:

1. Read files from Downloads folder  
2. Extract text from images (if applicable)  
3. Send file info to a local LLM (Ollama)  
4. Model suggests category + filename  
5. File is renamed and moved to organized folders  
6. Decision is stored in memory for future consistency

Notes: memory.json is intentionally cleared.

Setup

### 1. Install Ollama
https://ollama.com/download

Run a model:
```bash
ollama run phi


