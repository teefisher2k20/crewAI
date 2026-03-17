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

    content = content.replace(' // NOSONAR', '')

    with open(file, 'w', encoding='utf-8') as f:
        f.write(content)

print('Done fixing NOSONAR tags.')  # noqa: T201
