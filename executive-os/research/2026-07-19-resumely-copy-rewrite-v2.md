# Resumely iOS — Full-Screen Copy Rewrite Audit + Version 2

- **Date:** 2026-07-19
- **Product:** Resumely iOS (`ResumeBuilder IOS APP`)
- **Sources:** live screen inventory · `.agents/product-marketing.md` · `2026-07-19-x-twitter-activation-gtm-hooks.md` · founder Preview screenshot
- **Status:** draft rewrite pack — **copy only, no code shipped**
- **Version:** Rewrite v2.0

---

## ASSUMPTIONS

1. Scope = **active V2 journey** (Home → Fit → Diagnosis → Optimized/Preview → Export → Submit Package → Me) + Design/Expert locked teasers + marketing screenshot slots. Legacy Scan/Improve strings included where still reachable.
2. English is the source of truth; Hebrew needs a follow-up parity pass after EN approval.
3. Backend-generated gap titles (e.g. “job title business”) get **prompt/guardrail rules**, not only UI string swaps.
4. “ATS-friendly” (process) is allowed; “ATS score / Free ATS Check / pass ATS / Improve ATS” as outcome language is not.
5. This pack does **not** change scoring logic, analytics event names, or navigation structure.

→ Correct these now if wrong; otherwise treat v2 as the candidate string set for a future implementation packet.

---

## North-star rewrite rules (v2)

| Do | Don't |
|---|---|
| Fit / Match / diagnosis / gaps / export / package | Free ATS Check, ATS score (as product name), Improve ATS, pass ATS filters |
| “Resumely Match Score” or “Match estimate” | Official / employer ATS score implications |
| “Sounds like you” / your own wording | Resume-soup / generic AI flex |
| “Invisible for this job” / searchable | “75% auto-rejected” meme |
| “Not a hiring guarantee” | Interview / job guarantees |
| One job → export → next job | Spray volume as the hero |

**Activation sequence to support in copy:** upload → job → fit/diagnosis → optimize → **export** → optimize for another job / submit package.

---

## Severity legend

| Sev | Meaning |
|---|---|
| **P0** | Claim/trust risk — conflicts with approved positioning or do-not-claim list |
| **P1** | Activation language — hurts upload→export clarity or anti-slop story |
| **P2** | Polish / consistency — tone, redundancy, post-success CTAs |

---

# Part A — Rewrite audit (problems by screen)

| Screen | Sev | Current issue | Why it fails |
|---|---|---|---|
| Home progress step 3 | P0 | `ATS score` | Names the metric as ATS; should be Match |
| Home guest CTA | P0 | `Free ATS Check` / `Run Free ATS Check` | Official-ATS vibes; product-marketing avoids this |
| Home state `readyForFreeATS` | P0 | `Ready for a free ATS check` | Same |
| Upload sheet body | P0 | `We'll read it the way an ATS does.` | Overclaims parser fidelity |
| Upload scanned fail | P1 | `so an ATS can't read it either` | OK as parse education if softened |
| Locked Optimized teaser | P0 | `An ATS match score…` | Rename to Match Score |
| Optimized chip | P0 | `Improve ATS` / `Improving ATS...` | Founder screen; worst trust hit |
| Optimized insights | P0 | `ATS insights` / `ATS Match` | Align to Match / parse |
| Design locked | P1 | `12 ATS-safe templates` + `parseable by the bots` | Prefer ATS-friendly; drop “bots” bravado |
| Expert card | P1 | `ATS-safe structure` / `ATS Deep Report` | Rename Deep Report → Match Deep Report or Keyword Report |
| Me stats | P0 | `ATS score` | → Match Score |
| Marketing screenshots | P0 | `ATS checker` / `ATS resume score` captions | Fight Fit-First ASO story |
| Share strings | P0 | `My resume scored %lld%% on ATS` | Explicitly wrong claim |
| Diagnosis / Preview | P1 | Backend gap sludge (`job title business`) | Breaks “your own wording” |
| Post-export Preview | P1 | Hero still `Preview & Export PDF` after success | Demote re-export |
| Auth headline | P2 | `…in 60 seconds` | Risky promise; optional soften |
| Guest save sheet | P2 | Big `SCORE` chrome | Prefer Match estimate framing |
| Ambassador | P2 | `Did you land the interview?` | Close to outcome claim; soften |

---

# Part B — Rewrite Version 2 (screen-by-screen)

Format: **Current → v2**. Only strings that change (or strategic keep) are listed.

---

## 0. Tab bar

