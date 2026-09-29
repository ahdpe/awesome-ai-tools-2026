<div align="center">

# Awesome AI Tools 2026

**A curated, practical guide to AI tools that are genuinely useful in 2026.**

[![Awesome](https://awesome.re/badge.svg)](https://awesome.re)
[![Tools](https://img.shields.io/badge/tools-81-2ea44f)](#catalog)
[![Last updated](https://img.shields.io/badge/last%20updated-2026--09--29-0969da)](#maintenance)
[![Stars](https://img.shields.io/github/stars/ahdpe/awesome-ai-tools-2026?style=flat&logo=github)](https://github.com/ahdpe/awesome-ai-tools-2026/stargazers)
[![License: MIT](https://img.shields.io/badge/license-MIT-yellow.svg)](LICENSE)
[![PRs welcome](https://img.shields.io/badge/PRs-welcome-brightgreen.svg)](CONTRIBUTING.md)

</div>

<p align="center">
  <strong>English</strong> · <a href="README.ru.md">Русская версия</a>
</p>

> 81 tools across 10 categories. Every entry links to an official project or product page. No affiliate links and no paid placement.

This is a selective guide, not a dump of every product with “AI” in its name. It is designed to help people quickly find a sensible starting point and understand the tradeoffs before opening ten tabs.

## Start here

These are useful starting points, not universal winners:

| I want to... | Start with... |
|---|---|
| Use a general AI assistant | [ChatGPT](https://chatgpt.com/), [Claude](https://claude.ai/), [Gemini](https://gemini.google.com/) |
| Research with visible sources | [Perplexity](https://www.perplexity.ai/), [NotebookLM](https://notebooklm.google.com/) |
| Work with a codebase | [GitHub Copilot](https://github.com/features/copilot), [Cursor](https://www.cursor.com/), [Claude Code](https://docs.anthropic.com/en/docs/claude-code/overview), [OpenAI Codex](https://openai.com/codex/) |
| Build an AI agent | [LangGraph](https://www.langchain.com/langgraph), [OpenAI Agents SDK](https://openai.github.io/openai-agents-python/), [PydanticAI](https://ai.pydantic.dev/) |
| Run models privately | [Ollama](https://ollama.com/), [LM Studio](https://lmstudio.ai/), [Open WebUI](https://openwebui.com/) |
| Build retrieval or RAG | [Qdrant](https://qdrant.tech/), [pgvector](https://github.com/pgvector/pgvector), [Firecrawl](https://www.firecrawl.dev/) |
| Evaluate an LLM application | [Langfuse](https://langfuse.com/), [Arize Phoenix](https://arize.com/docs/phoenix/), [Promptfoo](https://www.promptfoo.dev/) |
| Create visual or audio media | [Midjourney](https://www.midjourney.com/), [Runway](https://runwayml.com/), [ElevenLabs](https://elevenlabs.io/) |

## Browse the catalog

- [Assistants & Research (8)](#assistants)
- [Coding Agents & Developer Tools (9)](#coding)
- [Agent Frameworks & Automation (9)](#agents)
- [Local AI & Inference (8)](#local)
- [RAG, Search & Knowledge (8)](#rag)
- [Evaluation & Observability (8)](#evaluation)
- [Image & Design (8)](#image)
- [Video & Avatars (7)](#video)
- [Voice, Audio & Music (7)](#audio)
- [Model APIs & Platforms (9)](#platforms)

<a id="catalog"></a>

## Catalog

<a id="assistants"></a>

### Assistants & Research

General-purpose assistants, answer engines, and tools for working with sources.

| Tool | Useful for | Access | Source | Local | API |
|---|---|---|---|:---:|:---:|
| **[ChatGPT](https://chatgpt.com/)** | General-purpose assistant for writing, analysis, research, files, and multimodal work. | Free tier | Closed | No | Yes |
| **[Claude](https://claude.ai/)** | Assistant for long documents, careful reasoning, writing, and collaborative work. | Free tier | Closed | No | Yes |
| **[Gemini](https://gemini.google.com/)** | Multimodal assistant integrated with Google's apps, search, and model ecosystem. | Free tier | Closed | No | Yes |
| **[Perplexity](https://www.perplexity.ai/)** | Answer engine focused on current web research with visible citations. | Free tier | Closed | No | Yes |
| **[Microsoft Copilot](https://copilot.microsoft.com/)** | Consumer and workplace assistant connected to Microsoft's productivity ecosystem. | Free tier | Closed | No | No |
| **[NotebookLM](https://notebooklm.google.com/)** | Source-grounded notebooks for summaries, questions, study guides, and audio overviews. | Free tier | Closed | No | No |
| **[Le Chat](https://chat.mistral.ai/)** | Mistral's multilingual assistant for chat, documents, search, and enterprise work. | Free tier | Closed | No | Yes |
| **[Clarity](https://agent-tools.cloud/services/desktop-o99r0sf-tail935fba-ts-net-sub899)** | Base mainnet x402 research gateway with free discovery plus paid USDC report and chat endpoints. | Paid | Closed | No | Yes |

<a id="coding"></a>

### Coding Agents & Developer Tools

Tools that understand codebases, edit files, review changes, and help ship software.

| Tool | Useful for | Access | Source | Local | API |
|---|---|---|---|:---:|:---:|
| **[GitHub Copilot](https://github.com/features/copilot)** | Coding assistance, chat, reviews, and agents integrated with GitHub and popular IDEs. | Free tier | Closed | No | No |
| **[Cursor](https://www.cursor.com/)** | AI-first code editor for repository-aware edits, chat, and agentic development. | Free tier | Closed | No | No |
| **[Devin Desktop](https://devin.ai/desktop)** | The new name for Windsurf: an agent command center with the full IDE, terminal workflows, and multi-agent management. | Free tier | Closed | No | No |
| **[Claude Code](https://docs.anthropic.com/en/docs/claude-code/overview)** | Terminal coding agent for understanding repositories, editing code, and running development tasks. | Paid | Closed | No | No |
| **[OpenAI Codex](https://openai.com/codex/)** | Coding agent for parallel tasks, implementation, review, refactoring, and repository work. | Free tier | Mixed | No | Yes |
| **[Aider](https://aider.chat/)** | Open-source terminal pair programmer with Git-aware edits and broad model support. | Open source | Open | Yes | No |
| **[Continue](https://www.continue.dev/)** | Open coding assistant platform for IDE chat, autocomplete, agents, and custom models. | Open source | Mixed | Yes | No |
| **[Cline](https://cline.bot/)** | Open-source IDE agent with file editing, terminal use, browser control, and approvals. | Open source | Open | Yes | No |
| **[Roo Code](https://roocode.com/)** | Open-source coding agent with specialized modes, model choice, and extensible workflows. | Open source | Open | Yes | No |

<a id="agents"></a>

### Agent Frameworks & Automation

SDKs and platforms for tool use, orchestration, durable workflows, and multi-agent systems.

| Tool | Useful for | Access | Source | Local | API |
|---|---|---|---|:---:|:---:|
| **[LangChain](https://www.langchain.com/)** | Model-agnostic framework and integrations for tools, retrieval, and agent applications. | Open source | Mixed | Yes | Yes |
| **[LangGraph](https://www.langchain.com/langgraph)** | Low-level runtime for durable, stateful agents with streaming and human approval. | Open source | Open | Yes | Yes |
| **[OpenAI Agents SDK](https://openai.github.io/openai-agents-python/)** | Lightweight SDK for agents, tools, handoffs, guardrails, sessions, and tracing. | Open source | Open | Yes | Yes |
| **[Google Agent Development Kit](https://google.github.io/adk-docs/)** | Google's open toolkit for building, evaluating, and deploying modular agents. | Open source | Open | Yes | Yes |
| **[LlamaIndex](https://www.llamaindex.ai/)** | Framework for agents and context-augmented applications built around private data. | Open source | Mixed | Yes | Yes |
| **[CrewAI](https://www.crewai.com/)** | Framework and platform for role-based agent crews and automated workflows. | Open source | Mixed | Yes | Yes |
| **[Microsoft AutoGen](https://microsoft.github.io/autogen/stable/)** | Event-driven framework for conversational and scalable multi-agent applications. | Open source | Open | Yes | Yes |
| **[PydanticAI](https://ai.pydantic.dev/)** | Typed Python agent framework with structured outputs, tools, validation, and model portability. | Open source | Open | Yes | Yes |
| **[Dify](https://dify.ai/)** | Visual platform for AI workflows, RAG applications, agents, and model operations. | Free tier | Source available | Yes | Yes |

<a id="local"></a>

### Local AI & Inference

Run models privately on laptops, workstations, or your own servers.

| Tool | Useful for | Access | Source | Local | API |
|---|---|---|---|:---:|:---:|
| **[Ollama](https://ollama.com/)** | Simple local model runtime with a CLI, model library, and HTTP API. | Free | Open | Yes | Yes |
| **[LM Studio](https://lmstudio.ai/)** | Desktop app for discovering, running, and serving local language models. | Free | Mixed | Yes | Yes |
| **[llama.cpp](https://github.com/ggml-org/llama.cpp)** | Efficient C/C++ inference engine for running quantized models across many devices. | Open source | Open | Yes | Yes |
| **[vLLM](https://vllm.ai/)** | High-throughput open inference and serving engine for production language models. | Open source | Open | Yes | Yes |
| **[Open WebUI](https://openwebui.com/)** | Self-hosted chat interface for local and hosted models with tools and knowledge bases. | Free | Source available | Yes | Yes |
| **[LocalAI](https://localai.io/)** | OpenAI-compatible local inference stack for text, images, audio, and embeddings. | Open source | Open | Yes | Yes |
| **[Jan](https://jan.ai/)** | Open-source desktop assistant for private local models and optional cloud providers. | Open source | Open | Yes | Yes |
| **[MLX](https://github.com/ml-explore/mlx)** | Apple Silicon array framework for efficient local machine learning research and inference. | Open source | Open | Yes | Yes |

<a id="rag"></a>

### RAG, Search & Knowledge

Retrieval, vector search, web extraction, and document preparation for AI applications.

| Tool | Useful for | Access | Source | Local | API |
|---|---|---|---|:---:|:---:|
| **[Qdrant](https://qdrant.tech/)** | Vector database and similarity search engine for retrieval-heavy AI applications. | Free tier | Mixed | Yes | Yes |
| **[Weaviate](https://weaviate.io/)** | Open vector database with hybrid search, multimodal retrieval, and managed hosting. | Free tier | Mixed | Yes | Yes |
| **[Milvus](https://github.com/milvus-io/milvus)** | Distributed open-source vector database designed for large-scale similarity search. | Open source | Open | Yes | Yes |
| **[Chroma](https://www.trychroma.com/)** | Developer-friendly retrieval database for embeddings, documents, and AI application memory. | Free tier | Mixed | Yes | Yes |
| **[pgvector](https://github.com/pgvector/pgvector)** | PostgreSQL extension for vector similarity search alongside relational application data. | Open source | Open | Yes | No |
| **[Pinecone](https://www.pinecone.io/)** | Managed vector database for semantic search, recommendations, and production retrieval. | Free tier | Closed | No | Yes |
| **[Firecrawl](https://www.firecrawl.dev/)** | Web crawling and extraction that turns sites into LLM-ready structured content. | Free tier | Mixed | Yes | Yes |
| **[Unstructured](https://unstructured.io/)** | Document ingestion and partitioning for PDFs, office files, email, and enterprise data. | Free tier | Mixed | Yes | Yes |

<a id="evaluation"></a>

### Evaluation & Observability

Trace, test, evaluate, and monitor LLM applications and agents.

| Tool | Useful for | Access | Source | Local | API |
|---|---|---|---|:---:|:---:|
| **[LangSmith](https://www.langchain.com/langsmith)** | Framework-agnostic tracing, evaluation, testing, monitoring, and agent deployment platform. | Free tier | Closed | No | Yes |
| **[Langfuse](https://langfuse.com/)** | Open-source LLM observability, prompt management, evaluation, and usage analytics. | Free tier | Mixed | Yes | Yes |
| **[Arize Phoenix](https://arize.com/docs/phoenix/)** | Open-source tracing and evaluation for LLM applications, agents, and retrieval systems. | Open source | Open | Yes | Yes |
| **[W&B Weave](https://wandb.ai/site/weave)** | Tracing, evaluation, and iteration tools for AI applications and model pipelines. | Free tier | Mixed | Yes | Yes |
| **[MLflow](https://mlflow.org/)** | Open platform for experiment tracking, model management, evaluation, and generative AI observability. | Open source | Open | Yes | Yes |
| **[DeepEval](https://deepeval.com/)** | Open-source testing and evaluation framework for LLM outputs, RAG, and agents. | Open source | Mixed | Yes | Yes |
| **[Ragas](https://ragas.io/)** | Evaluation framework focused on retrieval pipelines and context-grounded AI applications. | Open source | Mixed | Yes | Yes |
| **[Promptfoo](https://www.promptfoo.dev/)** | Open-source CLI for prompt tests, model comparisons, red teaming, and CI checks. | Open source | Open | Yes | Yes |

<a id="image"></a>

### Image & Design

Image generation, editing, design assistance, and visual workflows.

| Tool | Useful for | Access | Source | Local | API |
|---|---|---|---|:---:|:---:|
| **[Midjourney](https://www.midjourney.com/)** | High-quality image generation with strong artistic direction and style exploration. | Paid | Closed | No | No |
| **[Adobe Firefly](https://firefly.adobe.com/)** | Generative image and design tools integrated across Adobe creative applications. | Free tier | Closed | No | Yes |
| **[Canva AI](https://www.canva.com/ai/)** | Accessible AI design suite for presentations, social graphics, images, and brand assets. | Free tier | Closed | No | No |
| **[Ideogram](https://ideogram.ai/)** | Image generation particularly useful for typography, posters, logos, and graphic layouts. | Free tier | Closed | No | Yes |
| **[Leonardo.Ai](https://leonardo.ai/)** | Creative production platform for images, assets, editing, and consistent visual styles. | Free tier | Closed | No | Yes |
| **[FLUX](https://blackforestlabs.ai/)** | Black Forest Labs image models available through APIs and selected open weights. | Mixed | Mixed | Yes | Yes |
| **[ComfyUI](https://www.comfy.org/)** | Node-based open workflow system for local image and generative media models. | Open source | Open | Yes | Yes |
| **[Invoke](https://invoke.ai/)** | Professional creative engine for controlled image generation, workflows, and team use. | Open source | Mixed | Yes | Yes |

<a id="video"></a>

### Video & Avatars

Text-to-video, video editing, synthetic presenters, and production tools.

| Tool | Useful for | Access | Source | Local | API |
|---|---|---|---|:---:|:---:|
| **[Sora](https://openai.com/sora/)** | OpenAI video generation and editing for text, images, and visual storytelling. | Paid | Closed | No | Yes |
| **[Runway](https://runwayml.com/)** | Generative video platform with creation, transformation, editing, and production controls. | Free tier | Closed | No | Yes |
| **[Google Veo](https://deepmind.google/models/veo/)** | Google's video generation model family for cinematic clips and controllable audio-visual output. | Paid | Closed | No | Yes |
| **[Luma Dream Machine](https://lumalabs.ai/dream-machine)** | Image and video generation focused on motion, cinematic control, and fast iteration. | Free tier | Closed | No | Yes |
| **[Kling AI](https://klingai.com/)** | Text-to-video and image-to-video generation with consumer-friendly creative controls. | Free tier | Closed | No | Yes |
| **[HeyGen](https://www.heygen.com/)** | AI avatars, voice translation, and presenter videos for business communication. | Free tier | Closed | No | Yes |
| **[Synthesia](https://www.synthesia.io/)** | Enterprise avatar videos for training, onboarding, localization, and internal communication. | Paid | Closed | No | Yes |

<a id="audio"></a>

### Voice, Audio & Music

Speech synthesis, transcription, voice agents, editing, and music generation.

| Tool | Useful for | Access | Source | Local | API |
|---|---|---|---|:---:|:---:|
| **[ElevenLabs](https://elevenlabs.io/)** | Speech synthesis, voice cloning, dubbing, transcription, and conversational voice agents. | Free tier | Closed | No | Yes |
| **[Descript](https://www.descript.com/)** | Text-based editing for podcasts and video with transcription and voice tools. | Free tier | Closed | No | No |
| **[Suno](https://suno.com/)** | Song generation from prompts with vocals, lyrics, arrangement, and style controls. | Free tier | Closed | No | No |
| **[Udio](https://www.udio.com/)** | AI music creation and extension with prompting, remixing, and track controls. | Free tier | Closed | No | No |
| **[Deepgram](https://deepgram.com/)** | Low-latency speech-to-text, text-to-speech, and voice agent APIs. | Free tier | Closed | No | Yes |
| **[Cartesia](https://cartesia.ai/)** | Real-time voice generation infrastructure for responsive conversational applications. | Free tier | Closed | No | Yes |
| **[OpenAI Whisper](https://github.com/openai/whisper)** | Open-source multilingual speech recognition and translation model for local transcription. | Open source | Open | Yes | Yes |

<a id="platforms"></a>

### Model APIs & Platforms

Hosted model access, inference APIs, routing, and developer platforms.

| Tool | Useful for | Access | Source | Local | API |
|---|---|---|---|:---:|:---:|
| **[OpenAI API](https://platform.openai.com/docs/overview)** | Developer platform for text, reasoning, multimodal, realtime, image, audio, and agent APIs. | Usage-based | Closed | No | Yes |
| **[Anthropic API](https://docs.anthropic.com/en/api/getting-started)** | Claude model API with tool use, prompt caching, batches, and enterprise controls. | Usage-based | Closed | No | Yes |
| **[Google AI Studio](https://aistudio.google.com/)** | Browser workspace and API access for prototyping with Google's Gemini models. | Free tier | Closed | No | Yes |
| **[Mistral AI La Plateforme](https://docs.mistral.ai/getting-started/platform-overview/)** | Mistral model APIs for text, coding, documents, embeddings, and agents. | Usage-based | Mixed | No | Yes |
| **[GroqCloud](https://console.groq.com/)** | Low-latency hosted inference for supported open and commercial models. | Free tier | Closed | No | Yes |
| **[Together AI](https://www.together.ai/)** | Cloud platform for open-model inference, fine-tuning, dedicated endpoints, and GPU workloads. | Usage-based | Closed | No | Yes |
| **[Fireworks AI](https://fireworks.ai/)** | Fast model inference, fine-tuning, and production deployment for generative applications. | Usage-based | Closed | No | Yes |
| **[OpenRouter](https://openrouter.ai/)** | Unified API and routing layer for models from many different providers. | Mixed | Closed | No | Yes |
| **[Hugging Face Inference Providers](https://huggingface.co/docs/inference-providers/index)** | Unified access to hosted models and inference providers through the Hugging Face ecosystem. | Free tier | Mixed | No | Yes |

## How entries are labeled

- **Access** describes the easiest entry point, not every pricing plan. Pricing changes often; verify it on the official site.
- **Source** is `Open`, `Closed`, `Mixed`, or `Source available`. `Mixed` usually means an open client or model exists alongside proprietary hosted services.
- **Local** means a meaningful part of the tool or model can run on your own hardware. A desktop client that only calls a cloud model is not counted as local.
- **API** means there is a documented developer API or SDK, not merely an unofficial integration.

## Selection criteria

An entry should:

1. Solve a clear, practical problem.
2. Be usable or actively maintained as of the review date.
3. Link to an official product, documentation, or source repository.
4. Offer distinct value instead of duplicating a stronger entry.
5. Describe access and openness without promotional claims.

We deliberately exclude abandoned projects, thin wrappers with no meaningful differentiation, affiliate links, undisclosed sponsored placement, and tools whose primary purpose is harmful or deceptive activity.

## Contributing

Suggestions and corrections are welcome. Read [CONTRIBUTING.md](CONTRIBUTING.md) before opening a pull request. Vendors may submit their own product, but must disclose their affiliation and use the same factual format as every other entry.

The catalog is generated from [`data/tools.json`](data/tools.json). Do not edit the catalog tables by hand.

<a id="maintenance"></a>

## Maintenance

Last reviewed: **September 29, 2026**.

- Structured data and both language versions are checked in CI.
- Links are checked on pull requests and on a weekly schedule.
- Stale or discontinued tools move out of the active catalog.
- Pricing and feature labels are snapshots, not guarantees.

## License

[MIT](LICENSE). Descriptions are provided for informational purposes; product names and trademarks belong to their respective owners.
