**English** | [中文](./README_zh.md)

# HitCC

## Complete reverse-engineering documentation of the full logic of Claude Code CLI Node.js version v2.1.84

HitCC is not a source code repository. It is a documentation knowledge base for learning, analysis, and rewrite work.  
The goal of this project is not to reconstruct the original file tree, but to recover Claude Code CLI's core runtime logic, module boundaries, configuration system, and surrounding ecosystem as faithfully as possible, so it can serve as a stable reference for a runnable alternative or a high-similarity rewrite.

This project is not affiliated with Anthropic PBC. The repository does not contain Claude Code original source code, cracking content, or implementations intended to bypass product policies or permission mechanisms.

## Notes

To obtain the Claude Code CLI package analyzed by this repository:
```sh
npm pack @anthropic-ai/claude-code@2.1.84
```

The Python scripts under `recovery_tools/` can perform an initial round of cleanup on obfuscated or encrypted source code.

This repository is based only on static analysis of Claude Code CLI v2.1.84 obtained through the method above. It does not include runtime dynamic analysis, and it did not use any Anthropic PBC network services, including LLM inference services.

The documentation content in this repository may be quite extensive. The current statistics for the `docs/` directory (the following data may not be updated in real time):

```
TOTAL
  Files: 81
  Lines: 27170
  Chars: 698707
  Bytes: 953399
```


## What This Repository Provides

- Structured reverse-engineering documentation for the main Claude Code CLI execution chain
- Topic-oriented analysis from startup entry to the Agent Loop, Tool Use, prompt assembly, and session persistence
- Split-out explanations of surrounding systems such as MCP, Plugin, Skill, TUI, Remote Persistence, and Bridge
- Candidate architecture, known boundaries, and open questions for rewrite-oriented engineering

## What This Repository Does Not Provide

- Reconstruction of the original source file structure
- Private server-side implementation details
- A guarantee of 1:1 behavioral reproduction
- A directly runnable CLI, SDK, or installation script

## Documentation Coverage

The current knowledge base is not organized by the original source tree. It is organized by runtime topics that can be reconstructed with stable confidence.  
At present, the coverage of `docs/` can be understood by directory:

- `00-overview`
  - Scope boundaries, evidence sources, confidence terminology, and documentation maintenance conventions
- `01-runtime`
  - CLI entry, command tree, and runtime mode dispatch
  - Session / Transcript persistence and recovery
  - Input compilation pipeline, main Agent Loop, and compact branch
  - Model adapter, provider selection, auth, stream handling, and remote transport
  - Two built-in network tools: `web-search` and `web-fetch`
  - Telemetry, control plane, and non-LLM network paths
  - Settings sources, paths, merging, caching, write-back, and key consumption surfaces
- `02-execution`
  - Tool execution core, concurrent execution, Hook runtime, Permission / Sandbox / Approval
  - Instruction discovery, rules, prompt assembly, and context layering
  - Non-main-thread prompt paths, attachment lifecycle, context modifiers, and tool-use context
- `03-ecosystem`
  - Resume, Fork, Sidechain, Subagent, and agent team
  - Remote persistence, bridge, and Plan system
  - MCP, Skill, Plugin, TUI, and their runtime interaction boundaries
- `04-rewrite`
  - Candidate layering, directory skeleton, open questions, and blocking judgments for rewrite engineering
- `05-appendix`
  - Unified terminology and evidence indexes such as the glossary and evidence map

## Current Conclusions

Based on the current evidence boundary, this documentation set is already sufficient to support:

- Reconstructing a runnable alternative
- A modular high-similarity rewrite

But it is still insufficient to promise:

- Accurate reconstruction of the original project directory
- Full reconstruction of private server-side black-box logic
- 1:1 reproduction of all edge-case behaviors in the original product

For more specific judgments, see:

- [Scope, Evidence, and Conclusions](./docs/00-overview/01-scope-and-evidence.md)
- [Rewrite Judgment, Blocking Open Questions, and Next Evidence Work](./docs/04-rewrite/02-open-questions-and-judgment.md)

## Recommended Reading Order

1. Start with [docs/00-overview/01-scope-and-evidence.md](./docs/00-overview/01-scope-and-evidence.md) to understand what this documentation already knows and what is still unknown.
2. Then read [docs/01-runtime/01-product-cli-and-modes.md](./docs/01-runtime/01-product-cli-and-modes.md) and the other `01-runtime` pages to build a model of the product shape and the main runtime chain.
3. Continue with `02-execution` to connect prompt handling, tool use, hooks, permissions, attachments, and related execution paths.
4. Then move into `03-ecosystem` to complete the surrounding systems: MCP, Plugin, Skill, TUI, Remote, and Plan.
5. Finally, read `04-rewrite` to connect the current knowledge boundary with practical engineering strategy.

If you only want a quick entry point, start directly from [docs/00-overview/00-index.md](./docs/00-overview/00-index.md).

## Maintenance Principles

This repository is maintained as a knowledge base rather than a single long-form document. The core principles are:

- `00-overview/00-index.md` is only the global entry point and does not duplicate main content
- Parent pages only provide navigation and boundary descriptions, not long-form mechanism analysis
- Child pages hold the actual content, evidence points, counter-evidence, and open questions
- Unknowns are centralized in the scope page and rewrite judgment page to avoid duplicate maintenance across multiple directory pages
- When new evidence appears, update the relevant topic page first, then backfill the glossary or evidence map

Detailed conventions are described in:

- [docs/00-overview/02-document-style-and-structure-conventions.md](./docs/00-overview/02-document-style-and-structure-conventions.md)

## Suitable Use Cases

This repository is more suitable for:

- Studying the system structure and responsibility boundaries of Claude Code CLI
- Providing architectural reference for self-built agentic coding shells
- Defining stable knowledge boundaries for high-similarity rewrite work
- Cross-checking where a feature sits inside the main runtime chain

It is not suitable for:

- Searching for original source code
- Expecting a directly runnable replacement implementation
- Pursuing full reconstruction of private server-side logic

## License

Copyright (c) 2026 Hitmux contributors

This project is licensed under [Creative Commons Attribution 4.0 International (CC BY 4.0)](https://creativecommons.org/licenses/by/4.0/).

This means you may:

- Copy and redistribute the project content
- Modify, adapt, and republish it
- Use it in commercial or non-commercial scenarios

But you must:

- Preserve attribution to the original authors or source
- Include a link to the license
- Indicate whether changes were made

See [LICENSE](./LICENSE) in the repository root for the full license text.

## Acknowledgements

Thanks to the [Linux Do](https://linux.do) community for its support.

## Disclaimer

Please use this project only for learning, research, teaching, or legitimate engineering analysis.  
Any use of this project to infringe Anthropic PBC's lawful rights or to bypass product policies is unrelated to this project, and the risk is solely the user's responsibility.

The authors assume no legal responsibility for the accuracy or completeness of the documentation, or for any direct or indirect loss caused by using it, including but not limited to legal risk, technical failure, or data loss.


## Star History

<a href="https://www.star-history.com/?repos=hitmux%2Fhitcc&type=date&legend=top-left">
 <picture>
   <source media="(prefers-color-scheme: dark)" srcset="https://api.star-history.com/image?repos=hitmux/hitcc&type=date&theme=dark&legend=top-left" />
   <source media="(prefers-color-scheme: light)" srcset="https://api.star-history.com/image?repos=hitmux/hitcc&type=date&legend=top-left" />
   <img alt="Star History Chart" src="https://api.star-history.com/image?repos=hitmux/hitcc&type=date&legend=top-left" />
 </picture>
</a>