| Current | v2 | Notes |
|---|---|---|
| Home | Home | keep |
| Optimized | Optimized | keep |
| Design | Design | keep |
| Expert | Expert | keep |
| Me | Me | keep |
| Latest optimization restored / …tabs are back in sync. | keep | fine |

---

## 1. Auth / Guest

### Auth sheet
| Current | v2 |
|---|---|
| Tailor your resume to any job in 60 seconds. | Tailor your resume to one job — then export a PDF that still sounds like you. |
| Create Account / Sign In / Sign Up / field labels | keep |

### Me — guest
| Current | v2 |
|---|---|
| Create a free account to save every optimization, sync across devices, and export unlimited PDFs. | Create a free account to save optimizations, sync devices, and keep your exports. |
| Create free account / Already have one? Sign in | keep |
| Your resume is uploaded securely… Sign in only when you're ready to optimize and export. | Your resume is uploaded securely for analysis. Sign in when you're ready to optimize and export. |

### Save account sheet
| Current | v2 |
|---|---|
| SCORE | MATCH |
| Save your {score} | Save your Match Score |
| Your optimized résumé & score history | Your optimized résumé & match history |
| Unlimited PDF exports, any template | PDF exports for every template you use |
| Continue with Apple / email / Maybe later | keep |
| Your résumé stays private… | keep |

---

## 2. Home / Activation

### Hero (default)
| Current | v2 |
|---|---|
| GET STARTED | GET STARTED |
| Step 1 of 3 | Step 1 of 3 |
| See your résumé like a recruiter does | See what this job is missing on your résumé |
| Upload, match to a job, and get your first diagnosis in under 2 minutes. | Upload, paste one job, and get a Match diagnosis before you apply. |
| Progress: Upload · Add job · **ATS score** | Upload · Add job · **Match** |
| See what a recruiter notices in the first 7 seconds — then fix it. | See the gaps a recruiter may notice — then fix them in your own words. |
| View optimized resume / Preview and export your PDF | keep |
| Use a saved resume | keep |

### Activation state machine

| State | Current headline | v2 headline | Current subhead | v2 subhead |
|---|---|---|---|---|
| noResume | Upload your resume for a recruiter-style read | Upload your resume to start | See what a recruiter may notice in 7 seconds… | We'll read your file, then compare it to one job posting. |
| resumeNoJob | Paste a job to reveal missing keywords | Paste the job you're applying to | A job description lets us compare… | One posting → keyword gaps, fit, and what to fix. |
| readyForFreeATS | Ready for a free ATS check | Ready for a free Match check | See the first score before signing in… | See your Match estimate before signing in — then unlock full diagnosis. |
| readyToOptimize | Ready for your resume diagnosis | Ready for your resume diagnosis | Get your match score, top gaps… | Get your Match Score, top gaps, missing signals, and a rewrite you control. |
| atsComplete | Your free Resumely Match Score is in | Your free Resumely Match Score is in | Sign in to unlock full optimization and PDF export. | Sign in to unlock full optimization and PDF export. |
| optimizing | Finding the aha moments… | Finding what to fix next… | Reading your resume, comparing it to the job… | Comparing your resume to this job and preparing clear next fixes. |
| optimizedReady | Your optimized resume is ready | Your optimized resume is ready | Review the diagnosis, preview the PDF… | Review the diagnosis, export the PDF, or refine further. |
| exportComplete | Resume exported successfully | PDF exported — nice | Share it, apply, or keep improving in Optimized. | Share it, submit your package, or optimize for another job. |

### Step 3 CTAs
| Current | v2 |
|---|---|
| Free ATS Check | Free Match Check |
| Run Free ATS Check | Run Free Match Check |
| See your score before signing in | See your Match Score before signing in |
| Analyze / Analyze my resume | keep |
| Diagnose gaps and improve this resume | Diagnose gaps for this job |
| Optimize / Continue to optimize | keep |
| Sign in to Optimize | Sign in to optimize |

### Continuity
| Current | v2 |
|---|---|
| Continue from the diagnosis you already ran | keep |
| Continue to optimize | keep |

---

## 3. Upload / picker / failures

### Upload sheet
| Current | v2 |
|---|---|
| Add your résumé | Add your résumé |
| PDF or DOCX, up to 5 MB. We'll read it the way an ATS does. | PDF or DOCX, up to 5 MB. We'll extract the text so it stays readable for common parsers. |
| Browse Files | keep |
| no file handy? / Paste… / Try a sample… Coming soon | keep |
| See a real diagnosis in 20 seconds | See a sample diagnosis in seconds |

