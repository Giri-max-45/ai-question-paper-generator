# LLM prompts

Prompt files are filled in later stages (not used in Stage 1):

| File | Stage | Purpose |
|------|-------|---------|
| `topic_extraction.txt` | 3 | Modules / topics / subtopics JSON |
| `question_generation.txt` | 6 | Examination questions from retrieved context only |
| `difficulty.txt` | 7 | Easy/medium/hard + Bloom level |
| `validation.txt` | 9 | Syllabus / clarity / marks checks |
| `question_improvement.txt` | 9 | Rewrite rejected questions |
| `previous_paper_analysis.txt` | 11 | Frequency patterns, do not copy questions |
