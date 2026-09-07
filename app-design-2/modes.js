/* Agent-mode prompts, and the copy buttons that hand them over.
   One prompt per mode. Each is written to be pasted at the START of a message — the rest of
   the message is whatever the student actually wants to ask. */
const MODES = [
  { k:"EXPLAIN", t:"Explain, do not write",
    p:"EXPLAIN mode. Read the code I give you and explain what it actually does, line by line, in "
     +"plain language. Then ask me three questions about it that I should be able to answer if I "
     +"understood it. Do not write any new code. Do not suggest improvements yet." },
  { k:"REVIEW", t:"Review what I wrote",
    p:"REVIEW mode. I have already written this. Name up to three things you would change and say "
     +"why each one matters — naming, structure, an edge case I missed. Do not rewrite it for me "
     +"and do not give me the corrected file. I want to make the changes myself." },
  { k:"DEBUG", t:"Help me find it",
    p:"DEBUG mode. Something is wrong and I want to find it myself. Ask me what I expected and "
     +"what actually happened. Narrow it down with me — point at the region or the line worth "
     +"checking and tell me what to look for there. DO NOT tell me the fix and DO NOT write "
     +"corrected code, even if I ask. Stop when I say I have found it." },
  { k:"PAIR", t:"Build it with me",
    p:"PAIR mode. We are building this together. Before you write anything, ask me what I want it "
     +"to do. Then work in small steps: one step, show me, wait for me to say go. Explain any line "
     +"I would not have written myself." },
  { k:"SPEC", t:"I specify, you build",
    p:"SPEC mode. Below is my specification. Build exactly what it says — no more, no less, and do "
     +"not fill gaps with what you assume I meant. When you are done, list every place my spec was "
     +"vague or silent and what you had to guess." },
];

document.addEventListener("DOMContentLoaded", () => {
  const host = document.getElementById("modes");
  if (!host) return;
  host.innerHTML = MODES.map((m, i) => `
    <div class="md">
      <div><span class="md-k">${m.k}</span><span class="md-t">${m.t}</span></div>
      <button class="md-b" type="button" data-i="${i}">Copy prompt</button>
    </div>`).join("");
  host.addEventListener("click", async e => {
    const b = e.target.closest(".md-b"); if (!b) return;
    const text = MODES[Number(b.dataset.i)].p;
    try { await navigator.clipboard.writeText(text); }
    catch (err) {
      const ta = document.createElement("textarea");
      ta.value = text; document.body.appendChild(ta); ta.select();
      document.execCommand("copy"); ta.remove();
    }
    const was = b.textContent; b.textContent = "Copied"; b.classList.add("ok");
    setTimeout(() => { b.textContent = was; b.classList.remove("ok"); }, 1500);
  });
});