### Home upload hero
| Current | v2 |
|---|---|
| Upload your résumé / PDF or DOCX · up to 5 MB / Choose a file | keep |
| Résumé selected / Choose a different file | keep |

### Failures
| Current | v2 |
|---|---|
| It looks like a scanned image — there's no selectable text, so an ATS can't read it either. | It looks like a scanned image — there's no selectable text for us (or most parsers) to read. |
| That file won't work yet / too large / generic | keep sense; keep CTAs |
| Tip: in most apps, Export as PDF keeps the text readable. | keep |

---

## 4. Job input / Fit check

### Job card
| Current | v2 |
|---|---|
| Add Job / URL or paste description | keep |
| LinkedIn or job post URL | keep |
| Or paste job description here | keep |
| word-count guidance / blockers | keep (clarity already good) |

### Check Fit
| Current | v2 |
|---|---|
| Is this job a fit? | Is this job worth your time? |
| Paste the job description below. We'll estimate your fit before you spend time optimizing. | Paste the posting. We'll estimate fit before you invest in a full optimize. |
| We'll use the job link you added… | keep sense |
| Check Fit | keep |
| Estimated fit vs this job. Not affiliated with any ATS vendor. No optimization credit used. | Estimated fit vs this job — Resumely's guidance, not an employer ATS score. No optimization credit used. |
| Skip fit and optimize / Edit target job | keep |

### Fit verdict
| Current | v2 |
|---|---|
| Strong Fit / Stretch Fit / Weak Fit | keep |
| Estimated match score | Resumely Match Score |
| Key Gaps / Missing Keywords | keep |
| Optimize for This Job | Optimize for this job |
| Edit target job / Skip — Browse Other Jobs | Edit target job / Skip — try another job |
| Estimated fit vs this job, not a hiring guarantee. | keep (canonical) |

### Fit loading
| Current | v2 |
|---|---|
| Checking fit for this role | keep |
| Comparing your experience against the job requirements. | keep |
| Estimating keyword match | Estimating keyword overlap |

---

## 5. Diagnosis (+ free score)

### Resume Diagnosis
| Current | v2 |
|---|---|
| FIRST READ | FIRST READ |
| Here is what the job sees | Here's what this posting needs from you |
| A compact diagnosis of fit, gaps, missing signals, and the next best fix. | Fit, gaps, missing signals, and the next fix — in your voice. |
| Resume Match Score | Resumely Match Score |
| Your resume matches about {n}% of this job | About {n}% Match to this job (estimate) |
| Potential after optimization: about {n}% | Potential after edits: about {n}% |
| Top 3 gaps / Missing keywords | keep |
| Improve my resume / Edit target job | keep |
| Start with resume + job / Analyze my resume | keep |
| Diagnosis unavailable… | keep |

### Diagnosis panel on Preview (founder screen)
| Current | v2 |
|---|---|
| Resume diagnosis | Resume diagnosis |
| % match | Match estimate |
| Improve ATS | Improve match |
| Improving ATS... | Improving match… |
| Estimated match guidance based on the target job, not a hiring guarantee. | keep |
| Work the concept 'job title business' into… | **Guardrail:** never show raw model concepts. Prefer: “Use the employer’s job title (or a close title you actually held) in one achievement — in your words.” |
| Add at least one metric… | keep (good) |

### Free score result (guest)
| Current | v2 |
|---|---|
| YOUR FIRST DIAGNOSIS | YOUR FIRST MATCH CHECK |
| Based on formatting + keyword match vs the job you paste. Not affiliated with any ATS vendor. | keep |
| Let's fix the basics / Good start… / Strong — polish it | keep |
| ATS issue found | Formatting or keyword issue found |
| Sign in to unlock full resume optimization. | keep |
| {n} free checks remaining this week. | keep |

### Loading modes
| Mode | Current title | v2 title | Current subtitle | v2 subtitle |
|---|---|---|---|---|
| atsCheck | Scanning like a recruiter would | Checking match like a first read | Most recruiters scan… | A quick pass for formatting + keyword signals vs this job. |
| diagnosis | Preparing your diagnosis | Preparing your diagnosis | Turning resume and job signals… | Turning resume + job signals into clear next fixes. |
| optimization | Optimizing your resume | Optimizing your resume | Matching your experience to this role. | Aligning your experience to this role — keeping your wording. |
| status | Checking formatting an ATS can parse | Checking formatting parsers can read | — | — |

