# MarkItDown Integration Evaluation

**Decision: ADOPT for ResumeBuilder backend.**

## What It Is

Microsoft MarkItDown (MIT, 147K GitHub stars) converts PDF, DOCX, PPTX, Excel, images, HTML and more into structured Markdown optimized for LLM consumption. It preserves document structure — section headings, bullet lists, tables.

## Why It Matters for ResumeBuilder

The current `pdfjs-dist` parser joins all text items with spaces and returns flat unstructured text. MarkItDown returns Markdown with section headers, making LLM resume extraction significantly more reliable. It also unlocks DOCX upload, which is currently blocked with "coming soon."

## Integration Architecture

A small Python FastAPI service (`workers/document-conversion/`) wraps MarkItDown. ResumeBuilder's Next.js app (on Vercel) calls it via `MARKITDOWN_SERVICE_URL`. The service is deployed on Railway or Render using Docker.

### Upload flow (new)

```
User uploads PDF or DOCX
  → isSupportedResumeFile() validates magic bytes
  → convertResumeFile() calls Python service
  → { markdown, format } returned
  → stored in resumes.raw_text
  → optimizeResume(markdown, jd) called
```

## Files Created

- `workers/document-conversion/main.py` — FastAPI service
- `workers/document-conversion/converter.py` — MarkItDown wrapper
- `workers/document-conversion/Dockerfile`
- `workers/document-conversion/requirements.txt`
- `src/lib/markitdown-client.ts` — Next.js HTTP client
- `src/lib/utils/file-validation.ts` — PDF + DOCX magic byte validation
- `src/app/api/upload-resume/route.ts` — 3 targeted edits

## POC Validation (do before deploying)

```bash
python3 -m venv /tmp/mid-test && source /tmp/mid-test/bin/activate
pip install markitdown[pdf,docx]
markitdown /path/to/resume.pdf
markitdown /path/to/resume.docx
```

Gate: structured Markdown output (section headers visible) on 4+ of 5 test resumes.

## Security

- Files written to uuid-named temp path — never user filename
- Temp file deleted in `finally` block
- Max 10MB enforced before conversion
- ALLOWED_ORIGINS set to ResumeBuilder domain only
- Docker container runs as non-root user

## Future: AI Audit Toolkit

The same Python microservice can handle client intake documents (PDFs, reports, process docs). Add a `document_type` field and route accordingly after ResumeBuilder is stable.
