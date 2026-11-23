"""Warning Label for Humans — make.fun entry.

Brief (competition.yaml, confirmed): one line, 1-160 chars, the safety
warning label that should come printed on every human being. Funny first,
plausible second. Judge weighs, in order: (1) is a warning label for
humans and funny; (2) laugh lands in one read, turn in the last few
words; (3) feels true about people in general (recognition); (4) sounds
like a real printed label; (5) fits 160 chars, no filler, no second idea.

Candidates weighed:
1. "WARNING: This human insists it has read the terms and conditions.
   It has not." — CHOSEN (77 chars). Universal: everyone has clicked
   "I agree" without reading. Deadpan, real label voice, and the turn is
   two words at the very end. Bonus: the label complains about labels.
   REVISION (pass 2): "will insist" -> "insists". A printed label states
   facts in the present tense, like a spec, not predictions — tighter,
   more deadpan, 81 -> 77 chars. Re-checked head-to-head against the
   runner-up ("five minutes away" ETA lie) and the chosen line still wins:
   universal flaw beats a narrower, well-worn joke shape.
2. "WARNING: This unit will say 'I'm five minutes away' while still in
   bed." — runner-up. Very recognizable lie, good "unit" label voice,
   turn at the end. Loses to #1: the flaw is narrower (only people who
   lie about ETA), and "five minutes away" is a well-worn joke shape.
3. "WARNING: Contains a person who will say 'just one more episode'
   until 4 a.m." — strong recognition, but "just one more episode" is a
   stock punchline; the turn is visible from the setup.
4. "CAUTION: This human will Google its symptoms, ignore the doctor, and
   trust a forum user named xX_healer_Xx." — vivid, but three beats is a
   second idea; judge criterion 5 punishes that.
5. "CAUTION: Contents may suddenly believe a 3 a.m. Wikipedia page
   qualifies as research." — funny, but "contents" is generic and the
   laugh is smeared across the line instead of landing at the end.
"""

import os

LINE = "WARNING: This human insists it has read the terms and conditions. It has not."

def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    text = LINE.strip()
    assert 1 <= len(text) <= 160, "gate: entry must be 1-160 chars"
    assert text.strip(), "gate: entry must not be only whitespace"
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(text)

if __name__ == "__main__":
    main()
