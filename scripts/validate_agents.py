"""Validate package integrity and migration preservation. Does not execute agents."""
from pathlib import Path
import hashlib,json,re
ROOT=Path(__file__).resolve().parents[1]
index=json.loads((ROOT/'agents-catalog.json').read_text());migration=json.loads((ROOT/'migration.json').read_text())
assert len({x['slug'] for x in index})==len(index)==migration['total_agents']
def exists(path):
 p=(ROOT/path).resolve();assert p.is_relative_to(ROOT),path;assert p.exists(),path;return p
for row in index:
 slug=row['slug'];assert re.fullmatch(r'[a-z0-9]+(?:-[a-z0-9]+)*',slug)
 a=exists(row['manifest']);d=json.loads(a.read_text());assert d['slug']==slug and d['schema_version']==1
 for name in ['README.md','specification.md','workflow.mmd','schemas/README.md','fixtures/README.md','evaluations/README.md']:exists(a.parent/ name)
 graph=(a.parent/'workflow.mmd').read_text();assert graph.startswith('flowchart LR\n')
 assert 'click ' not in graph and '%%{' not in graph
 if d['source_graph']['nodes']:
  assert graph.count(' -->|')==len(d['source_graph']['edges'])
 for impl in d['implementations']:
  exists(impl['path']+'/README.md');assert impl['status'] in ['planned','source-available','reported-fixture-tested','fixture-tested','live-tested']
  if impl['status']=='planned':assert 'files' not in impl and not impl['runtime_tested']
  for path in impl.get('files',[]):exists(path)
 for p in d['prompts']:
  text=exists(p['path']).read_text();assert '## Build' in text and '## Operate' in text
 # Check only new package docs; preserve historical implementation reports verbatim.
 for p in a.parent.rglob('*.md'):
  if 'implementations/n8n' in str(p):continue
  for href in re.findall(r'\]\(([^)]+)\)',p.read_text()):
   if href.startswith(('https:','http:','#','mailto:')):continue
   target=href.split('#')[0];assert (p.parent/target).exists(),(p,href)
for move in migration['moves']:
 p=exists(move['to']);assert hashlib.sha256(p.read_bytes()).hexdigest()==move['sha256'],p
 assert not (ROOT/move['from']).exists(),move['from']
for path,sha in migration['original_n8n_file_hashes'].items():assert hashlib.sha256(exists(path).read_bytes()).hexdigest()==sha
print(f'PASS: {len(index)} agent packages, implementation states, prompts, Mermaid graph counts, local links; all {len(migration["moves"])} collected JSON hashes unchanged.')
