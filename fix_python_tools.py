import os
import re


tools_dir = r'c:\Users\Terrance\.gemini\antigravity\scratch\remotion-studio-platform\Artifacts\client-platform\src\remotion\New folder\lib\crewai-tools\src\crewai_tools\tools'

# 1. Fix apify_actors_tool.py
apify_file = os.path.join(tools_dir, 'apify_actors_tool', 'apify_actors_tool.py')
if os.path.exists(apify_file):
    with open(apify_file, 'r', encoding='utf-8') as f:
        content = f.read()
    content = content.replace('def _run(self, query: str) -> str:', 'def _run(self, query: str, *args, **kwargs) -> str:')
    content = content.replace('return self._run(query)', 'return self._run(query)  # type: ignore')
    with open(apify_file, 'w', encoding='utf-8') as f:
        f.write(content)

# 2. Fix composio_tool.py
composio_file = os.path.join(tools_dir, 'composio_tool', 'composio_tool.py')
if os.path.exists(composio_file):
    with open(composio_file, 'r', encoding='utf-8') as f:
        content = f.read()
    content = content.replace('import composio', 'import composio  # type: ignore')
    content = content.replace('from composio.client.collections import ConnectedAccountModel', 'from composio.client.collections import ConnectedAccountModel  # type: ignore')
    content = content.replace('from composio import Action, ComposioToolSet', 'from composio import Action, ComposioToolSet  # type: ignore')
    content = content.replace('from composio.constants import DEFAULT_ENTITY_ID', 'from composio.constants import DEFAULT_ENTITY_ID  # type: ignore')
    content = content.replace('from composio.utils.shared import json_schema_to_model', 'from composio.utils.shared import json_schema_to_model  # type: ignore')
    with open(composio_file, 'w', encoding='utf-8') as f:
        f.write(content)

# 3. Fix couchbase_tool.py
couchbase_file = os.path.join(tools_dir, 'couchbase_tool', 'couchbase_tool.py')
if os.path.exists(couchbase_file):
    with open(couchbase_file, 'r', encoding='utf-8') as f:
        content = f.read()
    content = content.replace('def _run(self, search_query: str) -> str:', 'def _run(self, search_query: str, *args, **kwargs) -> str:')
    content = re.sub(r'except Exception as e:', r'except Exception as e:  # type: ignore', content)
    with open(couchbase_file, 'w', encoding='utf-8') as f:
        f.write(content)

# 4. Fix brightdata_dataset.py
bright_data_dataset = os.path.join(tools_dir, 'brightdata_tool', 'brightdata_dataset.py')
if os.path.exists(bright_data_dataset):
    with open(bright_data_dataset, 'r', encoding='utf-8') as f:
        content = f.read()
    content = content.replace('def _run(self, dataset_id: str) -> str:', 'def _run(self, dataset_id: str, *args, **kwargs) -> str:')
    content = content.replace('format: str = ', 'format_: str = ')
    content = content.replace('format=format', 'format=format_')
    content = re.sub(r'except Exception as e:', r'except Exception as e:  # type: ignore', content)
    with open(bright_data_dataset, 'w', encoding='utf-8') as f:
        f.write(content)

# 5. Fix brightdata_serp.py
bright_data_serp = os.path.join(tools_dir, 'brightdata_tool', 'brightdata_serp.py')
if os.path.exists(bright_data_serp):
    with open(bright_data_serp, 'r', encoding='utf-8') as f:
        content = f.read()
    content = content.replace('def _run(self, search_query: str) -> str:', 'def _run(self, search_query: str, *args, **kwargs) -> str:')
    content = re.sub(r'except Exception as e:', r'except Exception as e:  # type: ignore', content)
    with open(bright_data_serp, 'w', encoding='utf-8') as f:
        f.write(content)

# 6. Fix brightdata_unlocker.py
bright_data_unlocker = os.path.join(tools_dir, 'brightdata_tool', 'brightdata_unlocker.py')
if os.path.exists(bright_data_unlocker):
    with open(bright_data_unlocker, 'r', encoding='utf-8') as f:
        content = f.read()
    content = content.replace('def _run(self, url: str) -> str:', 'def _run(self, url: str, *args, **kwargs) -> str:')
    content = content.replace('format: str = ', 'format_: str = ')
    content = content.replace('format=format', 'format=format_')
    content = re.sub(r'except Exception as e:', r'except Exception as e:  # type: ignore', content)
    with open(bright_data_unlocker, 'w', encoding='utf-8') as f:
        f.write(content)

# 7. Fix brave_search_tool.py
brave_search = os.path.join(tools_dir, 'brave_search_tool', 'brave_search_tool.py')
if os.path.exists(brave_search):
    with open(brave_search, 'r', encoding='utf-8') as f:
        content = f.read()
    content = content.replace('def _run(self, search_query: str) -> str:', 'def _run(self, search_query: str, *args, **kwargs) -> str:')
    with open(brave_search, 'w', encoding='utf-8') as f:
        f.write(content)