---

## 6. Optimized / Improve / Preview / Export

### Locked Optimized
| Current | v2 |
|---|---|
| Here's what you'll unlock. | keep |
| Your résumé, scored & rewritten | Your résumé, matched & rewritten |
| An ATS match score, keyword gaps, and line-by-line fixes — tuned to your target job. | A Resumely Match Score, keyword gaps, and line-by-line fixes — tuned to one target job. |
| Unlock after Optimize / Upload résumé on Home | keep |

### Optimized Resume (main)
| Current | v2 |
|---|---|
| Before / After | keep |
| Based on formatting + keyword match… Not affiliated… | keep |
| ATS insights | Match insights |
| See what's blocking this resume | See what's blocking this resume |
| Score signals / Top blockers / Addable keywords | keep |
| Improve ATS → | **Improve match** |
| ATS Match → | **Match** |
| Resume diagnosis / % match → | Resume diagnosis / **Match estimate** |
| Keep this optimized resume… / Save to My Resumes | keep |
| Improve further / Refine / Edit / Design / Expert | keep |
| Preview & Export PDF | keep (pre-export) |
| Submit Package | keep |
| Edit only facts you can verify. Save refreshes the preview and Match Score. | keep |
| More aligned, not guaranteed to pass any ATS. | More aligned with this job — not a guarantee of interviews or ATS outcomes. |

### Post-export actions (P1 layout + copy)
| Current | v2 |
|---|---|
| PDF exported successfully | PDF exported successfully |
| Share again | Share PDF |
| Optimize for another job | Optimize for another job |
| Preview & Export PDF (still primary) | **Secondary:** Export PDF again |
| Submit Package (secondary) | **Primary after success:** Submit Package *(or keep Share as co-primary)* |

Recommended stack after success:
1. Submit Package  
2. Optimize for another job  
3. Share PDF  
4. Export PDF again (tertiary)

### Improve (legacy if still reachable)
| Current | v2 |
|---|---|
| View ATS breakdown | View Match breakdown |
| Match Score / Keyword alignment | keep |
| Optimize for This Job | Optimize for this job |

### Target reached
| Current | v2 |
|---|---|
| RECRUITER-READY | READY TO SEND |
| Your résumé is ready to send | keep |
| Drop it into an ATS-safe template | Drop it into an ATS-friendly template |
| Make it look the part / Lock in your progress | keep |

### AI Chat
| Current | v2 |
|---|---|
| AI Chat | Resume chat |
| Ask AI to tweak your optimized resume… | Ask for a tweak — keep facts you can prove… |

---

## 7. Submit Package

| Current | v2 |
|---|---|
| Submit Package / Create Package / field labels | keep |
| This is an internal tracking package… does not send anything to the recruiter. | keep (excellent) |
| Save Package to Me / Package Contents / Cover Letter… | keep |
| Saved internally in Me. Nothing was sent automatically… | keep |
| Submit at Job Link | Open job link |

---

## 8. Scan (legacy)

| Current | v2 |
|---|---|
| Analyze & Optimize | keep |
| Run Free ATS Check | Run Free Match Check |
| Free ATS Preview | Free Match Preview |
| Sign in to unlock full optimization. | keep |

---

## 9. Expert

| Current | v2 |
|---|---|
| The full submit package, done for you. | keep |
| Cover letters & submit packages | keep |
| A tailored cover letter, likely recruiter questions, and an export-ready package… | keep |
| Resume Rewrite — Role-fit rewrite with ATS-safe structure. | Role-fit rewrite with ATS-friendly structure. |
| **ATS Deep Report** | **Match Deep Report** |
| Keyword coverage, compliance, formatting tips. | Keyword coverage, parse tips, formatting guidance. |
| Other mode titles | keep |
| Return after running Optimize… | keep |

---

## 10. History

| Current | v2 |
|---|---|
| Search job title or company | keep |
| No optimizations yet / Run a scan and optimization… | No optimizations yet / Run Optimize on Home to see it here. |
| Sign in to view history / Download PDF / Review | keep |

---

## 11. Me / Account

| Current | v2 |
|---|---|
| Account | keep |
| Optimized · **ATS score** · Templates | Optimized · **Match Score** · Templates |
| Latest Resume / My Applications / Credits / Account | keep |
| Tailor a resume to start tracking applications. | Optimize a resume for a job to start tracking applications. |
| Your data stays private… | keep |
| Sign In / Sign Out / Delete Account | keep |

---

## 12. Design

