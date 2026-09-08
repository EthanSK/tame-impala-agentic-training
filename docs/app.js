'use strict';
const notes = [...document.querySelectorAll('.note')];
const search = document.querySelector('#search');
const source = document.querySelector('#source-filter');
const evidence = document.querySelector('#evidence-filter');
const topic = document.querySelector('#topic-filter');
const techniques = [...document.querySelectorAll('.topics button')];
const countNumber = document.querySelector('#count-number');
const countLabel = document.querySelector('#count-label');
const empty = document.querySelector('#empty');
let technique = '';
const searchable = notes.map(note => ({note, text: note.textContent.normalize('NFKD').toLowerCase()}));
function filter() {
  const words = search.value.normalize('NFKD').toLowerCase().trim().split(/\s+/).filter(Boolean);
  let visible = 0;
  for (const {note, text} of searchable) {
    const match = (!technique || note.dataset.technique === technique) && (!topic.value || note.dataset.topic === topic.value) && (!source.value || note.dataset.source === source.value) && (!evidence.value || note.dataset.evidence === evidence.value) && words.every(word => text.includes(word));
    note.hidden = !match;
    if (match) visible++;
  }
  countNumber.textContent = String(visible);
  countLabel.textContent = visible === notes.length ? (visible === 1 ? 'note' : 'notes') : `of ${notes.length} notes`;
  empty.hidden = visible > 0;
}
search.addEventListener('input', filter);
source.addEventListener('change', filter);
topic.addEventListener('change', filter);
evidence.addEventListener('change', filter);
for (const button of techniques) button.addEventListener('click', () => {
  technique = button.dataset.technique;
  for (const item of techniques) item.setAttribute('aria-pressed', String(item === button));
  filter();
});
function clearFilters() {
  search.value = ''; source.value = ''; evidence.value = ''; topic.value = ''; technique = '';
  techniques.forEach(button => button.setAttribute('aria-pressed', String(button.dataset.technique === '')));
  filter();
}
document.querySelector('#clear').addEventListener('click', clearFilters);
const disclosure = document.querySelector('#agent-disclosure');
document.querySelector('#copy').addEventListener('click', async () => {
  const field = document.querySelector('#agent-prompt');
  const status = document.querySelector('#copy-status');
  try {
    await navigator.clipboard.writeText(field.value);
    status.textContent = "Agent prompt copied to clipboard";
  } catch {
    disclosure.open = true;
    document.querySelector('#agent-instructions').open = true;
    field.focus(); field.select();
    status.textContent = "Failed to copy. Select the prompt text and copy it manually.";
  }
});
function revealHash() {
  const id = decodeURIComponent(location.hash.slice(1));
  // The agent setup starts collapsed; a link straight to it (nav, README) opens it.
  if (id === 'agents' || id === 'agent-disclosure' || id === 'agent-instructions' || id === 'agent-prompt') disclosure.open = true;
  const target = document.getElementById(id);
  if (target?.classList.contains('note') && target.hidden) { clearFilters(); target.scrollIntoView(); }
}
window.addEventListener('hashchange', revealHash);

revealHash();
