'use strict';
const notes = [...document.querySelectorAll('.note')];
const search = document.querySelector('#search');
const source = document.querySelector('#source-filter');
const evidence = document.querySelector('#evidence-filter');
const topics = [...document.querySelectorAll('.topics button')];
const count = document.querySelector('#count');
let topic = '';
const searchable = notes.map(note => ({note, text: note.textContent.normalize('NFKD').toLowerCase()}));
function filter() {
  const words = search.value.normalize('NFKD').toLowerCase().trim().split(/\s+/).filter(Boolean);
  let visible = 0;
  for (const {note,text} of searchable) {
    const match = (!topic || note.dataset.topic === topic) && (!source.value || note.dataset.source === source.value) && (!evidence.value || note.dataset.evidence === evidence.value) && words.every(word => text.includes(word));
    note.hidden = !match;
    if (match) visible++;
  }
  count.textContent = `${visible} ${visible === 1 ? 'note' : 'notes'} of ${notes.length}`;
  document.querySelector('#empty').hidden = visible > 0;
}
search.addEventListener('input', filter);
source.addEventListener('change',filter);
evidence.addEventListener('change',filter);
for (const button of topics) button.addEventListener('click',() => {
  topic=button.dataset.topic;
  for (const item of topics) item.setAttribute('aria-pressed',String(item===button));
  filter();
});
function clearFilters() {
  search.value=''; source.value=''; evidence.value=''; topic='';
  topics.forEach(button => button.setAttribute('aria-pressed',String(button.dataset.topic==='')));
  filter();
}
document.querySelector('#clear').addEventListener('click',clearFilters);
document.querySelector('#copy').addEventListener('click',async () => {
  const field=document.querySelector('#agent-prompt');
  const status=document.querySelector('#copy-status');
  try {
    await navigator.clipboard.writeText(field.value);
    status.textContent='Copied to clipboard';
  } catch {
    field.focus(); field.select();
    status.textContent='Failed to copy. Select the prompt and copy it manually.';
  }
});
window.addEventListener('hashchange',() => {
  const target=document.getElementById(decodeURIComponent(location.hash.slice(1)));
  if(target?.classList.contains('note') && target.hidden) {clearFilters();target.scrollIntoView();}
});
