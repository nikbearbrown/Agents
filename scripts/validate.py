"""Validate publication artifacts without executing any workflow."""
import json, hashlib, re
from pathlib import Path
root=Path(__file__).resolve().parents[1]
catalog=json.loads((root/'catalog.json').read_text())
assert len({r['folder'] for r in catalog})==len(catalog)
for r in catalog:
 assert re.fullmatch('[a-z0-9]+(?:-[a-z0-9]+)*',r['folder']),r['folder']
 p=root/r['readme'];assert p.exists(),p
 if not r['json']:continue
 f=root/r['json'];d=json.loads(f.read_text());assert d.get('active') is False,f
 assert isinstance(d['nodes'],list) and isinstance(d['connections'],dict),f
 assert any(n['type']=='n8n-nodes-base.stickyNote' and n['name']=='Publication · Overview and setup' for n in d['nodes']),f
 assert not any('credentials' in n for n in d['nodes']),f
 assert not any(k in d for k in ('pinData','staticData','meta')),f
 prov=json.loads((f.parent/'provenance.json').read_text())
 assert prov['publication_sha256']==hashlib.sha256(f.read_bytes()).hexdigest(),f
 assert prov['license_evidence'],f
 assert (root/'licenses'/prov['license_evidence']['notice']).exists(),f
print(f'PASS: {len(catalog)} folder READMEs, JSON files, inactive flags, source hashes, annotation records and license notices')
