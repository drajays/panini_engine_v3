import re
with open("webui/app.py", "r") as f:
    content = f.read()

new_route = """
@app.route("/api/matrix/rules")
def api_matrix_rules():
    \"\"\"Derive all 24 cells, collect all applied sutras, and group by sutra.\"\"\"
    stem  = request.args.get("stem", "rAma")
    linga = request.args.get("linga", "pulliṅga")
    from phonology.joiner import slp1_to_devanagari
    
    rules = {}
    for v in range(1, 9):
        for vv in range(1, 4):
            key = f"{v}-{vv}"
            try:
                state = derive(stem, v, vv, linga=linga)
                produced = (slp1_to_devanagari(state.terms[0].varnas)
                            if state.terms else "")
                
                path = extract_applied_path(state.trace)
                for sid in path:
                    if sid not in rules:
                        # fetch sutra details
                        sutra_node = SUTRA_REGISTRY.get(sid)
                        rules[sid] = {
                            "id": sid,
                            "text_dev": sutra_node.text_dev if sutra_node else "",
                            "type_dev": sutra_node.sutra_type.name if sutra_node else "",
                            "forms": [],
                            "cells": []
                        }
                    if produced not in rules[sid]["forms"]:
                        rules[sid]["forms"].append(produced)
                    rules[sid]["cells"].append(key)
            except Exception:
                pass
                
    # Convert to list and sort by sutra ID (which typically reflects Panini order for standard IDs like x.y.z)
    def parse_sid(sid):
        try:
            return tuple(int(x) for x in sid.split("."))
        except:
            return (99,99,99)
            
    rules_list = sorted(rules.values(), key=lambda r: parse_sid(r["id"]))
    
    return jsonify({
        "stem": stem,
        "linga": linga,
        "rules": rules_list
    })
"""

# Insert before @app.route("/patha")
if "@app.route(\"/api/matrix/rules\")" not in content:
    content = content.replace('@app.route("/patha")', new_route + '\n@app.route("/patha")')
    with open("webui/app.py", "w") as f:
        f.write(content)