| Current | v2 |
|---|---|
| Recruiter-ready templates, one tap. | keep |
| 12 ATS-safe templates | 12 ATS-friendly templates |
| Swap layouts… Every template stays parseable by the bots. | Swap layouts, colors, and fonts. Every template stays simple to parse. |
| Template name `ATS` | `Classic` *(or keep product id internally; display “Classic”)* |
| Apply Design / Customise… | keep |

---

## 13. Marketing screenshot slots (App Store creatives)

| Slot | Current headline | v2 headline | Current subline | v2 subline | Current caption | v2 caption |
|---|---|---|---|---|---|---|
| tailor | Your resume, tailored for any job | Your resume, tailored for this job | Paste a posting. See what's blocking you. | Paste one posting. See what's missing. | AI resume tailor and ATS checker… | AI resume tailor and Match check for job seekers |
| blockers | See exactly what's blocking you | See exactly what's blocking you | Scores every section of your resume | Match signals across your resume | ATS resume score by section… | Resumely Match Score by section — not an employer ATS |
| aiEdits | AI edits that actually fit the role | Edits that fit the role — in your voice | Applied section by section, in one tap | Applied section by section, you approve | AI resume optimization by job description… | Targeted resume edits from the job description |
| templates | ATS-friendly templates that impress recruiters | ATS-friendly templates, clean export | Export a polished PDF from your phone | Export a polished PDF from your phone | Resume design templates - ATS safe… | Resume templates built for clean parsing |
| expert | Expert analysis for every section | Expert analysis for every section | Targeted rewrites at hiring-manager level | Targeted rewrites you can stand behind | Expert resume review with AI rewrite suggestions | Expert review with editable rewrite suggestions |

---

## 14. Share / Ambassador

| Current | v2 |
|---|---|
| My resume scored %lld%% on ATS — try ResumeBuilder AI: %@ | My Resumely Match Score was %lld%% for this job — try Resumely: %@ |
| Resume export — try ResumeBuilder AI: %@ | I exported a tailored resume with Resumely: %@ |
| Did you land the interview? | Did this application move forward? |
| Congrats! One step closer to the job. | Congrats — keep the momentum. |
| Here's a free export for your next application | Here's a free export for your next application |

---

## 15. Credits / Paywall (scaffold)

| Current | v2 |
|---|---|
| Get Credits / Credit Packs | keep |
| StoreKit wiring is scaffolded… | *(dev-only — hide from production UI)* |
| Paywall — coming soon | keep until monetization unparked |

---

# Part C — Backend / model guardrails (not UI keys)

These are required for v2 trust even if Localizable is perfect:

1. **Never surface raw concept tokens** (`job title business`, `synergy`, etc.) in gap titles.
2. Gap titles must be **human instructions** (“Add a metric…”, “Mirror the job’s title wording…”).
3. Prefer “using your own wording” in every rewrite suggestion footer.
4. Score explainer always near big % : estimate, not hiring guarantee, not employer ATS.

---

# Part D — Implementation packet (when approved)

1. Update English keys in `Localizable.xcstrings` (and Swift literals that seed them).
2. Hebrew parity pass for every changed key.
3. MarketingScreenshotView slot strings.
4. Share format strings.
5. Prompt/schema fix for diagnosis gap titles.
6. Post-export CTA order in `OptimizedResumeView` / export success stack.
7. Snapshot / UI tests that assert banned phrases: `Free ATS Check`, `Improve ATS`, `scored % on ATS`, `pass ATS`.

**Out of scope for v2 copy:** analytics event names (`ats_*` etc.), API field names, StoreKit products.

---

# Part E — Founder decision checklist

- [ ] Approve P0 renames (ATS score → Match / Free Match Check / Improve match)
- [ ] Approve auth headline soften (drop “60 seconds”)
- [ ] Approve post-export CTA reorder
- [ ] Approve Design template display name `ATS` → `Classic`
- [ ] Approve marketing screenshot caption pack
- [ ] Approve share string rewrites
- [ ] Authorize implementation session (code + HE) after 1.4.3 review noise settles — or sooner on a docs-only PR

---

## Related files

- Brief: `executive-os/research/2026-07-19-x-twitter-activation-gtm-hooks.md`
- Screen vs marketing snapshot: `executive-os/research/2026-07-19-resumely-brief-vs-marketing-and-app.md`
- Canonical marketing: `ResumeBuilder IOS APP/.agents/product-marketing.md`
- String catalog: `ResumeBuilder IOS APP/Resources/Localizable.xcstrings`
