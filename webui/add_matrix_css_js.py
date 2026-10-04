import re
with open("webui/templates/matrix.html", "r") as f:
    content = f.read()

head_extra = """
{% block head_extra %}
<style>
.tabs { display: flex; gap: 4px; border-bottom: 1px solid var(--line); margin: 10px 0 8px; }
.tabs button { background: none; color: var(--ink-dim); border: 1px solid transparent; border-bottom: none; padding: 6px 16px; font-size: 1.1rem; font-family: var(--dev); cursor: pointer; }
.tabs button.active { background: var(--bg-panel); border-color: var(--line); color: var(--accent); border-radius: 4px 4px 0 0; }
.rules-table { width: 100%; border-collapse: collapse; font-size: 14px; margin-top: 1rem; }
.rules-table th { text-align: left; padding: 8px; border-bottom: 1px solid var(--line); font-weight: 600; color: var(--ink-dim); font-size: 0.9em; }
.rules-table td { padding: 8px; border-bottom: 1px solid var(--line-soft); vertical-align: top; }
.rules-table tr:hover td { background: var(--bg-subtle); }
.rules-table .sutra-id { font-family: var(--mono); font-size: 0.85em; color: var(--accent); display: block; margin-top: 4px; }
.rules-table .sutra-text { font-family: var(--dev); font-size: 1.2em; color: var(--ink); }
.rules-table .sutra-type { font-size: 0.8em; color: var(--ink-faint); padding: 2px 6px; border: 1px solid var(--line); border-radius: 4px; display: inline-block; margin-bottom: 4px; }
.rules-table .forms-list { font-family: var(--dev); color: var(--ink); font-size: 1.1em; line-height: 1.5; }
.rules-table .cells-list { font-size: 0.8em; color: var(--ink-faint); margin-top: 4px; }
</style>
{% endblock %}
"""

if "{% block head_extra %}" not in content:
    content = content.replace("{% block content %}", head_extra + "\n{% block content %}")

js_additions = """
/* ── Tabs logic ── */
document.querySelectorAll(".tabs button").forEach(btn => {
  btn.addEventListener("click", () => {
    document.querySelectorAll(".tabs button").forEach(b => b.classList.remove("active"));
    btn.classList.add("active");
    const tabId = btn.dataset.tab;
    document.getElementById("tab-matrix").style.display = (tabId === "matrix") ? "block" : "none";
    document.getElementById("tab-rules").style.display  = (tabId === "rules") ? "block" : "none";
    
    if (tabId === "rules" && !document.getElementById("rules-content").innerHTML) {
      loadRules();
    }
  });
});

async function loadRules() {
  const stem  = document.getElementById("stem").value.trim();
  const linga = document.getElementById("linga").value;
  const rc = document.getElementById("rules-content");
  rc.innerHTML = '<div class="muted">सूत्राणि सङ्गृह्यन्ते (Fetching all rules)...</div>';
  
  try {
    const r = await fetch(`/api/matrix/rules?stem=${encodeURIComponent(stem)}&linga=${encodeURIComponent(linga)}`);
    const data = await r.json();
    renderRules(data.rules);
  } catch (e) {
    rc.innerHTML = '<div class="error">दोषः: ' + e.message + '</div>';
  }
}

function renderRules(rules) {
  if (!rules || rules.length === 0) {
    document.getElementById("rules-content").innerHTML = '<div class="muted">न किञ्चित् सूत्रं प्राप्तम्।</div>';
    return;
  }
  
  let html = '<table class="rules-table">';
  html += '<tr><th>सूत्रम्</th><th>प्रकारः</th><th>रूपाणि (Forms)</th></tr>';
  
  rules.forEach(r => {
    html += '<tr>';
    html += `<td>
               <span class="sutra-text dev">${escapeHtml(r.text_dev)}</span>
               <span class="sutra-id">${escapeHtml(r.id)}</span>
             </td>`;
    html += `<td><span class="sutra-type dev">${escapeHtml(sutraTypeDev(r.type_dev))}</span></td>`;
    html += `<td>
               <div class="forms-list dev">${escapeHtml(r.forms.join(', '))}</div>
               <div class="cells-list">Vibhakti-Vacana cells: ${escapeHtml(r.cells.join(', '))}</div>
             </td>`;
    html += '</tr>';
  });
  
  html += '</table>';
  document.getElementById("rules-content").innerHTML = html;
}
"""

if "Tabs logic" not in content:
    content = content.replace("async function loadMatrix() {", js_additions + "\nasync function loadMatrix() {")

    # We also want loadMatrix to clear the rules-content so it fetches anew if stem changes
    load_matrix_addition = """
  document.getElementById("rules-content").innerHTML = ""; // clear old rules
"""
    content = content.replace("status.innerHTML = '<span class=\"loading\"></span> चतुर्विंशतिः कोष्ठाः व्युत्पाद्यन्ते…';",
                              "status.innerHTML = '<span class=\"loading\"></span> चतुर्विंशतिः कोष्ठाः व्युत्पाद्यन्ते…';" + load_matrix_addition)


with open("webui/templates/matrix.html", "w") as f:
    f.write(content)

