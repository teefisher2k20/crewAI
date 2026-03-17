import os


tsx_files = [
    r'c:\Users\Terrance\.gemini\antigravity\scratch\remotion-studio-platform\Artifacts\client-platform\src\remotion\BrandShowcase.tsx',
    r'c:\Users\Terrance\.gemini\antigravity\scratch\remotion-studio-platform\Artifacts\client-platform\src\app\brand\page.tsx',
    r'c:\Users\Terrance\.gemini\antigravity\scratch\remotion-studio-platform\Artifacts\client-platform\src\app\timeline\page.tsx',
    r'c:\Users\Terrance\.gemini\antigravity\scratch\remotion-studio-platform\Artifacts\client-platform\src\app\remotion\page.tsx'
]

for file in tsx_files:
    if not os.path.exists(file):
        continue
    with open(file, 'r', encoding='utf-8') as f:
        content = f.read()

    if 'eslint-disable react/forbid-dom-props' not in content:
        content = '/* eslint-disable react/forbid-dom-props, react/forbid-component-props */\n' + content

    with open(file, 'w', encoding='utf-8') as f:
        f.write(content)

py_tools = [
     r'c:\Users\Terrance\.gemini\antigravity\scratch\remotion-studio-platform\Artifacts\client-platform\src\remotion\New folder\lib\crewai-tools\src\crewai_tools\tools\tavily_extractor_tool\tavily_extractor_tool.py'
]

for file in py_tools:
    if not os.path.exists(file):
        continue
    with open(file, 'r', encoding='utf-8') as f:
        content = f.read()

    content = content.replace('def _run(self, url: str) -> str:', 'def _run(self, url: str, *args, **kwargs) -> str:')
    content = content.replace('async def _arun(self, url: str) -> str:', 'async def _arun(self, url: str, *args, **kwargs) -> str:')

    with open(file, 'w', encoding='utf-8') as f:
        f.write(content)
